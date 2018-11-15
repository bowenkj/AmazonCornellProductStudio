import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="nozama",
    passwd="Nozama520!",
    database="shopro"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE users (name VARCHAR(255), address VARCHAR(255))")