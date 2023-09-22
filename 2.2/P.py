def solution(p: int, v: int, t: int):
    participants = {'Петя': p, 'Вася': v, 'Толя': t}
    winners = list(participants.items())
    winners.sort(key=lambda x: x[1], reverse=True)

    for i in range(len(winners)):
        pos = (8 * (i + 1) % 16)
        if i == 2: # Не додумался как по-другому сделать :(
            pos += 8
        print(f'{" " * pos}  {winners[i][0]}  ')
    print('   II      I      III   ')


def main():
    p = int(input())
    v = int(input())
    t = int(input())
    solution(p, v, t)


if __name__ == '__main__':
    main()

