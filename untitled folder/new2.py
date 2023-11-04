import pytesseract
from PIL import Image, ImageOps, ImageFilter

# Set the path to the tesseract executable if it's not in the PATH
# pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'  # Path to tesseract on macOS

# Function to preprocess and invert image colors
def preprocess_and_invert_image(image_path):
    # Open the image
    img = Image.open(image_path)

    # Convert image to grayscale
    img = img.convert('L')

    # Apply image filters to enhance quality
    img = img.filter(ImageFilter.MedianFilter())  # Reduce noise
    img = ImageOps.autocontrast(img)  # Improve contrast

    # Invert image colors
    img = ImageOps.invert(img)

    # Further filters after inversion
    img = img.filter(ImageFilter.SHARPEN)

    return img

# Function to perform OCR on a preprocessed image
def ocr_on_preprocessed_image(image_path):
    # Preprocess and invert the image colors
    img = preprocess_and_invert_image(image_path)

    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(img)

    return text

# Example usage
# Replace 'path_to_negative_image.jpg' with the actual path to your negative image file
extracted_text = ocr_on_preprocessed_image('image.jpg')
print(extracted_text)
