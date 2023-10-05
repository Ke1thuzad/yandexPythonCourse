from sys import stdin


def solution(reqs: list, keyword: str):
    for req in reqs:
        if keyword in req.lower():
            print(req)


def main():
    reqs = []
    for inp in stdin:
        reqs.append(inp.rstrip('\n'))
    keyword = reqs.pop(-1)
    solution(reqs, keyword.lower())


if __name__ == '__main__':
    main()
