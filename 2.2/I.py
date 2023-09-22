def solution(people: list):
    print(sorted(people)[0])


def main():
    people = []
    for _ in range(3):
        people.append(input())
    solution(people)


if __name__ == '__main__':
    main()
