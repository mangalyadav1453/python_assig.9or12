from mathematics import Subtraction as s
from mathematics import Addition as a
from mathematics import Multiplication as m
from mathematics import Division as d
from mathematics import modulus as l
def write_to_file(operation, num1, num2, result):
    with open("calculation_history.txt", "a") as file:
file.write(f"{num1} {operation} {num2} = {result}\n")

num1 = int(input("Enter operand1: "))
num2 = int(input("Enter operand2: "))
print("1) Addition\n2) Subtraction\n3) Multiplication\n4) Division\n5) Modulus")
c = int(input("Enter the mode of calculation: "))

try:
if c == 1:
result = a.Addition(num1, num2)
operation = "+"
elif c == 2:
result = s.Subtracting(num1, num2)
operation = "-"
elif c == 3:
result = m.Multiplying(num1, num2)
operation = "*"
elif c == 4:
result = d.Dividing(num1, num2)
operation = "/"
elif c == 5:
result = l.Mod(num1, num2)
operation = "%"
else:
print("Please choose a correct option.")
exit()

print(f"Result: {result}")
write_to_file(operation, num1, num2, result)

except ZeroDivisionError:
print("Error: Cannot divide by zero.")
except ValueError:
print("Error: Invalid input. Please enter valid numbers.")
except Exception as e:
print(f"An error occurred: {e}")
