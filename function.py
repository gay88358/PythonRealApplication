
# define swap = 交換
# num1 = 2, num2 = 4

# call by value
def swap1(num1, num2):
    temp = num2 # temp = 4
    num2 = num1 # num2 = 2
    num1 = temp # num1 = 4

def swap2(num1, num2):
    return num2, num1

# call by reference : memory
def swap3(data): # [2, 4]
    temp = data[1] # temp = 4
    data[1] = data[0] # data[1] = 2 [2, 2]
    data[0] = temp # data[0] = 4 [4, 2]
     
if __name__ == '__main__':
    x = 2
    y = 4
    swap1(x, y)
    data = [2, 4]
    swap3(data)
    print(data[0])
    print(data[1])

