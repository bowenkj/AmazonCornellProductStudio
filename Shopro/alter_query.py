import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="nozama",
    passwd="Nozama520!",
    database="shopro"
)

cur = mydb.cursor()


def addToWishlist(user_id, prod_id):
    cur.execute("SELECT * FROM users WHERE id = %d" % user_id)
    user = cur.fetchall()[0]
    product_ids = map(int, user[1].split(',')) if user[1] else []
    product_ids.append(prod_id)
    new_wishlist = ','.join(product_ids)
    print new_wishlist
    sql = "UPDATE users SET wishlist = %s WHERE id = %d"
    val = (new_wishlist, user_id)
    cur.execute(sql, val)
    mydb.commit()