
with open("ICON.png", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
    print (str)