import json


def solution(nums: list, json_title: str):
    stats = {
        'count': len(nums),
        'positive_count': len([i for i in nums if i > 0]),
        'min': min(nums),
        'max': max(nums),
        'sum': sum(nums),
        'average': float(f'{sum(nums) / len(nums):.2f}'),
    }
    with open(json_title, 'w', encoding='UTF-8') as json_f:
        json.dump(stats, json_f, indent=2)


def main():
    file_title = input()
    json_title = input()
    with open(file_title) as f:
        nums = f.read().replace('\n', ' ').split()
    solution(list(map(int, nums)), json_title)


if __name__ == '__main__':
    main()
