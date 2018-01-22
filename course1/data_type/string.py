




if __name__ == '__main__':
    name = "Z-Xuan Hong"
    print(name[-1]) # g
    print(name[1:5]) # -Xua [1, 5)
    print(name[:-1]) # [0:-1] Z-Xuan Hon
    print(name[-2:]) # ng

    name = name.replace(" ", "-") # replace all space with - => Z-Xuan-Hong
    print(name)
    name = name.replace("-", " ", 1) # replace first '-' with space => Z Xuan-Hong
    print(name)
    name = name.replace("-", " ", 2) # replace second '-' with space => Z Xuan Hong
    print(name)
    

    


