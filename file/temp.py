


def c2f(c):
    if c <= -273.15:
        return 'Invalided value!!'
    else :
        return c * 9 / 5 + 32




if __name__ == '__main__':
    temp = [20, 23.3, 34.4]
    with open('temp.txt', 'w') as file:
        for tem in temp:
            file.write(str(c2f(tem)) + '\n')
        