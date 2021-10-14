# -*- coding: UTF-8 -*-
class Attr(object):
    def __init__(self,name,type_):
        self.name = name
        self.type_ = type_
    
    def __get__(self,instance,cls):
        print('in __get__',instance,cls)
        return instance.__dict__[self.name]  # 将self.name变为实例P的属性

    def __set__(self,instance,value):
        print('in __set__')
        if not isinstance(value,self.type_):
            raise TypeError('expected an %s' % self.type_)
        instance.__dict__[self.name] = value  # 将self.name变为实例P的属性

    def __delete__(self,instance):
        print('in __delete__')
        del instance.__dict__[self.name]

class Person(object):
    name = Attr('name', str)
    age = Attr('age', int)
    height = Attr('height', float)
p = Person()
p.name = 'Bob'
print(p.name)
p.age = '17'
print(p.age)