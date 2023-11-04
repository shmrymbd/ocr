from multiprocessing import Pool
import pytesseract
import cv2
from PIL import Image

def perform_ocr_on_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img, lang='eng')
    return text

# Wrapper function to enable timeouts
def ocr_with_timeout(image_path, timeout=30):
    # Create a Pool of 1 worker
    with Pool(1) as pool:
        # Use apply_async to execute the OCR function with a timeout
        ocr_result = pool.apply_async(perform_ocr_on_image, (image_path,))
        try:
            # Get the result with the specified timeout
            text = ocr_result.get(timeout=timeout)
            return text
        except TimeoutError:
            print(f"OCR process timed out after {timeout} seconds.")
            return None

# Example usage
text_from_image = ocr_with_timeout('image.jpg', timeout=30)
if text_from_image:
    print(text_from_image)
