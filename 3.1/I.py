def solution(code: list[str]):
    for block in code:
        if '#' in block:
            res = block[:block.find('#')]
            if res:
                print(res)
        else:
            print(block)


def main():
    code = []
    block = input()
    while block != '':
        code.append(block)
        block = input()
    solution(code)


if __name__ == '__main__':
    main()
