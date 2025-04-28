# password_logic.py

import random
import string
from PySide6.QtCore import Qt

def generate_password(length, use_lower, use_upper, use_digits, use_symbols):
    # Если не выбран ни один из вариантов, генерируем пароль только из случайных букв
    if not any([use_lower, use_upper, use_digits, use_symbols]):
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

    # Определяем наборы символов для генерации пароля
    lowercase_letters = string.ascii_lowercase if use_lower else ''
    uppercase_letters = string.ascii_uppercase if use_upper else ''
    digits = string.digits if use_digits else ''
    symbols = string.punctuation if use_symbols else ''

    # Собираем все символы в один набор
    all_characters = lowercase_letters + uppercase_letters + digits + symbols

    # Генерируем пароль из заданной длины и набора символов
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password
