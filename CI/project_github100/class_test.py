# -*- coding: UTF-8 -*-
class Test(object):

    def __init__(self,foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')

def main():
    test = Test('hello')
    #不允许外界访问
    #test.__bar()
    #不允许外界访问
    #print(test.__foo)
    # 该方法可以：单下划线+类名
    print(test._Test__foo)

if __name__=="__main__":
    main()


