def solution(land_amount: int):
    result = 0
    for i in range(land_amount):
        description = input()
        k = 0
        while description != 'ВСЁ':
            if description == 'зайка' and not k:
                result += 1
                k = 1
            description = input()
    print(result)


def main():
    land_amount = int(input())
    solution(land_amount)


if __name__ == '__main__':
    main()
