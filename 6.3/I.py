import json
from requests import put
from sys import stdin


def change_user_data(url, user_id, user_data):
    json_encoded = json.dumps(user_data)
    response = put(f'http://{url}/users/{user_id}', json_encoded)


def main():
    url = stdin.readlines(1)[0].rstrip('\n')
    user_id = stdin.readlines(1)[0].rstrip('\n')
    user_data = {i.rstrip('\n').split('=')[0]: i.rstrip('\n').split('=')[1] for i in stdin.readlines()}
    change_user_data(url, user_id, user_data)


if __name__ == '__main__':
    main()
