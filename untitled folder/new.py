import pytesseract
from PIL import Image, ImageOps

# Make sure to set the path to the tesseract executable if it's not in the PATH
# pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'  # Path to tesseract on macOS

# Function to invert image colors
def invert_image(image_path):
    # Open the image
    img = Image.open(image_path)

    # Convert image mode to RGB if it's not already in RGB
    if img.mode != 'RGB':
        img = img.convert('RGB')

    # Invert image colors
    inverted_img = ImageOps.invert(img)
    return inverted_img

# Function to perform OCR on an inverted image
def ocr_on_inverted_image(image_path):
    # Invert the image colors
    img = invert_image(image_path)

    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(img)
    return text

# Example usage:
# Replace '/path/to/your/negative/image.jpg' with the actual path to your negative image
text_from_inverted_image = ocr_on_inverted_image('image.jpg')
print(text_from_inverted_image)
