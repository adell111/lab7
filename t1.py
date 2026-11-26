import re

text = input("Введите текст: ")
words = re.findall(r"\b\w+\b",text)
print(f"Количество слов: {len(words)}")