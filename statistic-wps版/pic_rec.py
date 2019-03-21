import cv2
import aircv as ac
import os
from fnmatch import fnmatch

def draw_circle(img, pos, circle_radius, color, line_width):
	cv2.circle(img, pos, circle_radius, color, line_width)
	cv2.imshow('objDetect', imsrc)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


def recognition(image_byte, num):
	#识别验证码
	with open('logincapture.bmp','wb') as f:
		f.write(image_byte)
		f.close()
	imsrc = ac.imread('logincapture.bmp')
	#imsrc = ac.imread(image_byte)
	most_confidence = []
	#根据模板内容，取出最自信的n个字符
	filedir = './template'
	for file in os.listdir(filedir):
		if fnmatch(file, '*.jpg'):
			imobj = ac.imread('./template/'+file)
			# find the match position
			pos = ac.find_template(imsrc, imobj)
			try:
				most_confidence.append((pos['confidence'],pos['result'][0],file))
			except TypeError:
				pass
	#排序后输出结果
	most_confidence.sort(reverse=True)
	target = most_confidence[0:num]
	target.sort(key=lambda x:x[1])
	result = ''
	for i in range(len(target)):
		result = result + target[i][2].strip('.')[0]
	print(result)
	return(result)


if __name__ == "__main__":
	recognition('a.bmp')