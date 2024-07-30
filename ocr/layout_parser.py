import layoutparser as lp
import cv2

image = cv2.imread("/home/user/Desktop/code/ocr/data/page1.jpg")
image = image[..., ::-1] 
# model = lp.Detectron2LayoutModel('lp://PubLayNet/mask_rcnn_R_50_FPN_3x/config')
# model = lp.AutoLayoutModel('lp://EfficientDete/PubLayNet')
model = lp.Detectron2LayoutModel('lp://PubLayNet/mask_rcnn_X_101_32x8d_FPN_3x/config')
layout = model.detect(image)
# print(layout)
# lp.draw_box(image, layout, box_width=3).show()

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

# 이미지 로드
image_path = '/home/user/Desktop/code/ocr/data/page2.jpg'  # 여기에 이미지 파일 경로를 넣으세요
image = Image.open(image_path)
image_width, image_height = image.size

class Rectangle:
    def __init__(self, x_1, y_1, x_2, y_2):
        self.x_1 = x_1
        self.y_1 = y_1
        self.x_2 = x_2
        self.y_2 = y_2

class TextBlock:
    def __init__(self, block, text=None, id=None, type=None, parent=None, next=None, score=None):
        self.block = block
        self.text = text
        self.id = id
        self.type = type
        self.parent = parent
        self.next = next
        self.score = score

# 박스 데이터 (예제 데이터를 사용합니다. 자신의 데이터를 여기에 넣으세요)
text_blocks = layout._blocks

print(text_blocks)
# 이미지 배경으로 설정
fig, ax = plt.subplots(1, figsize=(image_width / 100, image_height / 100))
ax.imshow(image)

# 각 텍스트 블록에 대해 박스 그리기
for block in text_blocks:
    rect = patches.Rectangle((block.block.x_1, block.block.y_1), 
                             block.block.x_2 - block.block.x_1, 
                             block.block.y_2 - block.block.y_1,
                             linewidth=2, edgecolor='r', facecolor='none')
    ax.add_patch(rect)

# 축과 눈금을 없애기
ax.axis('off')

# 결과 보여주기
plt.show()
plt.savefig('./example.png')