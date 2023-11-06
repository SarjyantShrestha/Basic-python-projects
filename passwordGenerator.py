import secrets
import string


def uppercase_check(password: str):
    for char in password:
        if char.isupper():
            return True

    return False


def symbols_check(password: str):
    for char in password:
        if char in string.punctuation:
            return True

    return False


def password_generator(length: int, upperCase: bool, symbols: bool):
    combination: string = string.ascii_lowercase + string.digits

    if symbols:
        combination += string.punctuation

    if upperCase:
        combination += string.ascii_uppercase

    combination_length = len(combination)
    new_password: str = ''

    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]

    return new_password


if __name__ == '__main__':
  for i in range(1,4):
    new_pass: str = password_generator(length=10, symbols=False, upperCase=True)
    checks = f'U: {uppercase_check(new_pass)}, S: {symbols_check(new_pass)}'
    print(f'{i} -> {new_pass} ({checks})')
