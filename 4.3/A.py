def recursive_sum(*vals):
    if not vals:
        return 0
    return vals[0] + recursive_sum(*vals[1:])