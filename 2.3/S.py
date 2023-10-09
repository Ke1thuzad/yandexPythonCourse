def binary_search():
    start = 0
    end = 1001
    mid = (start + end) // 2
    print(mid)
    response = input()
    while response != 'Угадал!':
        if response == 'Меньше':
            end = mid
            mid = (start + end) // 2
        elif response == 'Больше':
            start = mid
            mid = (start + end) // 2
        print(mid)
        response = input()


def main():
    binary_search()


if __name__ == '__main__':
    main()
