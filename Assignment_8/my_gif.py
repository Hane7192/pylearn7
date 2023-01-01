import os
import imageio

file_list = sorted(os.listdir("gif_frames"))
IMAGES =[]

for file_name in file_list:
    file_path = "gif_frames/" + file_name
    image = imageio.imread(file_path)
    IMAGES.append(image)

imageio.mimsave("my_gif.gif", IMAGES, fps=10)