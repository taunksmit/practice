mylist  = [9,7,3,1,4,8,5,6]
# mylist  = [9]

if (len(mylist) == 1):
	min_ele = mylist[0]
	max_ele = mylist[0] 
	print ('max =',max_ele,'min =',min_ele)
	exit()

min_ele = mylist[0]
max_ele = mylist[1] 

if mylist[0] > mylist[1]:
	min_ele = mylist[1]
	max_ele = mylist[0] 

for ele in range(2, len(mylist)):
	# print (mylist[ele])
	if mylist[ele] < min_ele:
		min_ele = mylist[ele]
	if mylist[ele] > max_ele:
		max_ele = mylist[ele]
	else:
		pass 
print ('max =',max_ele,'min =',min_ele)
# print (min_ele)