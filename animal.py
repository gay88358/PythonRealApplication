
# 繼承可以得到parent的function跟變數
class Animal:
    def __init__(self, kind):
        self._kind = kind

    def kind(self):
        return self._kind

    def sound(self):
        print('...')

class Cat(Animal):
    def __init__(self, kind):
        Animal.__init__(self, kind)
    # 重新複寫parent class的function
    # function overwrite
    
    #def kind(self):
    #    return self._kind
    def sound(self):
        print('mmm')


if __name__ == '__main__':
    cat = Cat('cat')
    print(cat.kind())
    cat.sound()