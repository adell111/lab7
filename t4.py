import re

def validate_email(email: str) -> bool:
    """Проверяет корректность email."""
    pattern = r'^[\w.+-]+@[\w-]+\.[\w.-]+$'
    return bool(re.match(pattern, email))


def validate_phone(phone: str) -> bool:
    """Проверяет корректность российского телефона."""
    pattern = r'^\+?7[\s-]?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}$'
    return bool(re.match(pattern, phone))


def validate_url(url: str) -> bool:
    """Проверяет корректность URL."""
    pattern = r'^https?://[\w.-]+\.[a-z]{2,}(/[\w./-]*)?$'
    return bool(re.match(pattern, url))

# Тесты
tests = [
    ("email", "anna.petrova+work@company.ru", validate_email),
    ("email","sergey.polok@gaml..ru",validate_email),
    ("email", "anna@company", validate_email),
    ("email", "@company.ru", validate_email),
    ("phone", "7-912-345-67-89", validate_phone),
    ("phone", "+7 912 345 67 89", validate_phone),
    ("phone", "+7 (123 30 8479 1",validate_phone),
    ("phone", "89123456789", validate_phone),
    ("url", "http://my-site.org", validate_url),
    ("url", "ftp://my-site.org", validate_url),
    ("url", "my-site.org", validate_url),
]

for type_, value, validator in tests:
    status = "[OK]" if validator(value) else "[FAIL]"
    print(f"{status:<6} | {type_.upper():<5} | {value}")