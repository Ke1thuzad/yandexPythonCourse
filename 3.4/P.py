from itertools import product, combinations


def solution(req_mast: str, ignored_val: str):
    to_mast = {"буби": "бубен", "пики": "пик", "трефы": "треф", "черви": "червей"}
    specials = ["валет", "дама", "король", "туз"]
    if ignored_val not in specials:
        nums = [str(i) for i in range(2, 11) if str(i) != ignored_val]
    else:
        nums = [str(i) for i in range(2, 11)]
        specials.remove(ignored_val)
    combs = list(product(sorted(nums + specials), to_mast.values()))
    final_combs = sorted(combinations(combs, r=3))

    i = 0
    for comb in final_combs:
        out = ", ".join(" ".join(a) for a in comb)
        if to_mast[req_mast] in out:
            print(out)
            i += 1
        if i == 10:
            break


def main():
    req_mast = input()
    ignored_val = input()
    solution(req_mast, ignored_val)


if __name__ == "__main__":
    main()
