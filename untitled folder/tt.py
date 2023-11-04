import argparse
from PIL import Image
import pytesseract
import cv2
import os
from collections import Counter

# Function to preprocess the image for OCR
def preprocess_image(image_path):
    # Read the image using OpenCV
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply any necessary preprocessing steps
    # Invert the image if it's a negative image
    img = cv2.bitwise_not(img)

    # Apply adaptive thresholding to binarize the image
    img = cv2.adaptiveThreshold(
        img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 2
    )

    return img

# Function to extract and return a sorted list of unique alphabetic characters
def extract_alphabets_from_image(image_path):
    preprocessed_img = preprocess_image(image_path)

    # Perform OCR using Tesseract
    text = pytesseract.image_to_string(preprocessed_img, lang='eng', config='--psm 6')

    # Filter out non-alphabetic characters and create a set of unique characters
    alphabets = [char.upper() for char in text if char.isalpha()]

    # Return a sorted list of unique alphabetic characters
    return sorted(set(alphabets))

# Main function to handle command line arguments and execute the script
def main():
    parser = argparse.ArgumentParser(description='Extract and list unique alphabetic characters from an image.')
    parser.add_argument('image_path', help='The path to the image file.')
    args = parser.parse_args()

    # Extract and print the list of alphabetic characters
    alphabets = extract_alphabets_from_image(args.image_path)
    print("Unique alphabetic characters found in the image:")
    print(alphabets)

if __name__ == '__main__':
    main()
