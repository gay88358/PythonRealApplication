



def convert_celsius_to_fahrenheit(c):
    if c <= -273.15:
        return "That temperature doesn't make sense!"    
    f = c * 9 / 5 + 32
    return f


if __name__ == '__main__':
    file = open('celsius_to_fahrenheit.txt', 'w')
    temperatures=[10,-20,-289,100]
    for c in temperatures:
        f = convert_celsius_to_fahrenheit(c)
        file.write(str(f) + "\n")
    file.close()


    