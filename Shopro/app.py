from flask import Flask
from flask import render_template, request
from flask_qrcode import QRcode
from flask_bootstrap import Bootstrap



app = Flask(__name__)
QRcode(app)
Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def qrcode():
    if request.method == 'POST':
        return render_template('create_qrcode.html', isQR=True, id=request.form['product-id'])
    return render_template('create_qrcode.html', isQR=False)

# @app.route('/')

@app.route('/qr-reader', methods=['GET'])
def readqrcode():
    return render_template('read_qrcode.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
