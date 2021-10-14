# -*- coding: UTF-8 -*-
import requests
from collections import Iterable , Iterator

# 继承迭代器
class WeatherIterator(Iterator):
    def __init__(self,cities):
        self.cities = cities
        self.index = 0
    def getWeather(self,city):
        r = requests.get(u'http://wthrcdn.etouch.cn/weather_min?city=' + city)
        data = r.json()['data']['forecast'][0]
        return "%s:%s , %s" % (city, data["low"], data['high'])
    def next(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index +=1
        return self.getWeather(city)

# 迭代对象
class WeatherIterble(Iterable):
    def __init__(self,cities):
        self.cities = cities
    #调用迭代器对象
    def __iter__(self):
        return WeatherIterator(self.cities)

for x in WeatherIterble([u'广州',u'上海',u'北京',u'长沙']):
    print(x)