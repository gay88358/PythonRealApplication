







if __name__ == '__main__':
    file = open("fruit.txt", 'w')

    fruits = ['apple', 'banana', 'peach']
    for fruit in fruits:
        file.write(fruit + "\n")    
    file.close()
