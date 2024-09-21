import math
x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))
z = float(input("Введите значение z: ")) 

b = math.sqrt(10 * (3 * math.sqrt(x) + x**(2/5)) * (math.asin(z) - abs(x - y))**2)

print(f"Значение B: {b}")