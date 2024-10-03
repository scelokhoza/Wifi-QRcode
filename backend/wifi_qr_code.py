import os
import img2pdf
from wifi_qrcode_generator import wifi_qrcode



class WifiQrCode:
    def __init__(self, wifi_name: str, password: str, authentication_type=None, hidden: bool = False):
        self.ssid: str = wifi_name
        self.password: str = password
        self.authentication_type: str = "WPA" if authentication_type is None else authentication_type
        self.hidden: bool = hidden

    def generate_qr_code(self):
        return wifi_qrcode(
            ssid=self.ssid,
            hidden=self.hidden,
            authentication_type=self.authentication_type,
            password=self.password
        )


    def create_image(self) -> None:
        self.generate_qr_code().make_image().save('wifi_qrcode.pdf')


    def make_pdf_qr_code(self):
        with open("qr_code.pdf","wb") as f:
            f.write(img2pdf.convert('wifi_qrcode.png'))
            os.remove('wifi_qrcode.png')



