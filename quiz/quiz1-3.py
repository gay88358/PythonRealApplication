



def convert_celsius_to_fahrenheit(c):
    if c <= -273.15:
        return "That temperature doesn't make sense!"    
    f = c * 9 / 5 + 32
    return f


if __name__ == '__main__':
    c = -300
    f = convert_celsius_to_fahrenheit(c)
    print(f) # 86



    