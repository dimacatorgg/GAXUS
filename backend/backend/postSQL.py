from django.db import connection
import psycopg2 
from psycopg2.extras import RealDictCursor

def test():
    with psycopg2.connect("dbname=GAXUS user=postgres host=localhost password=123") as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cr:
            cr.execute("SELECT * FROM aboutg")
            row = cr.fetchall()
            return row
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
    with psycopg2.connect("dbname=GAXUS user=postgres password=123") as connections:
        with connections.cursor() as cs:
            cs.execute("SELECT about FROM aboutg WHERE idx=%s",[idx])
            nes = cs.fetchall()
            if nes:
                cs.execute("UPDATE aboutg SET about=%s  WHERE idx=%s",[updateg,idx])
                print("Updetovano")
            else:
                cs.execute("INSERT INTO aboutg (about,idx) VALUES(%s,%s)",[updateg,idx])
                print("Napravljeno")
def getDatag(user):
    with connection.cursor() as cs:
        cs.execute("SELECT aboutg FROM aboutg WHERE idx=%s",[user])
        gledaj = cs.fetchall()
        if gledaj:
            print(gledaj)
            return gledaj
          
        else:
             return "Nista"
def getabout(ids):
    with psycopg2.connect("dbname=GAXUS user=postgres password=123") as con:
        with con.cursor(cursor_factory=RealDictCursor) as cs:
            cs.execute("SELECT about FROM aboutg WHERE idx=%s",[ids])
            res = cs.fetchall()
            return res