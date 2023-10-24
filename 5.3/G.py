class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


def name_validation(name):
    if not isinstance(name, str):
        raise TypeError
    if any(not ord(letter.lower()) in range(1072, 1106) for letter in name):
        raise CyrillicError
    if name[0].islower() or any(letter.isupper() for letter in name[1:]):
        raise CapitalError
    return name