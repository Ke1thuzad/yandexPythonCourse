def solution(friendships_lvl1: dict):
    friendships_lvl2 = {}
    for person in friendships_lvl1.keys():
        if person not in friendships_lvl2:
            friendships_lvl2[person] = set()
            for friend in set(friendships_lvl1[person]):
                friendships_lvl2[person].update(get_next_friendship_lvl(friend, person, friendships_lvl1))
    for person, friends in sorted(friendships_lvl2.items()):
        out = f'{person}: '
        for friend in sorted(friends):
            out += friend + ', '
        print(out.strip(', '))


def get_next_friendship_lvl(friend, person, friendships_lvl1: dict):
    return set(i for i in friendships_lvl1[friend] if i != person and i not in friendships_lvl1[person])


def main():
    user_input = input()
    friendships_lvl1 = {}
    while user_input != '':
        person, friend = user_input.split()
        if person not in friendships_lvl1:
            friendships_lvl1[person] = [friend]
        else:
            friendships_lvl1[person].append(friend)

        if friend not in friendships_lvl1:
            friendships_lvl1[friend] = [person]
        else:
            friendships_lvl1[friend].append(person)
        user_input = input()

    solution(friendships_lvl1)


if __name__ == '__main__':
    main()
