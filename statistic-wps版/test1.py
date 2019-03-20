from PIL import Image

image = Image.open('14.jpg')
#使用ImageEnhance可以增强图片的识别率
#enhancer = ImageEnhance.Contrast(image)
#enhancer = enhancer.enhance(4)
image = image.convert('L')
ltext = ''
ltext= image_to_string(image, lang='eng')
#print ltext
print(ltext)