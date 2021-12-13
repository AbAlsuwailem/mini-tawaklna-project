import sqlite3
import Individuals
def createTable():
    try:
       conn = sqlite3.connect("tdatabase.db")

       conn.execute('''CREATE TABLE tawaklna
                  (
                  FIRSTNAME TEXT NOT NULL,
                    LASTNAME TEXT NOT NULL,
                  SEX TEXT NOT NULL,
                  ID INT NOT NULL,
                  YearOfBirth TEXT NOT NULL,
                  vaccine TEXT NOT NULL,
                  DATEANDTIME TEXT NOT NULL,
                  PHONENUMBER TEXT NOT NULL,
                  PRIMARY KEY(ID,DATEANDTIME));''')

       conn.close()
       return 'created'
    except:
        return 'exsit'
def insret(ind):
    try:

        conn = sqlite3.connect("tdatabase.db")
        conn.execute("""INSERT INTO tawaklna  \
               VALUES (?,?,?,?,?,?,?,?)""",( ind.firtName, ind.lastname, ind.sex,ind.Id, ind.yearofB, ind.vacType, ind.dateTime, ind.phoneNum))
        conn.commit()
        conn.close()
        return True
    except:
        return False
def retrive(id):
    conn = sqlite3.connect("tdatabase.db")
    cursor = conn.execute(f"SELECT vaccine from tawaklna where ID=id")

    conn.close()
    return cursor[0]
def check(id):
    conn=sqlite3.connect("tdatabase.db")
    mycursor=conn.cursor()
    result=mycursor.execute("""select ID from tawaklna""")
   # result=mycursor.fetchall()
    count=0
    for row in result:

        if str(row[0]) == id:
            count+=1
    return count
def retrieveAll(self):
    retrieve=[]
    conn=sqlite3.connect("tdatabase.db")
    mycursor=conn.cursor()
    mycursor.execute("SELECT * FROM tawaklna")
    result=mycursor.fetchall()
    for row in result:
        retrieve.append(row)

    conn.close()
    return retrieve
def insretListOfRecords(listOfInd):
    try:
        conn = sqlite3.connect("tdatabase.db")
        for i in listOfInd:
            conn.execute("""INSERT INTO tawaklna  \
                  VALUES (?,?,?,?,?,?,?,?)""", (
            i.firtName, i.lastname, i.sex, i.Id, i.yearofB, i.vacType, i.dateTime, i.phoneNum))
        conn.commit()
        conn.close()
        return True
    except:
        return False






















