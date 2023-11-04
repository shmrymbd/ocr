import pytesseract
from PIL import Image, ImageOps

# If you have tesseract installed in a non-standard location, you might need to point pytesseract to it:
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
    
    # Save the inverted image if you need to use it later or to inspect it
    inverted_img.save('inverted_image.jpg')

    return inverted_img

# Function to perform OCR on an image
def ocr_on_image(image):
    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(image)
    return text

# Example usage
# Replace 'path_to_negative_image.jpg' with the actual path to your negative image file
inverted_img = invert_image_bw('2.jpg')
extracted_text = ocr_on_image(inverted_img)
print(extracted_text)
