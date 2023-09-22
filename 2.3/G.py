def solution(a: int, b: int):
    mx_factors = find_prime_factors(max(a, b))
    mn_factors = find_prime_factors(min(a, b))
    diff = find_differences_between_lists(mn_factors, mx_factors)
    mx_factors += diff

    result = 1

    for val in mx_factors:
        result *= val

    print(result)


def find_differences_between_lists(list1: list, list2: list):
    resulting_list = []
    for i in list1:
        if i not in list2 or (list1.count(i) - resulting_list.count(i)) > list2.count(i):
            resulting_list.append(i)
    return resulting_list


def find_prime_factors(x: int):
    factors = []
    for i in range(2, x + 1):
        while x % i == 0:
            factors.append(i)
            x //= i
    return factors


def main():
    a = int(input())
    b = int(input())
    solution(a, b)


if __name__ == '__main__':
    main()
