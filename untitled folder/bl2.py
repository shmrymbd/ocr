import pytesseract
from PIL import Image, ImageOps

# Ensure pytesseract is pointing to the right path to tesseract executable if it's not in the PATH
# pytesseract.pytesseract.tesseract_cmd = '/path/to/tesseract'

# Function to invert a black and white image
def invert_image_bw(image_path):
    # Open the image
    img = Image.open(image_path)
    
    # Convert the image to grayscale ('L') if it's not already
    if img.mode != 'L':
        img = img.convert('L')
    
    # Invert the image using ImageOps
    inverted_img = ImageOps.invert(img)
    return inverted_img

# Function to perform OCR on an image
def ocr_on_image(image):
    # Use Tesseract to do OCR on the image with the specified language and page segmentation mode
    text = pytesseract.image_to_string(image, lang='eng', config='--psm 6')
    return text

# Example usage
# Replace 'path_to_negative_image.jpg' with the actual path to your negative image file
inverted_image = invert_image_bw('image.jpg')
extracted_text = ocr_on_image(inverted_image)
print(extracted_text)
