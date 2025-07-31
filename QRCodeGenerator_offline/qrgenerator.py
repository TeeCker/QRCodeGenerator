import qrcode
import pay_by_square
from PIL import Image


code = pay_by_square.generate(
    beneficiary_name="Cat Paradise",
    iban="SK9809000000005211554196",
    swift="GIBASKBXXXX",
    amount=10,
    currency="EUR",
    constant_symbol="0308",
    note="Od mačičky Leušky ..."
)

qr_img = qrcode.make(code)
img = qr_img.get_image()
img = img.resize((490, 490))
img_back = Image.open("./qr-kod-ramik.png")

img_back.paste(img, (10, 10))
#img_back.show()
img_back.save("qr.png")
