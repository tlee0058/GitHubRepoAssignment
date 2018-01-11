

def triangle():
    pass
    print("triangle(10)")
    num = 1
    
    while num < 10:
        print("*" * num)
        num = num + 1
        
triangle()


def is_palindrome(word):
    pass
	letters = list(word)
	is_palindrome = True
	
	for letter in letters:
		if letter == letters[-1]:
			letters.pop(-1)
		else:
			is_palindrome = False
			break
	return is_palindrome