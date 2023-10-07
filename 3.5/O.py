from sys import stdin
import json


def solution(user_answers: list):
    with open('scoring.json') as f:
        scoring_system = json.load(f)

    total_points = 0
    test_id = 0
    for test_group in scoring_system:
        points_per_test = test_group['points'] // len(test_group['tests'])
        for test in test_group['tests']:
            if test['pattern'] == user_answers[test_id]:
                total_points += points_per_test
            test_id += 1
    print(total_points)


def main():
    user_answers = []
    for ans in stdin:
        user_answers.append(ans.rstrip('\n'))
    solution(user_answers)


if __name__ == '__main__':
    main()
