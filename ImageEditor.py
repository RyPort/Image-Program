# Hackathon project
# Ryan Porter
# Agusto Cohn
# Richard Bailey
from PIL import Image
import numpy as np

img = Image.open("ct.jpg")

# create an array from the image

img_ar = np.array(Image.open("ct.jpg"))

for row in img_ar:
    for pixel in row:
        pixel[0] = 0
        pixel[1] = 0
        pixel[2] = 0

img_2 = Image.fromarray(img_ar)




img_2.show()