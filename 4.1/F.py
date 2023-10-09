def modern_print(out: str):
    global cache
    if out not in cache:
        cache.add(out)
        print(out)


cache = set()