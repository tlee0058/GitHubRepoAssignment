

def add(num1, num2):
	return num1 + num2
	
def min(num1, num2):
	return num1 - num2
	
def mul(num1, num2):
	return num1 * num2
	
def div(num1, num2):
	return num1 / num2
	try:
		return num1 / num2
	except ZeroDivisionError:
		print("Handled div by zero, Returning zero")
		return 0
		
#keep running unless it's invalid input

def runOperation(operation):
	""" Determines the operation to run based on the operation
	argument which should bve passed in as an int"""
	if (operation == 1):
		print("adding")
		print(add(num1, num2))
	elif(operation == 2):
		print("subtracting")
		print(sub(num1, num2))
	elif(operation ==3):
		print("multiplying")
		print(mul(num1, num2))
	elif(operation == 4):
		print("dividing")
		print(div(num1, num2))
	else:
		print("I don't understand")	
	
def main():
	user_continue = True
	while user_continue:
		validInput = False
		while not validInput:
			try:
				num1 = int(input("What is number 1"))
				num2 = int(input("what is number 2"))
				operation = int(input("What do you wnat to do? 1, 2, 3, 4"))
				validInput = True
			except ValueError:  # to prevent from cracking
				print("invalid input. The progress will now exit")
			except:
				print("Unknown error")
			runOperation(operation, num1, num2)
			
		user_yn = input("Would you like to run another calc?")
		if(user_yn != 'y'):
			user_continue = False
			break
		else:
			continue
			
if __name__== "_main_": # will only run the main fuction if we directly execute this file.
#Think of the _name_ variable as an indicator assigned by python for the purpose of
#determining if the "main" fuction should be run. Adding this line will enable use to import
#our calculator "module" so we can reuse its functionality.
	main()
	