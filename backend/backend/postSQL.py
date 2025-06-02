from django.db import connection
def create():
    with connection.cursor() as cs:
        cs.execute("INSERT INTO post (name) VALUES (%s)",["sigma"])

def joj(napravi):
    with connection.cursor() as cs:
        cs.execute("INSERT INTO post (name) VALUES (%s)",[napravi])
        return "napravljeno"
def getAll():
    with connection.cursor() as cs:
       cs.execute("SELECT * FROM post")
       res = cs.fetchall()
       return res
def userIfno(updateg,idx):
    with connection.curosr() as cs:
        cs.execute("SELECT * FROM infoUser WHERE idx=%s",[idx])
        if (cs.fetchall()):
            cs.execute("UPDATE infoUser SET about=%s  WHERE idx=%s",[updateg,idx])
        else:
            cs.execute("INSERT INTO infoUser VALUES(%s,%s)",[updateg,idx])
        