





if __name__ == '__main__':
    file = open('example.txt', 'r') # r => read
    #file.seek(0) # move pointer to the first area
    content = file.readlines() # read line by line and retur a list     
    print(content)
    content = [i.rstrip("\n") for i in content]
    print(content)
    for item in content:
        score = int(item)
        score = score * 1.6
        print(score)
    content = [int(i) * 1.6 for i in content]  
    print(content)