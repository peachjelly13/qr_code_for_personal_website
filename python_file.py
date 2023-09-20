import qrcode as qr
from PIL import Image
qr_ = qr.QRCode(version =3,error_correction=qr.constants.ERROR_CORRECT_H,box_size=10,border=3)
qr_.add_data("https://luminous-sawine-5ec143.netlify.app/")
qr_.make(fit=True)
img = qr_.make_image(fill_color="yellow",back_color="blue")
img.save("websiteqr.png")