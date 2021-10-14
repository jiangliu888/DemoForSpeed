# -*- coding: UTF-8 -*-
""" 所谓抽象类就是不能够创建对象的类，这种类的存在就是专门为了让其他类去继承它 """

from abc import ABCMeta,abstractmethod

class Employee(object):

    def __init__(self,name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        pass

class Manager(Employee):
    def get_salary(self):
        return 15000.0

class Programmer(Employee):

    def __init__(self,name,working_hour=0):
        self._working_hour=working_hour
        super(Programmer,self).__init__(name)

    @property
    def working_hour(self):
        return self._working_hour

    @working_hour.setter
    def working_hour(self,working_hour):
        self._working_hour=working_hour if working_hour>0 else 0

    def get_salary(self):
        return 150.0 * self._working_hour

class Salesman(Employee):
    """销售员"""

    def __init__(self, name, sales=0):
        super(Salesman,self).__init__(name)
        self._sales = sales

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales if sales > 0 else 0

    def get_salary(self):
        return 1200.0 + self._sales * 0.05

def main():
    emps = [
        Manager('a'), Programmer('b'),
        Manager('c'), Salesman('d'),
        Salesman('e'), Programmer('f'),
        Programmer('g')
    ]

    for emp in emps:
        if isinstance(emp,Programmer):
            emp.working_hour = int(input('time:{} '.format(emp.name)))
        elif isinstance(emp, Salesman):
            emp.sales = float(input('sales:{} '.format(emp.name)))
        # 同样是接收get_salary这个消息但是不同的员工表现出了不同的行为(多态)
        print('{}:{}'.format(emp.name, emp.get_salary()))

if __name__ == '__main__':
    main()
