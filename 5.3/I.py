class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


def username_validation(username):
    if not isinstance(username, str):
        raise TypeError
    if any(not (ord(letter.lower()) in range(48, 58) or ord(letter.lower()) in range(95, 123)) for letter in username):
        raise BadCharacterError
    if ord(username[0]) in range(48, 58):
        raise StartsWithDigitError
    return username


def name_validation(name):
    if not isinstance(name, str):
        raise TypeError
    if any(not ord(letter.lower()) in range(1072, 1106) for letter in name):
        raise CyrillicError
    if name[0].islower() or any(letter.isupper() for letter in name[1:]):
        raise CapitalError
    return name


def user_validation(**kwargs):
    if sorted(kwargs.keys()) != sorted(('last_name', 'first_name', 'username')):
        raise KeyError
    if not all(isinstance(i, str) for i in kwargs.keys()):
        raise TypeError
    name_validation(kwargs['last_name'])
    name_validation(kwargs['first_name'])
    username_validation(kwargs['username'])
    return kwargs


print(user_validation(last_name="Иванов", first_name="Иван", username="ivanych45", password="123456"))
