from random import randint
import re


def generate_password(length, uppercase, numbers, symbols):
    chars = 'abcdefghijklmnopqrstuvwxyz'
    if uppercase:
        chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if numbers:
        chars += '0123456789'
    if symbols:
        chars += '!@#$%^&*()_+-=[]{}|;:,.<>?'

    password = ""
    for _ in range(length):
        password += chars[randint(0, len(chars)-1)]

    strength = 0
    if re.search(r'[A-Z]', password):
        strength += 20
    if re.search(r'[0-9]', password):
        strength += 20
    if re.search(r'[^A-Za-z0-9]', password):
        strength += 20
    if len(password) > 8:
        strength += 20
    if len(password) > 12:
        strength += 20
    
    return password, strength