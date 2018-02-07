




# void function which means that function is no return value
#def functionName(parameter):
    # do something...
# if return type is int then we call int function and so on...
#def functionName(parameter):
    # do something...
#    return something



def f(x):
    return x**2 + x + 1

def eatSpaceByGivenIndexElement(myStr, index):
    myStr[index] = myStr[index].replace(' ', '')


def c2f(c):
    if c <= -273.15:
        return 'Invalided Input'
    else:
        return c * 9 / 5 + 32



if __name__ == '__main__':
    c = input('input degree: ')
    print(c2f(float(c)))







#    names = ['app le', 'banana', 'peach']
#   eatSpaceByGivenIndexElement(names, 0)
#    print(names) # ['apple', 'banana', 'peach']

    #x = 3
    #y = f(3)
    #print(y) # 13



    




