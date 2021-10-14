# coding:utf-8
from collections import defaultdict
""" 输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
 """
def findArray(s,p):
    needs,window = defaultdict(int),defaultdict(int)
    left,right = 0,0
    valid = 0
    res =[]
    for i in p:
        needs[i] = 1
    
    while right < len(s):
        c = s[right]
        #右移窗口
        right +=1
        #1)****窗口扩大****
        if c in needs:
            window[c]+=1
            if window[c] == needs[c]:
                valid+=1
        #2)****判断是否需要窗口收缩****
        while right - left >=len(p):
            if valid ==len(needs):
                res.append(left)
        #**************************
            d = s[left]
            #左移窗口
            left += 1
            #3)****窗口缩小****
            if d in needs:
                if window[d] == needs[d]:
                    valid -= 1
                window[d] -= 1
    return res

print(findArray("cbaebabacd","abc"))