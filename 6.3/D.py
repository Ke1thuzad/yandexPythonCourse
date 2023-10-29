import json
from requests import get


def sum_response_json_data(url, key):
    response = get(f'http://{url}')
    data = json.loads(response.content)
    if key in data:
        print(data[key])
    else:
        print('No data')


def main():
    url = input()
    key = input()
    sum_response_json_data(url, key)


if __name__ == '__main__':
    main()
