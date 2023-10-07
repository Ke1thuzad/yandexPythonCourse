# ОЧЕРЕДНАЯ ОЧЕНЬ ИНТЕРЕСНАЯ ЗАДАЧА, ГДЕ НАДО ПОДУМАТЬ, А НЕ ПИСАТЬ ГИГАНТСКИЙ КОД. УРА!
def solution():
    total = 0
    with open('test.num', 'rb') as f:
        byte = f.read(2)
        while byte:
            if str(byte).count('\\x') == 2:
                total += int.from_bytes(byte)
            byte = f.read(2)
    print(total)

# 1196764 [b'\x16\xe1', b'\x11&', b'SX', b'\xf0\xad', b'v\xf4', b'\x87\xcd', b'h<', b'x\x95', b'w\xde', b'\xe1\xf0', b'\x08f', b'\x0f\xb6', b'\xf7Z', b'\xcd\xda', b'K\x9d', b'v\x97', b'\xb0\x1f', b'h\x99', b'\xa6\xff', b'\xa3s', b'I ', b'o\xd1', b'Im', b'\xedE', b'\x98\xfe', b'\xe4\xfe', b'\x02\xaa', b'\x1f0', b'\x06\x8e', b'\x19\x00', b'Pn', b'R\xa2', b'\x1a\x04', b'\xaa\xe9', b'c\xa0', b'\x0b*', b't\xb7', b'\xca\xc7', b'\xef\xbe', b'\xe5\xb8']
def main():
    solution()


if __name__ == '__main__':
    main()
