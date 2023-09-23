def solution(values: set):
    factors_to_values = []
    good_vals = {}
    for val in values:
        factors_to_values.append((val, frozenset(find_prime_factors(val))))
    for i in range(len(factors_to_values)):
        for j in range(len(factors_to_values)):
            if not factors_to_values[i][1].intersection(factors_to_values[j][1]):
                if factors_to_values[i][0] not in good_vals:
                    good_vals[factors_to_values[i][0]] = [factors_to_values[j][0]]
                else:
                    good_vals[factors_to_values[i][0]].append(factors_to_values[j][0])
    for value, factors in sorted(good_vals.items()):
        out = f'{value} - '
        for factor in sorted(factors):
            out += str(factor) + ', '
        print(out.strip(', '))


def find_prime_factors(x: int):
    factors = []
    for i in range(2, x + 1):
        while x % i == 0:
            factors.append(i)
            x //= i
    return factors


def main():
    values = set(map(int, input().split('; ')))
    solution(values)


if __name__ == '__main__':
    main()
