import json
from requests import get


def sum_response_json_data(url):
    res = 0
    response = get(f'http://{url}')
    data = json.loads(response.content)
    for i in data:
        if isinstance(i, int):
            res += i
    print(res)


def main():
    sum_response_json_data(input())


if __name__ == '__main__':
    main()
