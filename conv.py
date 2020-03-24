import base64

try:
    myfile = open("text.txt","w")
    with open("Picture.jpg", "rb") as img_file:
        my_string = base64.b64encode(img_file.read())
    myfile.write(my_string.decode("utf-8"))

except Exception as e:
   print(str(e))

