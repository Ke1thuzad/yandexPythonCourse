import json
from requests import get
from sys import stdin


def send_email_by_id(url, user_id, email_text):
    response = get(f'http://{url}/users/{user_id}')
    if response.status_code == 200:
        data = json.loads(response.content)
        print(eval('f"""' + email_text + '"""', data))
    else:
        print('Пользователь не найден')


def main():
    url = stdin.readlines(1)[0].rstrip('\n')
    user_id = stdin.readlines(1)[0].rstrip('\n')
    email_text = stdin.read()
    send_email_by_id(url, user_id, email_text)


if __name__ == '__main__':
    main()
