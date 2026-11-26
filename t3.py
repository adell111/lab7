def cesar_shiefr(text: str, shift: int) -> str:
    '''Шифрует русский текст шифром Цезаря'''
    '''
    В таблице Unicode русские буквы стоят по порядку от 1072 до 1103 для сторчных (кроме буквы ё - 1105)
    и от 1040 до 1071 для заглавных (кроме буквы Ё - 1025)    
    '''
    lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    upper = lower.upper()
    result = []
    for ch in text:
        if ch in lower:
            i = lower.index(ch)
            result.append(lower[(i + shift) % len(lower)])
        elif ch in upper:
            i = upper.index(ch)
            result.append(upper[(i + shift) % len(upper)])
        else:
            result.append(ch)

    return "".join(result)
shift = int(input("Впишите число, на которое нужно сдвинуть алфавит: "))
original = input("Введите текст для шфирования: \n")
crypted = cesar_shiefr(original,shift)
print(f"Оригинал: {original}")
print(f"Зашифрованный текст: {crypted}")

# Дешифрование
print(cesar_shiefr(crypted,-(shift)))