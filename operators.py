# product_price = 5000
# delivery_charge = 100
# total_price = product_price + delivery_charge
# print("Total Price:", total_price)




# #################
# a=10
# b=3
# print("Addition:", a + b)
# print("Subtraction:", a - b)
# print("Multiplication:", a * b)
# print("Division:", a / b)
# print("Floor Division:", a // b)
# print("Modulus:", a % b)
# print("Exponentiation:", a ** b)

# ################
# student = 10
# group = 2
# print("Number of Students per group:", student // group)

# ################
# followers = 100
# followers = followers -  1
# print("Number of Followers:", followers)

# saved_password = "ram123"
# enter_password = "ram123"
# print("Password Match:", saved_password == enter_password)


# balance = 500
# pin_correct = True
# if pin_correct and balance <= 1000:
#     print("Withdrawal Allowed")
# else:
#     print("Withdrawal not allowed.")




# #  simple bill calculator 1
# item1_price = 100
# item2_price = 200   
# item3_price = 50
# print("select items:")
# print("1. Item 1 - 100")
# print("2. Item 2 - 200")
# print("3. Item 3 - 50")
# selected_items = input("Enter the item numbers separated by commas (e.g., 1,2): ")
# selected_items_list = selected_items.split(",")
# total_price = 0

# for item in selected_items_list:
#     item = item.strip()

#     if item == "1":
#         quantity = int(input("Enter quantity for Item 1: "))
#         total_price += item1_price * quantity

#     elif item == "2":
#         quantity = int(input("Enter quantity for Item 2: "))
#         total_price += item2_price * quantity

#     elif item == "3":
#         quantity = int(input("Enter quantity for Item 3: "))
#         total_price += item3_price * quantity

#     else:
#         print("Invalid item:", item)

# print("Total Price:", total_price)


# ## simple bill calculator 2 
# total_price = 0

# while True:
#     item_name = input("Enter item name: ")
#     price = float(input("Enter price of {}: ".format(item_name)))
#     quantity = int(input("Enter quantity of {}: ".format(item_name)))

#     total_price += price * quantity

#     choice = input("Do you want to add another item? (yes/no): ").lower()
#     if choice != "yes":
#         break

# print("Total Price =", total_price)

####################

# password=input("Enter your password: ")
# if password=="ram123":
#     print("Access Granted")
# else:
#     print("Access Denied")

###############

# age = 20
# if age >= 18:
#     print("You are eligible to vote.")

# ####################
# marks =int(input("Enter your marks: "))
# if marks >= 90:
#     print("CGPA: 10")
# elif marks >= 80:
#     print("CGPA: 9.0")
# elif marks >= 70:
#     print("CGPA: 8.0")
# elif marks >= 60:
#     print("CGPA: 7.0")
# else:
#     print("CGPA: 6.0 OR below")

# ##############
# age = 25
# salary = 50000
# if age >= 18 and salary >= 30000:
#     print("Eligible for loan.")

# ##############
# day="Sunday"
# if day=="Sunday" or day=="Saturday":
#     print("Today is a holiday.")

# ###############
# login = True
# if not login:
#     print("Please log in to continue.")

####################
# pin = 1234
# balance = 1000
# entered_pin = int(input("Enter your PIN: "))
# if entered_pin == pin:
#     witdrawel_amount = float(input("Enter withdrawal amount: "))
#     if witdrawel_amount <= balance:
#         balance -= witdrawel_amount
#         print("Withdrawal successful.")
#     else:
#         print("Insufficient balance.")
#     print("Your balance is:", balance)
# else:
#     print("Incorrect PIN.")

###################
# for i in range(1, 6):
#     print(f"Sending mail {i}")

# ##################
# name = "dhoni"
# for char in name:
#     print(char)

# ######################
# count = 1
# while count <= 5:
#     print(f"Sending mail {count}")
#     count += 3

# #######################
# for i in range(10):
#     if i == 5:
#         break
#     print(f"Sending mail {i}")

# #########################
# student=["ram", "shyam", "hari", "gita"]
# student.append("sita")
# student.remove("shyam")
# print(student)

##################
# students={'ram', 'shyam', 'hari', 'gita'}
# print(students)
# num=[1, 2, 3, 4, 5, 6]
# print(num[-3])

###################
###data=(1, 2, 3, 4, 5)
##data[0]=10
#print(data)
# x=(1, 2,2,2, 3)
# print(x.count(2))

################
# X=('ram', 'shyam', 'hari', 'gita' , 'sita' , 'ram')
# print(X.count('ram'))

##############
# num=(1, 2, 3, 4, 5)
# print(num[1:4])  

################
#sets
#sets
# set is a collection of unique elements, meaning it does not allow duplicate values. Sets are unordered, which means that the items do not have a defined order, and they cannot be accessed by index. 
# x={1, 2, 3, 4, 5}
# print(x)

# #############
# a={1, 2, 3}
# b={3, 4, 5}
# print(a & b)  # intersection
# print(a | b)  # union
# print(a - b)  # difference
# print(a ^ b)  # symmetric difference

#####################
# def add(*numbers):
#     total =0
#     for i in numbers:
#         total += i
#     print("Sum of numbers:", total)
# add(10, 20, 30, 40)

################
# def squareroot(num):
#     return num ** 0.5
# print(squareroot(16))

##################
# def square(num):
#      return num ** 2
# print(square(6))

####################
# square=lambda x:x*x
# print(square(12))

#####################
# check_num = lambda x: "Even" if x % 2 == 0 else "Odd"
# print(check_num(7))   
# print(check_num(12))

######################
# to_upper = lambda x: x.upper()
# to_lower = lambda x: x.lower()

# print(to_upper("hello"))  
# print(to_lower("WORLD"))

#######################
# file = open("test.txt", "w")
# file.write("hello")
# file.close()
# print("file created successfully")

# file = open("test.txt", "r")
# data = file.read()
# print(data)
# file.close()

# file = open("test.txt", "a")
# file.write("\nworld")
# print("data appended successfully")
# file.close()

# file = open("test.txt", "r")
# print(file.read())
# file.close()

#####################
# try:
#     num = int(input("Enter a number: "))
#     print("You entered:", num)
# except ValueError:
#     print("only numbers are allowed")

# try:   
#     a=int(input("enter a number"))
#     b=int(input("enter a number"))
#     print(a/b)
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# except ValueError:
#     print("Error: Invalid input. Please enter a valid integer.")

try:
    file =open("non_existent_file.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("Error: The file does not exist.")
finally:
    print("File operation completed.")