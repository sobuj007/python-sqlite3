import sqlite3

def createtable():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS stor (item TEXT,quantity INTEGER,price REAL)")
    conn.commit()
    conn.close()

def insertdata(item,quantity,price):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO stor VALUES(?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()

def displaydata():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM stor")
    rows=cur.fetchall()
    conn.close()
    return rows

def deletedata(item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM stor WHERE item = ?",(item,))
    conn.commit()
    conn.close()

def updata(item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE stor SET quantity =?, price =? WHERE item = ?",(quantity,price,item))
    conn.commit()
    conn.close()

#insertdata("hellohi",5,150)
print(displaydata())
#deletedata("hello1")

print(displaydata())
#v=input("enter item:")
