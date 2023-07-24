import mathopr 


# Create an instance of MathOperations
class Invalidinput(Exception):
    def _init_(self,message):
        super()._init_(message)  
try:
    num1=int(input("enter num1: "))
    num2=int(input("enter num2: "))
except ValueError as error:
    raise Invalidinput("the provided values are invalid")  from error
opr=m.MathOperations


# Call member functions
print("Choose from below: ")
print("1) Addition\n2) Subtraction\n3) Trignometric")
n=int(input("Enter your choice: "))

if n==1:
    add = opr.add()
    print("Addition:", add)
    

elif n==2:
    sub = opr.subtract()
    print("Subtraction:", sub)
    

elif n==3:
    print("Choose from below: ")
    print("1) Sine\n2) Cosine ")
    if n==1:
        print("Sine: ",opr.sincalculate())
    if n==2:
        print("Cosine: ",)
    else:  
        print("Wrong Choice")

else:
    print("Invalid Choice")

    
# mul = opr.multiply()
# div = opr.divide()
# sqr = opr.square_root()

# print("Addition: ",add)
# print("subtraction: ",sub)
# print("Multiplication:", mul)
# print("Division:", div)
# print("Square Root:", sqr)


#mathopr file
import math 
class MathOperations:
    def _init_(self,num1=0,num2=0):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return(self.num1 + self.num2)
        
    def subtract(self):
        return(self.num1 - self.num2)
        
    def multiply(self):
        return(self.num1 * self.num2)
        
    def divide(self):
        if self.num2 != 0:
            return (self.num1 // self.num2)
        else:
            raise ZeroDivisionError("Cannot divide by zero!")
    def square_root(self):
        if self.num1 >= 0:
            return( math.sqrt(self.num1))
        else:
            raise ValueError("Cannot calculate square root of a negative number!")
    
    def sincalculate(self):
        return math.sin(self.num1) , math.sin(self.num2)
