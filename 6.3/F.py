import json
from requests import get


def get_users_name(url):
    response = get(f'http://{url}/users')
    data = json.loads(response.content)
    users = []
    for user in data:
        users.append(f'{user["last_name"]} {user["first_name"]}')
    print('\n'.join(sorted(users)))


def main():
    get_users_name(input())


if __name__ == '__main__':
    main()
