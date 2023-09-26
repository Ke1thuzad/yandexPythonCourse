from itertools import product


def solution(n: int):
    print("А Б В")
    print(
        "\n".join(
            " ".join(map(str, comb))
            for comb in product(range(1, n + 1), repeat=3)
            if sum(comb) == n
        )
    )


def main():
    n = int(input())
    solution(n)


if __name__ == "__main__":
    main()
