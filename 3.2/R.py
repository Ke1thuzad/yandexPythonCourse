def solution(coords: list):
    coord_dict = {}
    for i in range(len(coords)):
        ind = (coords[i][0] // 10, coords[i][1] // 10)
        if ind in coord_dict:
            coord_dict[ind] += 1
        else:
            coord_dict[ind] = 1
    print(max(coord_dict.values()))


def main():
    n = int(input())
    coords = [tuple(map(int, input().split())) for _ in range(n)]

    solution(coords)


if __name__ == '__main__':
    main()
