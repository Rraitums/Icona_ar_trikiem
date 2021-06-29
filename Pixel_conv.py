"""from PIL import Image

def pixelate(input_file_path, pixel_size):
    image = Image.open(input_file_path)
    image = image.resize(
        (image.size[0] // pixel_size, image.size[1] // pixel_size),
        Image.NEAREST
    )
    image = image.resize(
        (image.size[0] * pixel_size, image.size[1] * pixel_size),
        Image.NEAREST
    )

    image.show()

pixelate("OG.PNG",16)"""

#!/usr/local/bin/python3
from PIL import Image

# Open Paddington
img = Image.open("OG.PNG")

# Resize smoothly down to 16x16 pixels
imgSmall = img.resize((120,120),resample=Image.BILINEAR)

# Scale back up using NEAREST to original size
result = imgSmall.resize(img.size,Image.NEAREST)

result.show()
# Save
#result.save('result.png')
