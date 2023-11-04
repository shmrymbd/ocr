import argparse
from PIL import Image, ImageOps
import pytesseract

# Function to invert image colors
def invert_image(image):
    # Invert the colors using ImageOps
    return ImageOps.invert(image)

# Function to perform OCR on an image
def ocr_on_image(image_path):
    # Open the image using PIL
    img = Image.open(image_path)
    
    # Convert image to grayscale ('L') if it's not already
    if img.mode != 'L':
        img = img.convert('L')
    
    # Invert image colors if it's a negative
    img = invert_image(img)

    # Perform OCR using Tesseract
    text = pytesseract.image_to_string(img, lang='eng', config='--psm 12')
    return text

# Main function to handle command line arguments and execute the OCR
def main():
    parser = argparse.ArgumentParser(description='Perform OCR on an image.')
    parser.add_argument('image_path', help='The path to the image file.')
    args = parser.parse_args()

    # Perform OCR on the image and print the results
    text = ocr_on_image(args.image_path)
    print(text)

if __name__ == '__main__':
    main()
