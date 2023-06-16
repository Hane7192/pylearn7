import os
import cv2

img = cv2.imread('./part_1/numbers.webp')
img2 = img

height, width, channels = img.shape
w_size = 100
h_size = 50
w = width/w_size
h = height/h_size
k = 0

for i in range(h_size):  
    
    if i%5 == 0:
        path = f'./part_1/{int(i/5)}'
        os.mkdir(path)
        k = 0
    for j in range(w_size):
        x = w * j
        y = h * i
        img = img[int(y):int(y+h), int(x):int(x+w)]
        cv2.imwrite(os.path.join(path ,str(j+k*w_size) + ".jpg"),img)
        img = img2
    k += 1