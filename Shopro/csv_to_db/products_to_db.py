import mysql.connector
import csv

mydb = mysql.connector.connect(
    host="localhost",
    user="nozama",
    passwd="Nozama520!",
    database="shopro"
)

cur = mydb.cursor()

sql = "INSERT INTO products VALUES (%d, %s, %s, %f, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

with open('Database - Product.csv') as csvfile:
    reader = csv.reader(csvfile)
    for idx, row in enumerate(reader):
        if idx == 0:
            continue
        id = int(row[0])
        name = row[1]
        size = row[2]
        price = row[3]
        color = row[4]
        brand = row[5]
        description = row[6]
        model_info = row[7]
        composition = row[8]
        measure = row[9]
        other_info = row[10]
        pic1 = row[11]
        pic2 = row[12]
        pic3 = row[13]
        val = (id, name, size, price, color, brand, description, model_info, composition, measure, other_info, pic1,
               pic2, pic3)
        # cur.execute(sql, val)
        # cur.commit()
        print val,
        print ","




