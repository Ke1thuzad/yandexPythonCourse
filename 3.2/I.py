def solution(objs: list[str]):
    obj_count = {}
    for object in objs:
        if object in obj_count:
            obj_count[object] += 1
        else:
            obj_count[object] = 1

    for o, val in obj_count.items():
        print(o, val)


def main():
    terrain = input()
    objs = []
    while terrain != '':
        objs += terrain.split()
        terrain = input()
    solution(objs)


if __name__ == '__main__':
    main()
