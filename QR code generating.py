import qrcode
from PIL import Image

#放Data去encode個QR CODE 
data=input('HKPS')

#整QR CODE
qr=qrcode.QRCode(version=2,box_size=10,border=5)
qr.add_data(data)
qr.make(fit=True)

#整個QR code image
image=qr.make_image(fill='black',back_color='white')

#最後記得要save image
image.save('qr_code.png')
image.open('qr_code.png')