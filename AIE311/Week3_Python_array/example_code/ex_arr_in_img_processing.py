import cv2
import numpy as np

img = cv2.imread('bus.jpg') 
print(img.shape)
height, width, _ = img.shape
print(height, width)

img_array = np.random.randint(0, 50, size=(height, width, 3), dtype=np.uint8)
out_img = img + img_array
cv2.imshow('image', out_img)
cv2.waitKey(0)
cv2.destroyAllWindows()