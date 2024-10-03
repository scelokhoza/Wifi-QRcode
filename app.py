from flask import Flask, render_template, request, redirect, url_for
from backend.wifi_qr_code import WifiQrCode
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Handles the root route for the app.

    If a POST request is made, it handles the form submission and creates a QR code
    based on the form data. The QR code is then saved as an image and a PDF, and
    the user is redirected to the /qr route to view the QR code.

    If a GET request is made, it simply renders the index.html template.
    """
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
    """
    Displays the QR code that was generated based on the user's form submission.

    The QR code is displayed in the qr.html template, which is rendered by this
    function.

    Returns:
        The rendered qr.html template.
    """
    return render_template('qr.html')



if __name__ == "__main__":
    app.run(debug=True)