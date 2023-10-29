import json
from requests import post


def register_new_user(url, username, last_name, first_name, email_addr):
    json_encoded = json.dumps(
        {'username': username, 'last_name': last_name, 'first_name': first_name, 'email': email_addr}
    )
    response = post(f'http://{url}/users', json_encoded)


def main():
    url = input()
    username, last_name, first_name, email_addr = (input() for _ in range(4))
    register_new_user(url, username, last_name, first_name, email_addr)


if __name__ == '__main__':
    main()
