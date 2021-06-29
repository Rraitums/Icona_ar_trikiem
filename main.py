import PIL.Image as Image
import io
import base64
from ICON import byte_data


b = base64.b64decode(byte_data)
img = Image.open(io.BytesIO(b))
img.show()
#img.save("Final.png")