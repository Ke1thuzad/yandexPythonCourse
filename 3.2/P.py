def solution():
    terrain = input()
    objects = set()
    while terrain != '':
        last = ''
        last_zaika = 0
        for obj in terrain.split():
            if last_zaika:
                objects.add(obj)
                last_zaika = 0
            if obj == 'зайка':
                if last != 'зайка':
                    objects.add(last)
                last_zaika = 1
            last = obj
        terrain = input()
    for out in objects:
        if out != '':
            print(out)


def main():
    solution()


if __name__ == '__main__':
    main()
