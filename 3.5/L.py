def solution(nums: list[tuple[str, int]]):
    even = [('', 0)]
    odd = [('', 0)]
    eq = [('', 0)]
    lst = -1
    for i in range(len(nums)):
        if nums[i][0].isnumeric():
            lst = distribute_to_group_by_digits(nums[i][0])
        match lst:
            case 0:
                last_pos = even[-1][1]
                cur_pos = nums[i][1]
                if last_pos != cur_pos:
                    even.append(('\n' * (cur_pos - last_pos), last_pos))
                even.append(nums[i])
            case 1:
                last_pos = odd[-1][1]
                cur_pos = nums[i][1]
                if last_pos != cur_pos:
                    odd.append(('\n' * (cur_pos - last_pos), last_pos))
                odd.append(nums[i])
            case 2:
                last_pos = eq[-1][1]
                cur_pos = nums[i][1]
                if last_pos != cur_pos:
                    eq.append(('\n' * (cur_pos - last_pos), last_pos))
                eq.append(nums[i])
    return even, odd, eq


def distribute_to_group_by_digits(x: str):
    even = 0
    for digit in x:
        if int(digit) % 2 == 0:
            even += 1

    odd = (len(x) - even)
    if odd < even:
        return 0
    if odd > even:
        return 1
    return 2


def main():
    file_title = input()
    even_file_title = input()
    odd_file_title = input()
    eq_file_title = input()
    nums = []
    with open(file_title) as f:
        lines = f.readlines()
    for i in range(len(lines)):
        for val in lines[i].split():
            nums.append((val, i))

    evens, odds, eqs = solution(nums)

    with open(even_file_title, 'w', encoding='UTF-8') as f:
        formatted_even = ' '.join([val[0] for val in evens]).replace('\n ', '\n').strip(' ')
        f.write(formatted_even + '\n' * (nums[-1][1] + 1 - formatted_even.count('\n')))
    with open(odd_file_title, 'w', encoding='UTF-8') as f:
        formatted_odd = ' '.join([val[0] for val in odds]).replace('\n ', '\n').strip(' ')
        f.write(formatted_odd + '\n' * (nums[-1][1] + 1 - formatted_odd.count('\n')))
    with open(eq_file_title, 'w', encoding='UTF-8') as f:
        formatted_eq = ' '.join([val[0] for val in eqs]).replace('\n ', '\n').strip(' ')
        f.write(formatted_eq + '\n' * (nums[-1][1] + 1 - formatted_eq.count('\n')))


if __name__ == '__main__':
    main()
