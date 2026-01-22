
for i in range(1, 11):
    print(i, "square is", i * i)










text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)










marks = [45, 67, 89, 34, 56, 40]

for m in marks:
    if m > 50:
        print(m)









num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)













i = 1
while i <= 20:
    if i % 2 != 0:
        print(i)
    i += 1

















correct_password = "python123"
password = ""

while password != correct_password:
    password = input("Enter password: ")

print("Access Granted")















while True:
    data = input("Enter something: ")
    if data.lower() == "stop":
        break













n = int(input("Enter a number: "))
sum = 0

for i in range(1, n + 1):
    sum += i

print("Sum:", sum)


















numbers = [12, 45, 78, 34, 89]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number:", largest)














items = [10, 20, 30, 40, 50]

for item in items:
    print(item)














total = 0
count = 0

while True:
    num = int(input("Enter a number: "))
    if num < 0:
        break
    total += num
    count += 1

if count > 0:
    print("Average:", total / count)
else:
    print("No positive numbers entered")














num = int(input("Enter a number: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
