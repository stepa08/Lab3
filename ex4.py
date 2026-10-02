# Вводим строку
text = input("Введите строку: ")

# Выводим операцию и её значение
print(f"Длинна: {len(text)}")
print(f"Верхний регистр: {text.upper()}")
print(f"Нижний регистр: {text.lower()}")
print(f"Первый символ: {text[0]}")
print(f"Последний символ: {text[-1]}")
print(f"Количество пробелов: {text.count(' ')}")
