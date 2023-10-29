import json
from requests import get
from sys import stdin


def collect_data(url, paths):
    all_data = 0
    for path in paths:
        response = get(f'http://{url + path}')
        all_data += sum(json.loads(response.content))
    print(all_data)


def main():
    paths = []
    for data in stdin:
        paths.append(data.rstrip('\n'))
    url = paths.pop(0)
    collect_data(url, paths)


if __name__ == '__main__':
    main()
