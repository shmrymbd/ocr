import pytesseract
import argparse
import cv2
import numpy as np
from PIL import Image

# Function to preprocess the X-ray image for OCR
def preprocess_xray_image_for_ocr(filename):
    # Read the image using OpenCV
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

    # Invert the image if it's a negative image
    img = cv2.bitwise_not(img)

    # Apply adaptive thresholding to binarize the image
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 2)

    # Use morphological operations to separate characters
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

    # Resize the image to increase the resolution
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    return img

# Function to perform OCR on a preprocessed image and list alphabets
def list_alphabets_from_ocr(preprocessed_img):
    # Convert the OpenCV image to PIL format
    img_pil = Image.fromarray(preprocessed_img)

    # Perform OCR using Tesseract
    ocr_result = pytesseract.image_to_string(img_pil, lang='eng', config='--psm 6')

    # Filter out non-alphabet characters and make a set of unique alphabets
    alphabet_set = {char for char in ocr_result.upper() if char.isalpha()}

    # Convert set to a sorted list
    alphabet_list = sorted(list(alphabet_set))

    return alphabet_list

def main():
    parser = argparse.ArgumentParser(description='List all alphabet characters found in an X-ray image.')
    parser.add_argument('filename', help='The filename of the X-ray image.')
    args = parser.parse_args()

    try:
        preprocessed_img = preprocess_xray_image_for_ocr(args.filename)
        alphabets = list_alphabets_from_ocr(preprocessed_img)
        print('Alphabets found in the image:', alphabets)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
