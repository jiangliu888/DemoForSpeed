# -*- coding: UTF-8 -*-
class Person(object):

    __slots__ = ('_name','_age','_gender')

    def __init__(self,name,age):
        self._name = name
        self._age = age
    # 访问器 - getter方法
    @property
    def name(self):
        return self._name
    # 访问器 - getter方法
    @property
    def age(self):
        return self._age
    # 修改器 - setter方法
    @age.setter
    def age(self,age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print("{}:aaa".format(self._name))
        else:
            print("{}:bbb".format(self._name))

def main():
    person = Person('AAA',12)
    person.play()
    person._gender ='男'
    print("{}".format(person._gender))
if __name__=="__main__":
    main()    