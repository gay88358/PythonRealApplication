
# 物件：由function跟變數組合而成，會改變狀態
# parent class
class Note:
    # 建構子，用來初始化物件的狀態
    def __init__(self):
        print('constructor...')
        self._text = ''
        print('constructor done...')
    
    def read(self):
        return self._text

    def write(self, text):
        self._text = self._text + text + ' '
# () 繼承
# child class
class SimpleNote(Note):
    def __init__(self):
        Note.__init__(self)

    
# child class
class PasswordNote(Note):
    def __init__(self):
        Note.__init__(self)
        self._password = 1234111222
    
    def read(self, password):
        if password == self._password:
            return self._text
        else:
            print('Password Error!')

    def write(self, password, text):
        print('write...')
        if self._password == password:
            self._text = self._text + text + ' '
        else:
            print('Password Error!')
        print('write done...')

if __name__ == '__main__':
    passwordNote = PasswordNote()
    password = 1234111222
   
    result = passwordNote.read(password)
    print(result)
    #simpleNote = SimpleNote()
    #simpleNote.write('python')
    #simpleNote.write('is')
    #simpleNote.write('fun')
    #result = simpleNote.read()
    #print(result)
    

