import pytesseract
import argparse
from PIL import Image, ImageEnhance

# Set up argument parsing
parser = argparse.ArgumentParser(description='Perform OCR on a black and white image.')
parser.add_argument('filename', help='The filename of the black and white image')
args = parser.parse_args()

# Function to enhance contrast and perform OCR on an image
def ocr_with_contrast_enhancement(filename):
    # Open the image
    img = Image.open(filename)
    
    # Convert image to grayscale ('L') if it's not already in black and white
    if img.mode != 'L':
        img = img.convert('L')

    # Enhance the contrast of the image
    enhancer = ImageEnhance.Contrast(img)
    img_enhanced = enhancer.enhance(2.0)  # Increase the contrast. Adjust the factor as needed.

    # Use Tesseract to do OCR on the contrast-enhanced image
    text = pytesseract.image_to_string(img_enhanced, lang='eng', config='--psm 6')

    return text

# Perform OCR using the provided filename with contrast enhancement
extracted_text = ocr_with_contrast_enhancement(args.filename)
print(extracted_text)
