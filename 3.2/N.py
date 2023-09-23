def solution(n: int):
    ingredients = set(input() for _ in range(n))
    recipes = {}
    m = int(input())
    for i in range(m):
        nametag = input()
        req_ingredients = set()
        for j in range(int(input())):
            req_ingredients.add(input())
        if frozenset(req_ingredients) in recipes:
            recipes[frozenset(req_ingredients)].append(nametag)
        else:
            recipes[frozenset(req_ingredients)] = [nametag]
    some_recipes = []
    for recipe in recipes:
        intersect = ingredients.intersection(recipe)
        if intersect == recipe:
            some_recipes += recipes[frozenset(intersect)]
    if not some_recipes:
        print('Готовить нечего')
    else:
        print(*sorted(some_recipes), sep='\n')


def main():
    n = int(input())
    solution(n)


if __name__ == '__main__':
    main()
