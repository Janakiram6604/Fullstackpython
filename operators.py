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
pin = 1234
balance = 1000
entered_pin = int(input("Enter your PIN: "))
if entered_pin == pin:
    witdrawel_amount = float(input("Enter withdrawal amount: "))
    if witdrawel_amount <= balance:
        balance -= witdrawel_amount
        print("Withdrawal successful.")
    else:
        print("Insufficient balance.")
    print("Your balance is:", balance)
else:
    print("Incorrect PIN.")