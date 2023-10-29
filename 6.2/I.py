import pandas as pd


def solution(x1, y1, x2, y2):
    field = pd.read_csv('data.csv')
    return field[((field['x'] >= x1) & (field['x'] <= x2)) & ((field['y'] >= y2) & (field['y'] <= y1))]


def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    print(solution(x1, y1, x2, y2))


if __name__ == '__main__':
    main()
