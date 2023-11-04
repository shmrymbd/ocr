import easyocr
import argparse

# Setup the command-line argument parser
parser = argparse.ArgumentParser(description='Perform OCR on an image using EasyOCR.')
parser.add_argument('image_path', help='Path to the image file on which to perform OCR.')
args = parser.parse_args()

# Create an EasyOCR reader instance for English
reader = easyocr.Reader(['en'])  # Add more languages if needed

# Use the reader to read text from the image specified in the command-line argument
results = reader.readtext(args.image_path)

# Print the detected text along with their confidence levels
for result in results:
    # Each result is a tuple containing the bounding box, text, and confidence
    bbox, text, prob = result
    print(f'Detected text: {text}\nConfidence level: {prob}')
