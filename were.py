

from random import randint



majoy_s = []
majoy_round = []

a = raw_input('How to decide whos narrator?  1:alredy-picked      other:random :')
if a == '1':
	majoy = {1:'werewolf',2:'seer',3:'witch',4:'villager'}
	sorted(majoy)
else:
	majoy = {1:'werewolf',2:'seer',3:'witch',4:'villager',5:'narrotor'}
	sorted(majoy)

def randplayer(majoy_sb):
	majoy_roundr = []
	for i in range(0,person_number):
		randr = randint(0,person_number -1 -i)
		popi = majoy_sb.pop(randr)
		majoy_roundr.append(popi)
	return majoy_roundr
	

person_number = int(raw_input("please enter the number of person:"))
for  i in range(1,person_number+1):
	print(majoy)
	a = int(raw_input("the next majoy is :"))
	majoy_s.append(majoy[a])

print "so there are %s identities, they are:" % person_number
print majoy_s
print (10 * '\n')

majoy_round = randplayer(majoy_s)

playeridenty = {}
for  i in range(0,person_number):
	name = raw_input("put name and scrollup to see your identity\nthe next person is :")
	playeridenty[name] = majoy_round[i]
	print("your identify is %s") % majoy_round[i]
	print (50 * "\n")

print (5 * '\n')

while 1:
	show = raw_input("gameover please print'1':")
	if show == "1":
		for name in playeridenty:
			print("\nname:%s    ,identify:%s \n") % (name,playeridenty[name])
		break

print(8 * '\n')

over = raw_input("are you playing well?")
