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
        self.generate_qr_code().make_image().save('wifi_qrcode.png')



if __name__ == '__main__':
    wifi = WifiQrCode(
        wifi_name='TECNO POP 7',
        password='Prince@3108',
        authentication_type='WPA'
    )
    wifi.create_image()