#!/usr/bin/python

import qrcode

# The URL you want to convert to QR code
url = "https://wa.me/6285194996351"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
img.save("qrcode.png")

# Display the image (optional, if you have PIL installed)
img.show()
