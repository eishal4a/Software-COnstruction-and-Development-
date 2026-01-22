
def final_price(price, tax_percent):
    tax = price * (tax_percent / 100)
    return price + tax

price = float(input("Enter price: "))
tax = float(input("Enter tax percentage: "))

print("Final Price:", final_price(price, tax))










def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

number = int(input("Enter a number: "))
print("Factorial:", factorial(number))














def temperature_status(temp):
    if temp < 10:
        return "Cold"
    elif temp <= 25:
        return "Warm"
    else:
        return "Hot"

temp = float(input("Enter temperature in Celsius: "))
print("Weather:", temperature_status(temp))












def calculations(a, b):
    sum_value = a + b
    difference = a - b
    product = a * b
    return sum_value, difference, product

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

result = calculations(x, y)
print("Sum:", result[0])
print("Difference:", result[1])
print("Product:", result[2])














def list_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

my_list = [10, 20, 30, 40, 50]
print("Sum of list:", list_sum(my_list))
