# Hackathon project
# Ryan Porter
# Agusto Cohn
# Richard Bailey
from PIL import Image
import numpy as np


def averagePixel(image_ar, y, x, inc):
    # store total rgb value
    r = 0
    g = 0
    b = 0
    
    for i in range(y, y+inc):
        for j in range(x, x+inc):
            r += image_ar[i][j][0]
            g += image_ar[i][j][1]
            b += image_ar[i][j][2]
    # get average pixel values
    r = r / (inc * inc)
    g = g / (inc * inc)
    b = b / (inc * inc)

    # set average pixel values
    for i in range(y, y+inc):
        for j in range(x, x+inc):
            image_ar[i][j][0] = r
            image_ar[i][j][1] = g
            image_ar[i][j][2] = b
        


# create an array from the image

img_ar = np.array(Image.open("ct.jpg"))

inc = 10
for y in range(0,len(img_ar),inc):
    for x in range(0,len(img_ar[0]),inc):
        averagePixel(img_ar,y,x,inc)


img_2 = Image.fromarray(img_ar)




img_2.show()
