import qrcode as qr

img = qr.make("This is sample QR.")

img.save('sampleQR.png')