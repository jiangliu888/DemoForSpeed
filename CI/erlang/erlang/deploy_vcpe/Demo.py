json_array = [{"time":20150312,"value":"c"}, {"time":20150301,"value":"a"}, {"time":20150305,"value":"b"}]
json_array.sort(key = lambda x:x["time"])
print(json_array)

a = [('b', 4), ('a', 12), ('d', 7), ('h', 6), ('j', 3)]
#key不代表json字符串的key值、默认升序(False)
a.sort(key=lambda x: x[1],reverse=True)
print(a)