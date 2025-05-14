from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687",auth=("neo4j","12345678"))
def ikok(ok,password,gmail,id):
  
    with driver.session() as session:
        session.run('CREATE (u:Korisnik {name:$name,password:$pass,gmail:$gmail,id:$id})',{
            "name":ok,
            "pass":password,
            "gmail":gmail,
            "id":id,
         
        })
def getAll():
   
    with driver.session() as session:
        res = session.run("MATCH (u:Korisnik) RETURN u.name AS name,u.gmail AS gmail")
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