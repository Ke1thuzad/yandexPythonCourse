from sys import stdin


def solution():
    for code_str in stdin:
        formatted_code = code_str[:code_str.find('#')]
        if formatted_code:
            print(formatted_code)


def main():
    solution()


if __name__ == '__main__':
    main()
