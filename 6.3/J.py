from requests import delete


def delete_user(url, user_id):
    delete(f'http://{url}/users/{user_id}')


def main():
    url = input()
    user_id = input()
    delete_user(url, user_id)


if __name__ == '__main__':
    main()
