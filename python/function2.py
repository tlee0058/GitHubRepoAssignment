def doesNothing():
	pass
	
doesNothing()

# return is a way to output or return data from a function

def makeOne():
	return 1
	
	x = makeOne()
print(x)
	
# arguments is a way to input or pass in data to a function - inputs(argument) output (return)
# 2 types of arguments 1) regular is like var1; 2) Keyword is var2 = 3 - set default value that may be overriden)

def addTen(myInt):
	myInt += 10
	return myInt
x = 10	
y = addTen(x)
print(x, y)

# doc string is like a cover of the manual and comments are contents or to hide error

def myFunc():
	'''
	I documented something
	'''
	#Only seen in code view, ignored
	pass

print(myFunc.__doc__)



def myAdd(var1, var2 = 10):
	return var1 + var2
print(myAdd(7))
print(myAdd(8,5)) # 5 can be overriden