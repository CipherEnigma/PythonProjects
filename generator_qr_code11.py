import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4,)
qr.add_data("www.linkedin.com/in/pragunie-a-6b0a56298")
qr.make(fit=True)
img=qr.make_image(fill_color="purple",back_color="white")
img.save("pragunie_web.png")