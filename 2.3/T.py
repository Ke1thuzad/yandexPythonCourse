def solution(n: int):
    last_hash = 0
    for i in range(n):
        block = int(input())
        for m in range(1000):
            k = 0
            for random in range(256):
                hash_n = (37 * (m + random + last_hash)) % 256
                if hash_n < 100 and block == (m * 256 * 256 + random * 256 + hash_n):
                    last_hash = hash_n
                    k = 1
                    break
            if k:
                break
        else:
            print(i)
            return 0
    else:
        print(-1)


def main():
    n = int(input())
    solution(n)


if __name__ == '__main__':
    main()
