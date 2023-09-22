def solution(orange_pieces: int):
    print('А Б В')
    for i in range(1, orange_pieces - 1):
        for j in range(1, orange_pieces - 1):
            for k in range(1, orange_pieces - 1):
                if i + j + k == orange_pieces:
                    print(i, j, k)


def main():
    orange_pieces = int(input())
    solution(orange_pieces)


if __name__ == '__main__':
    main()
