from cnocr import CnOcr
import streamlit as st
from cnocr.utils import draw_ocr_results
from PIL import Image
import pickle

import matplotlib.pyplot as plt

img_fp = '/home/user/Desktop/code/ocr/data/paper_10.jpg'
ocr = CnOcr()  # 所有参数都使用默认值


# print(out)
img_obj = open(img_fp, 'rb')
print(img_obj)
image = Image.open(img_obj).convert('RGB')
print(image)
out = ocr.ocr(image)
print(type(out[1]["position"]))
print(out)
pickle.dump(out, open( "./result/ocr_output.p", "wb" ) )
draw_ocr_results(image, out, "./result/ocr_result.png", "/home/user/Desktop/code/test/docs/fonts/simfang.ttf" )