


# 用來註解，當編譯器執行到這行，不會執行


if __name__ == '__main__':
    data = [ 2, 3, 4, 1, 2, 3 ] # integer list
    name = ['apple', 'htc', 'samsung', 'asus', 'acer'] # string list
    #indexing of list
    print(data[0]) # 2 first element
    print(data[-1]) # last element
    print(data[2:4]) # 4 2 
    print(data[:4]) # 2 3 4 1
    print(data[1:-1]) # 3 4 1 2
    print(data[0:]) # all element
    data.append(100) # append
    print(data)


