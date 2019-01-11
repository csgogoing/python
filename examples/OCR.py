import tesserocr
from PIL import Image

image=Image.open('image.jpg')
print(tesserocr.image_to_text(image))