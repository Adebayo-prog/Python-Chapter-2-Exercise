age = int(input("Enter your age: "))

maximum_heart_rate = 220 - age
lower_target = maximum_heart_rate * 0.50
upper_target = maximum_heart_rate * 0.85

print("Maximum heart-rate: ", maximum_heart_rate)
print("Lower target heart-rate: ", lower_target)
print("Upper target heart-rate: ", upper_target)