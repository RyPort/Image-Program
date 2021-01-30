# Hackathon project
# Ryan Porter
# Agusto Cohn
# Richard Bailey
from PIL import Image
import numpy as np

img = Image.open("ct.jpg")

img_chn_red = np.zeros(img.shape,dtype='uint8')
img_chn_red[:,:,0] = img[:,:,0]
img_red = Image.fromarray(img_chn_red)
img_red.show()


