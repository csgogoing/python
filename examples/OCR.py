import tesserocr
from PIL import Image





# with open('1.png', 'wb') as f:
# 	f.write(req_pic.content)
image=Image.open('1.png')
print(tesserocr.image_to_text(image))
print('verfy:%s'%verifyCode)
image = image.convert('L')
threashold = 80
table = []
for i in range(256):
	if i < threashold:
		table.append(0)
	else:
		table.append(1)
image_l = image.point(table, '1')
verifyCode = tesserocr.image_to_text(image_l).strip('\n\r\t')  
print('verfy2:%s'%verifyCode)
image.show()