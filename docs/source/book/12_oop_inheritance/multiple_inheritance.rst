Множественное наследование
--------------------------

В Python дочерний класс может наследовать несколько родительских.


class A:
    def __init__(self):
        print('A.__init__')

class B:
    def __init__(self):
        print('B.__init__')

class C(A, B):
    def __init__(self):
        print('C.__init__')
