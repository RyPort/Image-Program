# Hackathon project
# Ryan Porter
# Agusto Cohn
# Richard Bailey
from PIL import Image
import numpy as np

img = Image.open("ct.jpg")

# create an array from the image

img_ar = np.array(Image.open("ct.jpg"))


for x in range(len(img_ar)):
    for y in range(len(img_ar[0])):
        img_ar[x][y][0] = 0
        img_ar[x][y][1] = 0
        img_ar[x][y][2] = 255

img_2 = Image.fromarray(img_ar)




img_2.show()
