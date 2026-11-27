import re
text = input("Введите вашу строку: \n").strip()
cleaned = re.sub(r"[^\w]", '', text.lower())
if cleaned == cleaned[::-1]:
    print("Ваша строка палиндром.")
else:
    print("Ваша строка не палиндром.")