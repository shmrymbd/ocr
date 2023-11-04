import argparse
from PIL import Image, ImageOps, ImageEnhance
import easyocr
import numpy as np

def invert_and_enhance_contrast(image_path):
    # Open the image using PIL
    with Image.open(image_path) as img:
        # Convert the image to grayscale if it's not already
        if img.mode != 'L':
            img = img.convert('L')

        # Invert the image (negative to positive)
        img = ImageOps.invert(img)

        # Enhance the contrast
#        enhancer = ImageEnhance.Contrast(img)
#        img = enhancer.enhance(2)  # Adjust the factor as needed to increase contrast

    return img

def perform_ocr(image):
    # Create an EasyOCR reader instance for English
    reader = easyocr.Reader(['en'])  # Add more languages if needed

    # Perform OCR using the reader
    return reader.readtext(np.array(image), paragraph=True)

def main():
    parser = argparse.ArgumentParser(description='Perform OCR on an inverted and contrast-enhanced X-ray image.')
    parser.add_argument('image_path', help='The path to the image file.')
    args = parser.parse_args()

    processed_image = invert_and_enhance_contrast(args.image_path)
    ocr_results = perform_ocr(processed_image)

    # Print the detected text
    for (bbox, text) in ocr_results:  # Removed the unpacking of 'prob' since it's not returned
        print(f'Detected text: {text}')

if __name__ == '__main__':
    main()
