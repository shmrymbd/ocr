import pytesseract
from PIL import Image

# Specify the path to the tesseract executable if it's not in your PATH
# pytesseract.pytesseract.tesseract_cmd = '/path/to/tesseract'

# Function to perform OCR on an image
def ocr_on_bw_image(image_path):
    # Open the image
    img = Image.open(image_path)

    # Convert image to grayscale ('L') if it's not already in black and white
    if img.mode != 'L':
        img = img.convert('L')

    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(img, lang='eng')
    return text

# Example usage
# Replace 'path_to_bw_image.jpg' with the actual path to your black and white image file
extracted_text = ocr_on_bw_image('image.jpg')
print(extracted_text)
