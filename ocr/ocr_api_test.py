import requests
import json

image_fp = '/home/user/Desktop/code/ocr/data/page0.jpg'
r = requests.post(
    'http://0.0.0.0:8822/ocr_page', 
    # files={'image': open(image_fp, 'rb')},
    files={'image': (image_fp, open(image_fp, 'rb'), 'image/png')},
)
# ocr_out = r.json()['results']
print(r)


