class Foo:
    def __init__(self,num1,num2):
        self.__num1=num1
        self.num2=num2

    def __str__(self):
        return str(self.__dict__)

f1=Foo(10,20)
f2=Foo(20,30)
f3=Foo(30,40)
print(f1,f2,f3)
                                                
