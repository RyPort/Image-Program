# Hackathon project
# Ryan Porter
# Agusto Cohn
# Richard Bailey
from PIL import Image
import numpy as np

img = Image.open("ct.jpg")
img_data = np.array(img)
img_chn_red = np.zeros(img_data.shape,dtype='uint8')
img_chn_red[:,:,0] = img_data[:,:,0]
img_red = Image.fromarray(img_chn_red)
img_red.show()


print("Hello World")

#richies music is really loud

#testing login credentials