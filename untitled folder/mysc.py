import argparse
from PIL import Image, ImageOps
import pytesseract

def perform_ocr(image_path, psm):
    # Open the image file
    with Image.open(image_path) as img:
        # Convert the image to grayscale
        img = img.convert('L')
        # Invert if it is a negative image
        img = ImageOps.invert(img)
        # Perform OCR using Tesseract
        text = pytesseract.image_to_string(img, lang='eng', config=f'--psm {psm}')
    return text

def main():
    parser = argparse.ArgumentParser(description='OCR on an image file.')
    parser.add_argument('image_path', help='Path to the image file')
    parser.add_argument('--psm', type=int, default=6, help='Tesseract page segmentation mode')
    args = parser.parse_args()

    text = perform_ocr(args.image_path, args.psm)
    print(text)

if __name__ == '__main__':
    main()
