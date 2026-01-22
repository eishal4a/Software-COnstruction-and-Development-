
students = {
    "Ali": 85,
    "Sara": 90,
    "Ahmed": 78
}

for key, value in students.items():
    print(key, ":", value)









students = {"Ali": 85, "Sara": 90}
students["Ayesha"] = 88
print(students)









students = {"Ali": 85, "Sara": 90}
print("Marks of Ali:", students["Ali"])










students = {"Ali": 85, "Sara": 90}
students["Ali"] = 95
print(students)










students = {"Ali": 85, "Sara": 90, "Ahmed": 78}

students.pop("Sara")
del students["Ahmed"]

print(students)










dict1 = {"A": 1, "B": 2}
dict2 = {"C": 3, "D": 4}

dict1.update(dict2)
print(dict1)














num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")









a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

largest = max(a, b, c)
print("Largest number:", largest)














total = float(input("Enter total amount: "))

if total >= 500:
    discount = total * 0.20
elif total >= 200:
    discount = total * 0.10
else:
    discount = 0

print("Discount:", discount)
print("Final Amount:", total - discount)











username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Login Failed")









password = input("Enter password: ")

if len(password) < 6:
    print("Weak")
elif len(password) < 10:
    print("Medium")
else:
    print("Strong")









speed = int(input("Enter speed: "))

if speed <= 60:
    print("No fine")
elif speed <= 80:
    print("Small fine")
else:
    print("Heavy fine")









price = float(input("Enter total price: "))

if price >= 1000:
    discount = price * 0.20
elif price >= 500:
    discount = price * 0.10
else:
    discount = 0

final_price = price - discount
print("Final Price:", final_price)







temp = float(input("Enter temperature: "))
humidity = float(input("Enter humidity: "))
wind = float(input("Enter wind speed: "))

if temp < 30 and humidity < 60 and wind < 20:
    print("Pleasant")
elif temp < 40 and humidity < 80:
    print("Normal")
else:
    print("Harsh")
