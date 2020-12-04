import qrcode

image = qrcode.make("https://www.google.com")
image.save("qr.png", "PNG")
