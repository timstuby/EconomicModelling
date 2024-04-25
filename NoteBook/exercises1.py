#Exercise 1
import random

number1 = random.randint(1,100)
number2 = random.randint(1,100)

if number1 * number2 <= 1000:
    print(f"{number1} * {number2} = {number1*number2}")
else:
    print(f"{number1} + {number2} = {number1 + number2}")

#Exercise 2
for i in range(0, 10):
    print(f"Current Number: {i}, Previous number: {i-1}. Sum: {i + i-1}")

#Exercise 3
# strinput = input("Enter a word.")
# print(strinput[::2])

#Exercise 4
def remove_chars(word, n):
    print('Original string:', word)
    x = word[n:]
    return x
print("Removing characters from a string.")
print(remove_chars("Alphanumerical",3))

#Exercise 5
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
def comparenums(zulu):
    print(f"Given list is {zulu}")
    if zulu[0] == zulu[-1]:
        print("Result is true")
    else:
        print("Result is false")
comparenums(numbers_x)
comparenums(numbers_y)

#Index example:
my_list = [_ for _ in 'abcdefghijklmnop']
print(my_list)
#Slicing, just use :
#E.g
print(my_list[-5:-2])
#Stepping, use ::
print(my_list[2::2])

#Exercise 6:
sixlist = [10,20,33,46,55,88,291,1000]
for num in sixlist:
    if num % 5 == 0:
        print(f"{num} is divisible by 5")

# Note on using modulo (the %).
# Works as a division, and returns the
# remainder that could not be part of the divison.
# e.g: 10 % 3 returns 1. 5%5 returns 0.

# Exercise 7:
str_x = "Emma is a good developer. Emma hates insects."
print(f"Emma appears {str_x.count('Emma')} times")

#Exercise 8
for num in range(10):
    for i in range(num):
        print(num, end=" ") #print number
    # new line after each row to display pattern correctly
    print("\n")

#Exercise 9
def palinumber(bravo):
    bravo = str(bravo)
    if bravo == bravo[::-1]:
        print("Given number is palindrome number.")
    else:
        print("Given number not palindrome.")
palinumber(88948)
palinumber(121)


# Exercise 10
# List that contains odd numbers from first list
# And even numbers from second list

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
result1 = []
for num in list1:
    if num % 2 != 0:
        result1.append(num)

for num in list2:
    if num % 2 == 0:
        result1.append(num)

print(result1)

#Exercise 11
goofball = random.randint(1, 1000)
print(f"Original number is {goofball}")
goofball = str(goofball)
goofball = goofball[::-1]
listgoof = [_ for _ in goofball]
print(listgoof)

#Real solution:
number = 7428
print("Given number", number)
while number > 0:
    digit = number % 10
    number = number // 10
    print(digit, end=" ")

# Exercise 12
# Tax bracket

income = random.randint(1,500000)
def taxesowed(income):
    if income > 10000:
        leftoverT1 = income - 10000
        if leftoverT1 > 0 and leftoverT1 < 10000:
            due = leftoverT1 * 0.1
        elif leftoverT1 >= 10000:
            leftoverT2 = leftoverT1 - 10000
            due = 10000 * 0.1
            due += leftoverT2 * 0.2
    print(f"Income is {income}, so taxes owed is {due}")

taxesowed(income)


# Exercise 13:
# print multiplication table from 1 to 10
for i in range(1,11):
    print(i, end = "   ")
    for j in range(2,11):
        print(i * j, end = " ")
    print("\n")

# Exercise 14:
for i in range(6, 0, -1):
    for j in range(0 , i - 1):
        print("*", end = ' ')
    print(" ")

