import os
import img2pdf
from wifi_qrcode_generator import wifi_qrcode



class WifiQrCode:
    def __init__(self, wifi_name: str, password: str, authentication_type=None, hidden: bool = False):
        """
        Initialize a WifiQrCode object.

        Args:
            wifi_name (str): The ssid of the wifi network.
            password (str): The password of the wifi network.
            authentication_type (str, optional): The authentication type of the wifi network.
            hidden (bool, optional): Whether the wifi network is hidden. Defaults to False.

        Attributes:
            ssid (str): The ssid of the wifi network.
            password (str): The password of the wifi network.
            authentication_type (str): The authentication type of the wifi network.
            hidden (bool): Whether the wifi network is hidden.
            downloads_folder (str): The path to the downloads folder.
            pdf_file_path (str): The path to the pdf file.
        """
        self.ssid: str = wifi_name
        self.password: str = password
        self.authentication_type: str = "WPA" if authentication_type is None else authentication_type
        self.hidden: bool = hidden
        self.downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        self.pdf_file_path = os.path.join(self.downloads_folder, "qr_code.pdf")

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
        Converts the QR code image to a PDF and saves it to the Downloads folder.

        This is done by using the img2pdf library to convert the QR code image to a PDF.
        """
        with open(self.pdf_file_path, "wb") as f:
            f.write(img2pdf.convert('static/asserts/wifi_qrcode.png'))



