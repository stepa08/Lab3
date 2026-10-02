# Выводим название программы
print("Конвертер температур")

# Выводим возможный выбор конвертера
print("1. из °C в °F")
print("2. из °F в °C")

# Запрашиваем у пользователя его выбор
choice = input("Ваш выбор (1/2): ")


if choice == "1":
    celsius = float(input("Введите температуру в °C: "))
    fahrenheit = celsius * 9 / 5 + 32
    print(f"{celsius:.1f}°C = {fahrenheit:.1f}°F")  # Выводим результат
elif choice == "2":
    fahrenheit = float(input("Введите температуру в °F: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit:.1f}°F = {celsius:.1f}°C")  # Выводим результат
else:
    print("Некорректный выбор")  # Выводим ошибку при неверном выборе
