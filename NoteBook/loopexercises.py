# Exercise 1

# i = 0
# while True:
#     i += 1
#     print(i)
#     if i == 10:
#         break

# Exercise 2
for i in range(1,7):
    for j in range(1,i):
        print(j, end = " ")
    print("\n")

# Exercise 3
# entersandman = int(input("Enter a number."))
# sum = 0
# for i in range(1,entersandman+1):
#     sum += i
# print(sum)

# Exercise 4:
# Print multiplication table of given num:
# belly = int(input("Enter a number: "))
# for i in range (1, 11):
#     print(belly * i)

# Exercise 5:
# Number has to be divisible by 5
# If number is greater than 150, skip it.
# If the number is greater than 500, stop the loop

numbers = [12, 75, 150, 180 , 145, 525, 50]
for number in numbers:
    if number % 5 == 0 and number < 150:
        print(number)
    elif number > 150:
        continue
    elif number > 500:
        break
    # wrong order, but right idea

