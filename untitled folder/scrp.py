import argparse
from PIL import Image
import pytesseract
import cv2
from multiprocessing import Pool, TimeoutError
import os

# Function to preprocess the X-ray image for OCR
def preprocess_xray_image_for_ocr(image_path):
    # Read the image using OpenCV
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Invert the image if it's a negative image
    img = cv2.bitwise_not(img)

    # Apply adaptive thresholding to binarize the image
    img = cv2.adaptiveThreshold(
        img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 2
    )

    # Use morphological operations to separate characters
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

    # Resize the image to increase the resolution
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    return img

# Function to perform OCR on an image with a timeout
def perform_ocr_on_image(image_path, timeout_duration):
    try:
        pool = Pool(processes=1)
        result = pool.apply_async(pytesseract.image_to_string, (Image.open(image_path),))
        text = result.get(timeout=timeout_duration)  # Raises TimeoutError if it takes too long
        pool.close()
        pool.join()
        return text
    except TimeoutError:
        pool.terminate()
        print(f"OCR operation timed out after {timeout_duration} seconds.")
        return None

# Main function to handle command line arguments and run the OCR
def main():
    parser = argparse.ArgumentParser(description='Perform OCR on an image with text blocks.')
    parser.add_argument('image_path', help='The path to the image file you wish to OCR.')
    parser.add_argument('--timeout', help='The maximum time in seconds for the OCR operation to complete.', type=int, default=30)
    args = parser.parse_args()

    # Perform preprocessing on the image
    preprocessed_img_path = 'preprocessed.jpg'
    preprocessed_img = preprocess_xray_image_for_ocr(args.image_path)
    cv2.imwrite(preprocessed_img_path, preprocessed_img)

    # Perform OCR with a timeout
    extracted_text = perform_ocr_on_image(preprocessed_img_path, args.timeout)
    if extracted_text:
        print(extracted_text)

    # Cleanup preprocessed image file
    os.remove(preprocessed_img_path)

if __name__ == '__main__':
    main()
