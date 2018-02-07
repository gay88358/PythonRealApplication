


# if __name__ == '__main__':
#     step = 7
#     max = (step / 2) + 1
#     for i in range(1, step+2, 2):
#         y = (i + 1) / 2
#         space = max - y
#         for k in range(0, int(space)):
#             print(' ', end='')
#         for j in range(0, i):
#             print('*', end='')
#         print('')

if __name__ == '__main__':
    height = 5
    for i in range(1, height + 1):
        for j in range(height - i):
            print(' ', end='')
        for k in range(i * 2 - 1):
            print('*', end='')
        print('')

    for i in range(1, height + 1):
        for j in range(i - 1):
            print(' ', end='')
        for k in range((height - i) * 2 + 1):
            print('*', end='')
        print('')





        