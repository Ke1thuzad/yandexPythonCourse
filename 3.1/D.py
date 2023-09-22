def solution(logs: list[str]):
    for log in logs:
        if '@@@' != log[-3:]:
            if '##' == log[:2]:
                log = log[2:]

            print(log)


def main():
    logs = []
    log = input()
    while log != '':
        logs.append(log)
        log = input()
    solution(logs)


if __name__ == '__main__':
    main()
