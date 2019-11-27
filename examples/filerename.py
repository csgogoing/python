import os



excel_path = os.getcwd() + '\\'
print(excel_path)
for i in range(10):
	tmp = '%d.'%i
	print(tmp)
	for filename in os.listdir():
		if tmp in filename:
			oldname = excel_path + filename
			new_file = filename.split('.')
			newname = excel_path + new_file[1]
			try:
				os.rename(oldname,newname)
				print(newname)
			except FileExistsError as e:
				os.remove(oldname)
				print('del')
			else:
				pass


# excel_path = os.getcwd() + '\\'
# print(excel_path)
# for i in range(10,60):
# 	tmp = '%d  '%i
# 	print(tmp)
# 	for filename in os.listdir():
# 		if tmp in filename:
# 			oldname = excel_path + filename
# 			new_file = filename[4:]
# 			print(new_file)
# 			newname = excel_path + new_file
# 			try:
# 				os.rename(oldname,newname)
# 				print(newname)
# 			except FileExistsError as e:
# 				os.remove(oldname)
# 				print('del')
# 			else:
# 				pass

