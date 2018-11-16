from flask import Flask
from flask import render_template, request
from flask_qrcode import QRcode
from flask_bootstrap import Bootstrap
import select_query
# from flask_mysqldb import MySQL


app = Flask(__name__)
QRcode(app)
Bootstrap(app)
# mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def qrcode():
    if request.method == 'POST':
        return render_template('create_qrcode.html', isQR=True, id=request.form['product-id'])
    return render_template('create_qrcode.html', isQR=False)

# @app.route('/')


@app.route('/qr-reader', methods=['GET'])
def readqrcode():
    return render_template('read_qrcode.html')


@app.route('/test', methods=['GET'])
def test():
    return render_template('test.html')


@app.route('/product/<int:product_id>')
def showproduct(product_id):
    prod = select_query.getProductByID(product_id)[0]
    return render_template('product_detail.html', prod=prod)

@app.route('/dashboard/')
def dashboard():
    stores = select_query.getAllStores()
    return render_template('stores.html', stores=stores)

@app.route('/products')
def products():
    products = select_query.getAllProducts()
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
