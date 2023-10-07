from sys import stdin
import json


def solution(file_name: str, new_key_vals: dict):
    with open(file_name, encoding='UTF-8') as f:
        old_json: dict = json.load(f)
    old_json.update(new_key_vals)
    with open(file_name, 'w', encoding='UTF-8') as f:
        json.dump(old_json, f, ensure_ascii=False, indent=2)


def main():
    inp = [i.rstrip('\n') for i in stdin.readlines()]
    file_name = inp.pop(0)
    k_vs = [k_v.split(' == ') for k_v in inp]
    new_keys_vals = dict(k_vs)
    solution(file_name, new_keys_vals)


if __name__ == '__main__':
    main()
