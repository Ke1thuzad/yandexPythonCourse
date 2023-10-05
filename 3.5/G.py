def solution(nums: list):
    stats = [len(nums), len([i for i in nums if i > 0]), min(nums), max(nums), sum(nums), f'{sum(nums) / len(nums):.2f}']
    print(*stats, sep='\n')


def main():
    file_title = input()
    with open(file_title) as f:
        nums = f.read().replace('\n', ' ').split()
    solution(list(map(int, nums)))


if __name__ == '__main__':
    main()
