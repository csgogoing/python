from time import sleep, ctime
import threading

def super_player(file_, time):
	try:
		if time == 5:
			raise Exception('5')
		else:
			print('Start %s! %s!'%(file_, ctime()))
			sleep(time)
	except:
		print('555')

lists = {'3秒的歌':3, "5秒的歌":5, "4秒的歌":4}

threads = []
files = range(len(lists))
print(files)

for file_, time in lists.items():
	t  = threading.Thread(target=super_player, args=(file_, time))
	threads.append(t)

if __name__ == '__main__':
	for t in files:
		threads[t].start()
	for t in files:
		threads[t].join()

print('结束')