from io import BytesIO
import qrcode


def create_qrcode(payload: str, size=5) -> BytesIO:
    qr = qrcode.QRCode(
        version=1,
        box_size=size,
        border=0,
    )
    qr.add_data(payload)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    return qr_img