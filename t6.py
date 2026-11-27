import re

text = input("Введите текст: ")
# Очистка: буквы, цифры и пробелы
cleaned_text = re.sub(r'[^\w\s]', '', text)
print(cleaned_text)
# Ищем самое длинное слово
longest_word = max(cleaned_text.split(), key=len)

print(f"Самое длинное слово в тексте: {longest_word}")
