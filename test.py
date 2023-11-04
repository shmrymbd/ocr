import argparse
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
import easyocr
import numpy as np
import cv2

def invert_and_enhance_contrast(image_path):
    # Open the image using PIL
    with Image.open(image_path) as img:
        # Convert the image to grayscale if it's not already
        if img.mode != 'L':
            img = img.convert('L')

        # Invert the image (negative to positive)
        img = ImageOps.invert(img)
        # img = img.filter(ImageFilter.SHARPEN)
        img = gamma_correction (img, gamma=1.0)
        img = img.filter(ImageFilter.SHARPEN)

        # Enhance the contrast

#        enhancer = ImageEnhance.Contrast(img)
#        img = enhancer.enhance(2)  # Adjust the factor as needed to increase contrast

    return img

def gamma_correction(img, gamma=1.0):
    # Ensure the image is in 8-bit mode
    #img = img.convert('RGB')
    
    # Perform gamma correction
    gamma_table = [((i / 255.0) ** gamma) * 255 for i in range(256)]
    gamma_table = np.array(gamma_table).astype('uint8')
    img = Image.fromarray(gamma_table[img])

    return img

def linear_contrast_stretching(image):
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError("Image could not be read.")

    # Apply contrast stretching
    minmax_img = cv2.normalize(img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

    return minmax_img

def apply_clahe(image):
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError("Image could not be read.")

    # Create a CLAHE object
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    clahe_img = clahe.apply(img)

    return clahe_img

# def gamma_correction(image, gamma=1.0):
#     img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
#     if img is None:
#         raise ValueError("Image could not be read.")

#     # Build a lookup table mapping pixel values [0, 255] to adjusted gamma values
#     inv_gamma = 1.0 / gamma
#     table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")

#     # Apply gamma correction using the lookup table
#     gamma_img = cv2.LUT(img, table)

#     return gamma_img

def sharpen_image(image):
    with Image.open(image) as img:
        sharpened_img = img.filter(ImageFilter.SHARPEN)
    return sharpened_img

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
