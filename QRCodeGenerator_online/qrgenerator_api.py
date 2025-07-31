import requests
import base64
import json

#format = "png"
#beneficiary_name = "OZ OPUSTENÉ MAČKY"
#iban = "SK9783300000002401904587"
#amount = "10"
#currency = "EUR"
#cs = "0308"
#payment_note = "Od mačičky Leušky ..."
#unit_size = "512"

format = "png"
beneficiary_name = "Cat Paradise"
iban = "SK9809000000005211554196"
amount = "10"
currency = "EUR"
cs = "0308"
payment_note = "Od mačičky Leušky ..."
unit_size = "512"

url = "https://api.QRGenerator.sk/by-square/pay/base64?format="+format+"&iban="+iban+"&amount="+amount+"&currency="+currency+"&cs="+cs+"&beneficiary_name="+beneficiary_name+"&payment_note="+payment_note+"&unit_size="+unit_size+""

r = requests.get(url)

data_json = json.loads(r.content)
coded_img_data = data_json.get("data")
decoded_img_data = base64.b64decode(coded_img_data)

with open('qr.png', 'wb') as f:
    f.write(decoded_img_data)
    f.close

