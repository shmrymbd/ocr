from PIL import ImageFilter
from PIL import Image, ImageOps, ImageEnhance

def sharpen_image(image_path):
    with Image.open(image_path) as img:
        sharpened_img = img.filter(ImageFilter.SHARPEN)
    return sharpened_img

sharpen_image('image.jpg')
