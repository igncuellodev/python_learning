
base_number = int(input("Write the base, you want to power:\n"))
exponent_number = int(input("Write the exponent and press enter to see the result:\n"))
exponencial = base_number**exponent_number

print("The result of the operation is = " + str(exponencial))
import random
user_number = int(input("Write a number to generate other 3 random numbers:\n"))
num1 = random.randint(1,user_number)
num2 = random.randint(1,user_number)
num3 = random.randint(1,user_number)


print(num1)
print(num2)
print(num3)




kid_01 = int(input("Write the age of the first kid:\n"))
kid_02 = int(input("Write the age of the second kid:\n"))

if kid_01 < kid_02 and kid_02 - kid_01 >= 3:
    print("niño 02 es mucho mayor que niño 01")

elif kid_01 < kid_02 and kid_02 - kid_01 < 3:
    print("niño 02 es algo mayor que niño 01")

if kid_02 < kid_01 and kid_01 - kid_02 >= 3:
    print("niño 01 es mucho mayor que niño 02")

else:
    print("niño 01 es algo mayor que niño 02")




savings_goal = float(input("How much money do you want to save?:\n"))
user_today = float(input("Write how much money you saved today?:\n"))
user_savings = user_today
days = 1

while user_savings < savings_goal:
    print("Your goal: " + str(savings_goal) + " dollars")
    print("You have: " + str(user_savings) + " dollars")
    print("In " + str(days) + " days")
    user_today = float(input("Write how much money you saved today?:\n"))
    user_savings = user_savings + user_today
    days = days + 1


if user_savings >= savings_goal:
    print("You achieved, your saving goal: " + str(savings_goal) + " dollars " + "in " + str(days) + " days.") 
    print("You have a total of " + str(user_savings))

