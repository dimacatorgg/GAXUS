from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687",auth=("neo4j","12345678"))
def ikok(ok,password,gmail,id):
  
    with driver.session() as session:
        session.run('CREATE (u:Userd {name:$name,password:$pass,gmail:$gmail,id:$id,verif:$kuk})',{
            "name":ok,
            "pass":password,
            "gmail":gmail,
            "id":id,
            "kuk":False
        })
def getAll():
   
    with driver.session() as session:
        res = session.run("MATCH (u:Userd) RETURN u.name AS name,u.gmail AS gmail")
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
            MATCH (u:Userd)
            WHERE ($a1 IS NOT NULL AND u.name = $a1)
               OR ($a2 IS NOT NULL AND u.gmail = $a2)
            RETURN u LIMIT 1
        """, {"a1": name, "a2": gmail})

    
        return result.single() is not None
def proverin(ime,sifra):
    with driver.session() as session:
        res = session.run("MATCH (u:Userd) WHERE (u.name=$nes1 AND u.password=$nes2) RETURN u.id AS jupi",{
            "nes1":ime,
            "nes2":sifra
        })
        if res.single():
            return True
        else:
            return False
def dobijid(ime):
    with driver.session() as session:
        res = session.run("MATCH (u:Userd) WHERE u.name=$joj RETURN u.id AS id",{
            "joj":ime
        })
        return res.single()["id"]
def dobijpodatke(idx):
    with driver.session() as session:
        res = session.run("MATCH (u:Userd) WHERE u.id=$idx2 RETURN u AS sve",{
            "idx2":idx
        })
        li = []
        for i in res:
            li.append(i.data()["sve"])
        return li
def uzmisvepodtke(id):
    with driver.session() as session:
        res = session.run("MATCH (u:Userd) WHERE u.id = $idx RETURN u AS sve",{
            "idx":id
        })
        ku = []
        for i in res:
            ku.append(i.data()["sve"])
        return ku
def prijatelji(name):
    with driver.session() as session:
        ref = session.run("MATCH (u:Userd) WHERE u.name =~ $kok RETURN u AS sve", {
            "kok": f".*{name}.*"
        })
        hir = []
        for i in ref:
            hir.append(i.data()["sve"])
        return hir
def friendadd(user1,user2):
    with driver.session() as session:
        session.run("MATCH (u1:Userd {name:$user1}), (u2:Userd {name:$user2}) CREATE (u1)-[:FRIENDY]->(u2)",{
            "user1":user1,
            "user2":user2
        })
        return "Hju"
def prijatelj(user):
    with driver.session() as session:
        h = session.run("MATCH (u:Userd {name:$k})-[:FRIENDY]->(friend) RETURN friend AS sve",{
            "k":user
        })
        gu = []
        for i in h:
            gu.append(i.data()["sve"])
        return gu
def dodaj(k1,k2):
    with driver.session() as session:
        session.run("MATCH (u1:Userd {name:$ko}),(u2:Userd {name:$ko2}) WITH u1,u2 CREATE (u1)-[:FRIENDY]->(u2)",{
            "ko":k1,
            "ko2":k2
        })
       
        return "ddfsd"
def delete(k1,k2):
    with driver.session() as session:
        session.run("MATCH (u1:Userd {name:$k1}),(u2:Userd {name:$k2}) MATCH (u1)-[r:FRIENDY]->(u2) DELETE r",{
            "k1":k1,
            "k2":k2
        })
        return "Uspeno uradjeno"
def sigma(user):
    with driver.session() as session:
        run = session.run("MATCH (u:Userd) WHERE u.name=$name RETURN u AS sve",{
            "name":user
        })
        kuk = run.data()
        if kuk:

            return kuk[0]["sve"]
        else:
            return "Nema takovg korniska prestani da hakijes"
def friendcheck(u1,u2):
    with driver.session() as session:
        run = session.run("MATCH (u1:Userd {name:$u1}),(u2:Userd {name:$u2}) MATCH (u1)-[r:FRIENDY]->(u2) RETURN COUNT(r) AS broj ",{
            "u1":u1,
            "u2":u2
        })
        return run.data()[0]["broj"]
#Hey here