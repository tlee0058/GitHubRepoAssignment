def add(num1, num2):
	return num1 + num2
	
def sub(num1, num2):
	return num1 - num2
	
def mul(num1, num2):
	return num1 * num2
	
def div(num1, num2):
	return num1 / num2
	
def runOperation(operations):
	if(operation == 1):
	print(add(num1, num2))
	
	elif(operation == 2):
	print(sub(num1, num2))
	
	elif(operation == 3):
	print(mul(num1, num2))
	
	elif(operation == 4):
	print(div(num1, num2))
	
	else:
	print("I don't understand")
	
def main():
	user_continue = True
	while user_continue:
		validInput = False
		while not validInput:
			try:
				num1 = int(input("Enter number 1: ")
				num2 = int(input("Enter number 2: ")
				operation = int(input("What would you like to do?")
				validInput = True
			except ValueError:
				print("I don't know how")
			except:
				print("Unknown error")
			run Operation(operations, num1, num2)
			
		user_yn = input('would you like to do another one?")
		if(user_yn != 'y'):
			user_continue = False
			break
		else:
			continue
			
main()
		
				
	
	
			

		
		
	
	





	