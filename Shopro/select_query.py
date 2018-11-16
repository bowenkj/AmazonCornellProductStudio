import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="nozama",
    passwd="Nozama520!",
    database="shopro"
)

cur = mydb.cursor()


def getAllStores():
    cur.execute("SELECT * FROM stores")
    return cur.fetchall()

def getAllProducts():
    cur.execute("SELECT * FROM products")
    return cur.fetchall()

def getProductByID(id):
    cur.execute("SELECT * FROM products WHERE id = %d" % id)
    return cur.fetchall()
