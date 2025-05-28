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
        