







if __name__ == '__main__':
    fruits = ['apple', 'banana', 'peach']

    with open('fruit.txt', 'w') as file:
        for f in fruits:
            file.write(f + '\n')




    file = open("fruit.txt", 'w')

    fruits = ['apple', 'banana', 'peach']
    for fruit in fruits:
        file.write(fruit + "\n")    
    file.close()
