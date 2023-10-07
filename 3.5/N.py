import json
from copy import deepcopy


def solution(input_file_name: str, changes_file_name: str):
    result = {}
    with open(input_file_name, encoding='UTF-8') as f:
        initial_json = json.load(f)
    with open(changes_file_name, encoding='UTF-8') as f:
        changes_json = json.load(f)
    users: list[dict] = deepcopy(initial_json)
    for i in range(len(users)):
        for change in changes_json:
            if change['name'] == users[i]['name']:
                users[i].update(change)
                for key, val in users[i].items():
                    if key == 'name':
                        result[val] = {}
                    else:
                        try:
                            if val > initial_json[i][key]:
                                result[users[i]['name']][key] = val
                            else:
                                result[users[i]['name']][key] = initial_json[i][key]
                        except KeyError:
                            result[users[i]['name']][key] = val
                break
        else:
            for key, val in users[i].items():
                if key == 'name':
                    result[val] = {}
                else:
                    result[users[i]['name']][key] = val
    with open(input_file_name, 'w', encoding='UTF-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)


def main():
    input_file_name = input()
    changes_file_name = input()
    solution(input_file_name, changes_file_name)


if __name__ == '__main__':
    main()
