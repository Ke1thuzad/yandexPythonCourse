def solution(_keyword: str, reqs: list[str]):
    for request in reqs:
        if _keyword.lower() in request.lower():
            print(request)


def main():
    n = int(input())
    reqs = []
    for i in range(n):
        reqs.append(input())
    _keyword = input()
    solution(_keyword, reqs)


if __name__ == '__main__':
    main()
