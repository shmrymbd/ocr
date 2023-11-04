import easyocr
reader = easyocr.Reader(['en'])  # Specify languages here
results = reader.readtext('image.jpg')
for result in results:
    print(result[1])  # Prints detected text
