import base64
from PIL import Image

image = Image.open("OG.PNG")
image = image.resize((64,64),Image.ANTIALIAS)
image.save(fp="ICON.png")


with open("ICON.png", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
    print (str)
