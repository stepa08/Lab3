integer = int(input("Введите целое число:"))
decimal = float(input("Введите десятичную дробь:"))
string = input("Введите строку:")

print(f"Значение: {integer}, тип: {type(integer).__name__}")
print(f"Значение: {decimal}, тип: {type(decimal).__name__}")
print(f"Значение: {string}, тип: {type(string).__name__}")