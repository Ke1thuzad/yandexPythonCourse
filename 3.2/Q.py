def solution(a: str):
    friends = {}
    friends_2 = {}
    while a != '':
        person, friend = a.split()
        if person not in friends:
            friends[person] = []
        if friend not in friends:
            friends[friend] = []
        friends[person].append(friend)
        friends[friend].append(person)
        a = input()
    for p, f in friends.items():
        friends_2[p] = []
        for fr in f:
            if fr in friends:
                friends_2[p] += friends[fr]
    for man in sorted(friends_2.keys()):
        print(man, end=': ')
        friends_out = ''
        for mfriend in sorted(set(friends_2[man])):
            if mfriend != man:
                friends_out += mfriend + ', '

        print(friends_out.removesuffix(', '))


def main():
    a = input()
    solution(a)


if __name__ == '__main__':
    main()
