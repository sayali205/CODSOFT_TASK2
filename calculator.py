print("*..Simple Calculator..*")
def add(x,y):
	return x+y
def sub(x,y):
	return x-y
def mul(x,y):
	return x*y
def div(x,y):
	return x/y
print("Select Operation :")
print("1.Addition:")
print("2.Subtraction:")
print("3.Multiplication:")
print("4.Division:")
c=input("enter your choice=")
try:
	n1=float(input("Enter First Digit:"))
	n2=float(input("Enter First Digit:"))
	if c=='1':
		print("Result:",add(n1,n2))
	elif c=='2':
		print("Result:",sub(n1,n2))
	elif c=='3':
		print("Result:",mul(n1,n2))
	elif c=='4':
		print("Result:",div(n1,n2))
	else:
		print("Invalid Choice..")
except ValueError:
	print("Enter valid number..")