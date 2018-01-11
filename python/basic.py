x = 'ham'
print (x)

y = x + "book"
print (y)

# with space

y = x + " book"
print (y)

z = 10

y = x + str(z)
print (y)

# replace something in d(integer) or f (float)

y = "something %d" %z
print (y)

y = "something %f" %z
print (y) 

#shorten the decimal

y = "Something %.3f" %z 
print (y)

# add lines in between

x = "te\n\nst"
print (x) 

# add tabs in between words

x = "test\t\ttest"
print (x)

# use in to see if something is in something bigger
x = "ham" in "hamsandwich"
print(x)

# do a list
x = ["ham", 4, 2.2]
print(x)

# add something in the list
x.append(5)
print(x)

# insert something within the list (let's say insert 7 in the 2nd place (0 = first; 1 = second etc)
x.insert(1, 7)
print(x)

# opposite(remove something in the list - 7
x.pop(1)
print(x)

#checking for a length of a list - 5 below
x = len("words")
print(x)

#tuples is like list but you can't make adjustment:
x = ("ham", 4, 5)
print(x) 

#dictionary : attribute and character
sam = {}
sam["weapon"] = "chainsaw"
sam["health"] = 10

print(sam)

#another way of dictionary

sam = {
	"weapon" : "chainsaw",
	"age" : 29
	
}
print(sam)



#delete one of the dictionary items
sam = {}
sam["weapon"] = "chainsaw"
sam["health"] = 10

del sam["health"]
print(sam)

a = str(int(2.23) + float(14)) + "tomatoes"
print(a)

i = "ham Ham".upper()
print(i)

t = "SUPER Baby".lower()

b = "I am ham"
	b.split() # separte by space
	b.split("m") #take out all the m
	b.join(a) #put b inside of a
	
x = "int: %d, float %.5f" %(14.4, 55.2)
print(x)

L = [1,6,7,26,8,3,4,5]
L[:] #duplicate the list
L[:2] #output is [1,6] - printing the first 2 numbers
L[2:] #output is [7,26,8,3,4,5] - print 
L[::2] # [1,7,8,4]
L[1::2] #[6,26,3,5]

	







