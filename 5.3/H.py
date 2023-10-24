class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def username_validation(username):
    if not isinstance(username, str):
        raise TypeError
    if any(not (ord(letter.lower()) in range(48, 58) or ord(letter.lower()) in range(95, 123)) for letter in username):
        raise BadCharacterError
    if ord(username[0]) in range(48, 58):
        raise StartsWithDigitError
    return username
