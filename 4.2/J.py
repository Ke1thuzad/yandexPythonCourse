def secret_replace(encrypt: str, **encryption_pars: dict):
    encrypt: list = list(encrypt)
    used_indexes = {i: -1 for i in encryption_pars}
    for i in range(len(encrypt)):
        if encrypt[i] in encryption_pars:
            if encryption_pars[encrypt[i]]:
                used_indexes[encrypt[i]] = (used_indexes[encrypt[i]] + 1) % len(encryption_pars[encrypt[i]])
                encrypt[i] = encryption_pars[encrypt[i]][used_indexes[encrypt[i]]]
    return ''.join(encrypt)