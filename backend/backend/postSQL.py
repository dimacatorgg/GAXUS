from django.db import connection
import psycopg2 
from psycopg2.extras import RealDictCursor
#con = psycopg2.connect('postgres://avnadmin:AVNS_nqBWu8eKVfVxpvWL5lc@pg-2461e067-paypaldimitrijr-b09e.i.aivencloud.com:16437/defaultdb?sslmode=require')
con = psycopg2.connect('dbname=GAXUS password=123 user=postgres port=5432')
def testiraj():

    with con.cursor() as cs:
        #cs.execute("CREATE TABLE comments (idx VARCHAR(10000) NOT NULL,ime VARCHAR(1000) NOT NULL,idcom VARCHAR(10000) NOT NULL),poruka VARCHAR(10000) NOT NULL,up INT() NOT NULL,down INT() NOT NULL,rate INT() NOT NULL,)")
        cs.execute("SELECT * FROM comments")
        res = cs.fetchall()
      
        return res
    con.close()

def test():
   
    with con.cursor(cursor_factory=RealDictCursor) as cr:
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
    
    with con.cursor() as cs:
        cs.execute("SELECT about FROM aboutg WHERE idx=%s",[idx])
        nes = cs.fetchall()
        if nes:
            cs.execute("UPDATE aboutg SET about=%s  WHERE idx=%s",[updateg,idx])
            print("Updetovano")
        else:
            cs.execute("INSERT INTO aboutg (about,idx) VALUES(%s,%s)",[updateg,idx])
            print("Napravljeno")
def getDatag(user):
   

    with con.cursor(cursor_factory=RealDictCursor) as cs:
        cs.execute("SELECT aboutg FROM aboutg WHERE idx=%s",[user])
        gledaj = cs.fetchall()
        if gledaj:
            print(gledaj)
            return gledaj
          
        else:
            return "Nista"
def getabout(ids):

     with con.cursor(cursor_factory=RealDictCursor) as cs:
        cs.execute("SELECT about FROM aboutg WHERE idx=%s",[ids])
        res = cs.fetchall()
        return res
def upisi(idx,name,id,rate,poruka):
    
    with con.cursor(cursor_factory=RealDictCursor) as cs:
        cs.execute("INSERT INTO comments (idx,ime,up,down,idcom,rate,poruka) VALUES (%s,%s,0,0,%s,%s,%s)",[idx,name,id,rate,poruka])
        return "Upisan"
def komentari(idx):

    with con.cursor(cursor_factory=RealDictCursor) as cs:
        cs.execute("SELECT * FROM comments WHERE idx=%s",[idx])
        res = cs.fetchall()
        if res:

            print("Hello")
            return res
        else:
            return ""
            