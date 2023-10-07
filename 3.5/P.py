from sys import stdin


def solution(keyword: str, file_names: list[str]):
    found = 0
    for file in file_names:
        with open(file, encoding='UTF-8') as f:
            file_content = f.read().lower().replace('&nbsp;', ' ').split()
            print(file_content)
            if keyword in ' '.join(file_content):
                print(file)
                found += 1
    if not found:
        print('404. Not Found')


def main():
    user_input = []
    for ans in stdin:
        user_input.append(ans.rstrip('\n'))
    keyword = user_input.pop(0).lower().replace('&nbsp;', ' ').split()
    keyword = ' '.join(keyword)
    solution(keyword, user_input)


if __name__ == '__main__':
    main()
