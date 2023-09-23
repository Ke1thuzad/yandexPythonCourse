def solution(n: int):
    public_property = set()
    a = input()
    kids_property = set(a[a.find(':') + 2:].split(', '))
    all_property = kids_property
    for i in range(n - 1):
        a = input()
        kids_property = set(a[a.find(':') + 2:].split(', '))
        public_property.update(all_property.intersection(kids_property))
        all_property.update(kids_property)
    print(*sorted(all_property.symmetric_difference(public_property)), sep='\n')


def main():
    n = int(input())
    solution(n)


if __name__ == '__main__':
    main()
