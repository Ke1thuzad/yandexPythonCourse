def solution(important_info: str, repeats: int):
    for i in range(repeats):
        print(important_info)


def main():
    important_info = input()
    repeats = int(input())
    solution(important_info, repeats)


if __name__ == '__main__':
    main()
