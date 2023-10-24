import string
from hashlib import sha256


class MinLengthError(Exception):
    pass


class PossibleCharError(Exception):
    pass


class NeedCharError(Exception):
    pass


def password_validation(password,
                        min_length=8,
                        possible_chars=(string.ascii_letters + string.digits),
                        at_least_one=str.isdigit):
    if not isinstance(password, str):
        raise TypeError
    if len(password) < min_length:
        raise MinLengthError
    if any(letter not in possible_chars for letter in password):
        raise PossibleCharError
    if all(not at_least_one(i) for i in password):
        raise NeedCharError
    return sha256(password.encode('UTF-8')).hexdigest()
