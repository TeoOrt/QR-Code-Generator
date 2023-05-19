import qrcode


def create_qr_code(url, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)


# Link of the image
# Replace it
url = "https://teoort.github.io/AQO_LinkTree/"
filename = "AQO.png"

# Save the image into the qr code
create_qr_code(url, filename)
