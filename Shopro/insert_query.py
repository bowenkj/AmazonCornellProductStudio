import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="nozama",
    passwd="Nozama520!",
    database="shopro"
)

cur = mydb.cursor()


def addUser(username, password):
    sql = "INSERT INTO users (name, password) VALUES (%s, %s)"
    val = (username, password)
    cur.execute(sql, val)

    mydb.commit()
    print(cur.rowcount, "record inserted.")