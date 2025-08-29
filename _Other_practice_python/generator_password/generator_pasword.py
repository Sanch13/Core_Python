import string
from random import choices, choice


def get_random_password(min_length=8):
    if min_length < 8:
        raise ValueError(f"Длина пароля должна быть не менее {min_length} символов.")

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    all_characters = lower + upper + digits + special

    password = [
        choice(lower),
        choice(upper),
        choice(digits),
        choice(special)
    ]

    password.extend(choices(all_characters, k=min_length-4))

    return ''.join(password)


if __name__ == '__main__':
    for _ in range(10):
        print(get_random_password(12))
