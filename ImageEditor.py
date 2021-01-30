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
    incx = 0
    incy = 0
    
    if x+inc > len(image_ar[0]):
        incx = len(image_ar[0]) - x
    else:
        incx = inc
    
    if y+inc > len(image_ar):
        incy = len(image_ar) - y
    else:
        incy = inc
    
    for i in range(y, y+incy):
        for j in range(x, x+incx):
                r += image_ar[i][j][0]
                g += image_ar[i][j][1]
                b += image_ar[i][j][2]
                
                
    # get average pixel values
    r = r / (incx * incy)
    g = g / (incx * incy)
    b = b / (incx * incy)

    # set average pixel values
    for i in range(y, y+incy):
        for j in range(x, x+incx):
            image_ar[i][j][0] = r
            image_ar[i][j][1] = g
            image_ar[i][j][2] = b
     


# create an array from the image

#img_ar = np.array(Image.open("ct.jpg"))
#img_ar = np.array(Image.open("gator.jpg"))
img_ar = np.array(Image.open("download.jpg"))

inc = 13
for y in range(0,len(img_ar),inc):
    for x in range(0,len(img_ar[0]),inc):
        averagePixel(img_ar,y,x,inc)



img_2 = Image.fromarray(img_ar)




img_2.show()
