import mysql.connector
import csv

mydb = mysql.connector.connect(
    host="localhost",
    user="nozama",
    passwd="Nozama520!",
    database="shopro"
)

cur = mydb.cursor()

sql = "INSERT INTO stores (name, location) VALUES (%s, %s)"
val = ('supreme', None)
cur.execute(sql, val)

mydb.commit()
print(cur.rowcount, "record inserted.")