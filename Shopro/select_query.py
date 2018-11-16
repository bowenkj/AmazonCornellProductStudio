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

def getUserByID(id):
    cur.execute("SELECT name, wishlist FROM users WHERE id = %d" % id)
    return cur.fetchall()

def getAllUsers():
    cur.execute("SELECT * FROM users")
    return cur.fetchall()

def getUser(username, password):
    sql = "SELECT * FROM users WHERE name = %s and password = %s"
    val = (username, password)
    cur.execute(sql, val)
    return cur.fetchall()




#
# user = getUserByID(123221405)[0]
# name = user[0]
# wishlist = map(int, user[1].split(','))
# print wishlist
