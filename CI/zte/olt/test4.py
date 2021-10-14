# -*- coding: UTF-8 -*-
# 给数字带上含义，和元组中一一对应
name, age, sex, email = 0, 1, 2, 3                        
# 高级：name, age, sex, email = range(4)
student = ('tom', 18, 'male', 'tom @ qq.com' )
print(student[name])
if student[age] > 12:
     print('True')
if student[sex] == 'male':
    print('True')

from collections import namedtuple
 
# 生成一个Student类
Student = namedtuple('Student', ['name', 'age', 'sex', 'email'])
# 生成一条信息对象
s = Student('tom', 18, 'male', 'tom@qq.com')
# 通过类对象进行取数据
print(s.name, s.age, s.sex, s.email)

from random import randint
 
def count_seq(data):     
    # fromkeys() 函数用于创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值
    # 初始化统计结果字典,data中的key作为结果字典的key，0作为每个key的初始值
    result_c = dict.fromkeys(data, 0)     
    # 循环data，对字典中中碰到的值进行 +1 ，循环完成后就是结果
    for x in data:
        result_c[x] += 1
    return result_c
 
if __name__ == '__main__':
    # 生成２０个随机数
    data = [randint(0, 20) for _ in range(20)]
    print(data)    
    # 结果
    result_c = count_seq(data)
    for i in result_c:
        print(i, result_c[i])

from collections import Counter
 
 
def count_seq(data):
     
    # 创建Counter对象，并把打他传递进去
    median_c = Counter(data)
     
    # 返回统计最大的3个数
    return median_c.most_common(3)
 
if __name__ == '__main__':
    # 生成２０个随机数
    data = [randint(0, 20) for _ in range(20)]
    print(data)
     
    # 结果
    result_c = count_seq(data)
    print(result_c, dict(result_c))

d = {x:randint(60,100) for x in 'abcdefg'}

