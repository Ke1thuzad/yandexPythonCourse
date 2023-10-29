from requests import get


def sum_response_data(url):
    res = 0
    response = get(f'http://{url}')
    decoded_data = int(response.content.decode())
    while decoded_data != 0:
        res += decoded_data
        response = get(f'http://{url}')
        decoded_data = int(response.content.decode())
    print(res)


def main():
    sum_response_data(input())


if __name__ == '__main__':
    main()
