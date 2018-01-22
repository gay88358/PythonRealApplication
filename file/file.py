





if __name__ == '__main__':
    file = open("example.txt", 'r')
    content = file.read() # read all file and return string type
    print(content)
    file.seek(0) # move pointer to the first area
    content = file.readlines() # read line by line and retur a list 
    print(content)
    content = [i.rstrip("\n") for i in content] # delete the \n
    print(content)


