x = 0 
while(x < 10):
	x += 1
print(x)

x,y = 0,0 
while(True):

		x += 1
		y += 2
		if(x+y > 10):
			break

# print everything in the list			
x = [1,2,7]
for i in x:
	print(i)

#print everything up to 30 (30 won't show)
for i in range(30):
	print(i)
	
# a range and in 2 increments:	
for i in range(10, 20, 2):
	print(i)

	# start loop over(on next value, if in for loop) skip anything that is not true
	
for i in range(30):
	if not(i % 3):
		continue
	print(i)
	
#try and except - prevent breaking (anything that requires user input)
# x = 5 + 'ham' will break
try:
	x = 5 + 'ham'
except:
	print("darn it")
	
try:
	x = 5 + 'ham'
except:
	print("darn it")
	
# pass is to ignore and move on, may be used in For, While or Try/Exception
try:
	x = 5 + 'ham'
except:
	pass
	
# raise - force an error to occur
raise TypeError("hahaha")

# Finally - last actions to perform following try/except. occurs before any real errors are returned.
try:
	x = 5 + 'ham'
except: ZD:
	print("will not see this")
finally:
	print("the final word")
	
#fibinacci Sequence [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
fiboSeq = []
a,b = 0,1
while(b < 1000):
	fibSeq.append(a)
	a,b = b, a + b
print(fiboSeq)

#prime [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
primes = []
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        98
for i in range(2, 100):
	for x in range(2,i):
		if (i % x == 0):			
		break
		else:
			primes.append(i)
		
	print(primes)

# 1 3 5 7 9	
for i in range(10):
	if(i%2):
		pass
	else:
		continue
	print(i)
	
#5, 6
for i in [[1,2,3],[4,5],[6,7]]:
	for j in i:
		if(4<j<=6):
			print(j)
			

	


    