students = [
    ("Иван", 25, 4.5),
    ("Мария", 22, 4.85),
    ("Пётр", 30, 4.2),
    ("Анна", 20, 4.95),
]

# Заголовок
print(f"{"Имя":<10} {"Возраст":>8} {"Балл":>8}" )
print('-' * 31)

# Данные
for name, age, score in students:
    print(f"{name:<10}| {age:<8}| {score:<8.2f}|" )
print('-' * 31)
# Итог
avg = sum(s[2] for s in students) / len(students)
print(f"{'Средний балл': <10} {'':>8} {avg:<8.2f}")