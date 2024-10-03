import img2pdf
from wifi_qrcode_generator import wifi_qrcode



class WifiQrCode:
    def __init__(self, wifi_name: str, password: str, authentication_type=None, hidden: bool = False):
        """
        Constructor for WifiQrCode.

        Args:
        wifi_name (str): The name of the wifi network.
        password (str): The password of the wifi network.
        authentication_type (str, optional): The authentication type of the wifi network. Defaults to None.
        hidden (bool, optional): Whether the wifi network is hidden. Defaults to False.

        """
        self.ssid: str = wifi_name
        self.password: str = password
        self.authentication_type: str = "WPA" if authentication_type is None else authentication_type
        self.hidden: bool = hidden

    def generate_qr_code(self):
        """
        Generates a QR code for the given wifi credentials.

        Returns:
        wifi_qrcode object: The QR code for the given wifi credentials.
        """
        return wifi_qrcode(
            ssid=self.ssid,
            hidden=self.hidden,
            authentication_type=self.authentication_type,
            password=self.password
        )


    def create_image(self) -> None:
        """
        Creates an image of the QR code and saves it to a file.

        """
        self.generate_qr_code().make_image().save('static/asserts/wifi_qrcode.png')


    def make_pdf_qr_code(self):
        """
        Converts the QR code image to a PDF and saves it to a file.

        This is done by using the img2pdf library to convert the QR code image to a PDF.

        The PDF is saved to a file named 'qr_code.pdf'.

        """
        with open("qr_code.pdf","wb") as f:
            f.write(img2pdf.convert('wifi_qrcode.png'))



