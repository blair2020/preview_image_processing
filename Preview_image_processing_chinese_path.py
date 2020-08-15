import requests
import cv2
import os
img_path = 'G:/GF2_PMS1_W115.0_N36.2_20200614_L1A0004870657-MSS1.jpg'
print(os.path.exists(img_path))
img = cv2.imread(img_path, 1)
print(img.shape)
b, g, r = cv2.split(img)
merged = cv2.merge([b, b, g])
# cv2.imwrite(os.path.dirname(img_path) + 'test.png', merged)
cv2.imwrite(img_path.replace('jpg', 'png'), merged)
# cv2.imshow('image', img)
# cv2.imshow("merged 1", merged)
# cv2.waitKey(0)