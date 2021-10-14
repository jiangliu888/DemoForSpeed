# coding:utf-8
""" 输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。 """
import collections

def lengthOfLongestSubstring(s):
    window = collections.defaultdict(int) # 记录窗口中响应的字符出现的次数
    left,right = 0,0 
    res = 0

    while right < len(s):
        c1 = s[right] # 即将加入window的字符c1
        window[c1]+=1
        right += 1 # 右移窗口
        while window[c1] >1:
            c2 = s[left]
            window[c2]-=1
            # 左移窗口
            left += 1   
        res = max(res,right-left)       
    return res

print(lengthOfLongestSubstring("abcbbcbb"))