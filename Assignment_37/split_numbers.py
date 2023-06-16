import os
import cv2

img = cv2.imread('numbers.webp')
img2 = img

height, width, channels = img.shape
w_size = 100
h_size = 50
w = width/w_size
h = height/h_size

    
for i in range(h_size):
    if i%5 == 0:
        path = f'./{int(i/5)}'
        os.mkdir(path)
    for j in range(w_size):
        x = w * j
        y = h * i
        img = img[int(y):int(y+h), int(x):int(x+w)]
        cv2.imwrite(os.path.join(path ,str(j) + ".jpg"),img)
        img = img2
    