number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

sum = number1 + number2 + number3
average = sum/3

product = number1 * number2 * number3

smallest = min(number1, number2, number3)
largest = max(number1, number2, number3)

print("Sum: ", sum)
print("Average: ", average)
print("Product: ", product)
print("Smallest: ", smallest)
print("Largest: ", largest)