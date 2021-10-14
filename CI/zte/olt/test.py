# def quick_sort(quick_list):
#     if quick_list == []:
#         return []
#     else:
#         k = quick_list[0]
#         less = quick_sort([l for l in quick_list[1:] if l < k])
#         more = quick_sort([m for m in quick_list[1:] if m >= k])
#         return less + [k] + more

# result = quick_sort([2,1,33,2,4,5,6])
# print(result)

list0=[1,2,3,4,5,6,7]
print(list0[:4])
print(list0[:4][::-1])
print(list0[1:])