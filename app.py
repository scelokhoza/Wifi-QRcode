from flask import Flask, render_template, request, redirect, url_for
from backend.wifi_qr_code import WifiQrCode
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        wifi_name = request.form['wifi_name']
        password = request.form['password']
        auth_type = request.form['auth_type']
        hidden = 'hidden' in request.form

        qr_code = WifiQrCode(wifi_name, password, auth_type, hidden)
        qr_code.create_image()
        qr_code.make_pdf_qr_code()

        return redirect(url_for('display_qr'))
    return render_template('index.html')


@app.route('/qr')
def display_qr():
    return render_template('qr.html')



if __name__ == "__main__":
    app.run(debug=True)