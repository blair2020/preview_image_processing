import cv2
import requests
import numpy as np

# url = 'http://36.112.130.153:7777/DSSPlatform/BROWSE/ARCHIVE_PGS/GF2/LEVEL1A/PMS1/20200317/GF2_PMS1_E127.7_N26.4_20200317_L1A0004677036.jpg'
# url = 'http://36.112.130.153:7777/DSSPlatform/BROWSE/ARCHIVE_PGS/GF2/LEVEL1A/PMS2/20200103/GF2_PMS2_E127.7_N26.3_20200103_L1A0004523322.jpg'
url = 'http://36.112.130.153:7777/DSSPlatform/BROWSE/ARCHIVE_PGS/GF2/LEVEL1A/PMS2/20191214/GF2_PMS2_E127.8_N26.3_20191214_L1A0004472573.jpg'
r = requests.get(url)
# 保存原图
with open(url.split('/')[-1], 'wb') as f:
    f.write(r.content)
# cv2读取图像
img = cv2.imdecode(np.frombuffer(r.content, np.uint8), cv2.IMREAD_COLOR)  # 直接解码网络数据
# 显示图像
# cv2.imshow('img', img)
# 处理图像
b, g, r = cv2.split(img)
img_processed = cv2.merge([b, b, g])
# 保存处理后图像
cv2.imwrite(url.split('/')[-1].replace('jpg', 'png'), img_processed)
# 显示处理后的图像
# cv2.imshow('img_processed', img_processed)
# cv2.waitKey(0)