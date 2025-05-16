from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687",auth=("neo4j","12345678"))
def ikok(ok,password,gmail,id):
  
    with driver.session() as session:
        session.run('CREATE (u:Users {name:$name,password:$pass,gmail:$gmail,id:$id})',{
            "name":ok,
            "pass":password,
            "gmail":gmail,
            "id":id,
         
        })
def getAll():
   
    with driver.session() as session:
        res = session.run("MATCH (u:Users) RETURN u.name AS name,u.gmail AS gmail")
        ol = []
        for i in res:
            ol.append(i.data()['name'])
        return ol
def getdata(nes):
  
    with driver.session() as session:
        result =  session.run('MATCH (u:Korisnik {id:$kurs}) RETURN u.name AS name,u.gmail AS gmail',{
            "kurs":nes
        })
        jos = result.single()
        if jos:
            return jos["name"]
        else:
            return None
def proveri(name,gmail):
    with driver.session() as session:
        result = session.run("""
            MATCH (u:Users)
            WHERE ($a1 IS NOT NULL AND u.name = $a1)
               OR ($a2 IS NOT NULL AND u.gmail = $a2)
            RETURN u LIMIT 1
        """, {"a1": name, "a2": gmail})

    
        return result.single() is not None
def proverin(ime,sifra):
    with driver.session() as session:
        res = session.run("MATCH (u:Users) WHERE (u.name=$nes1 AND u.password=$nes2) RETURN u.id AS jupi",{
            "nes1":ime,
            "nes2":sifra
        })
        if res.single():
            return True
        else:
            return False
def dobijpodatke(idx):
    with driver.session() as session:
        res = session.run("MATCH (u:Users {id:$idx2})",{
            "idx2":idx
        })
        li = []
        for i in res:
            li.append(i.data())
        return li