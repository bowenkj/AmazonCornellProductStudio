from flask import Flask
from flask import render_template, request, redirect, url_for
from flask_qrcode import QRcode
from flask_bootstrap import Bootstrap
import select_query, insert_query, alter_query
# from flask_mysqldb import MySQL


app = Flask(__name__)
QRcode(app)
Bootstrap(app)
# mysql = MySQL(app)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username, password = request.form['username'], request.form['password']
        insert_query.addUser(username, password)
        user = select_query.getUser(username, password)
        return redirect(url_for('user_profile', user_id=user[0][0]))
    return render_template('register.html')


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username, password = request.form['username'], request.form['password']
        user = select_query.getUser(username, password)
        return redirect(url_for('user_profile', user_id=user[0][0]))
    return render_template('login.html')


@app.route('/user_profile/<user_id>')
def user_profile(user_id):
    user_id = int(user_id)
    user = select_query.getUserByID(user_id)
    username = user[0][0]
    return render_template('profile_page.html', username=username, user_id=user_id)


@app.route('/create_qrcode', methods=['GET', 'POST'])
def qrcode():
    if request.method == 'POST':
        return render_template('create_qrcode.html', isQR=True, id=request.form['product-id'])
    return render_template('create_qrcode.html', isQR=False)


@app.route('/qr-reader/<int:user_id>', methods=['GET'])
def scanqr(user_id):
    return render_template('qr-scanner.html', user_id=user_id)


@app.route('/product/<int:product_id>/<int:user_id>')
def showproduct(product_id, user_id=None):
    prod = select_query.getProductByID(product_id)[0]
    return render_template('product_detail.html', prod=prod, product_id=product_id, user_id=user_id)


@app.route('/updateProduct/<int:product_id>/<int:user_id>')
def updateproduct(product_id, user_id=None):
    if user_id:
        alter_query.addToWishlist(product_id, user_id)
    prod = select_query.getProductByID(product_id)[0]
    return render_template('product_detail.html', prod=prod, product_id=product_id, user_id=user_id)


@app.route('/dash')
def dashboard():
    print "reach here"
    stores = select_query.getAllStores()
    return render_template('stores.html', stores=stores)

@app.route('/products')
def products():
    products = select_query.getAllProducts()
    return render_template('products.html', products=products)

@app.route('/wishlist/<int:user_id>')
def wishlist(user_id):
    user = select_query.getUserByID(user_id)[0]
    name = user[0]
    product_ids = map(int, user[1].split(',')) if user[1] else []
    wishlist = []
    for product_id in product_ids:
        prod = select_query.getProductByID(product_id)[0]
        wishlist.append(prod)
    return render_template('wishlist.html', username=name, wishlist=wishlist, user_id=user_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
