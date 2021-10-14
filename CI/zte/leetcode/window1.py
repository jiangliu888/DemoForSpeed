# coding:utf-8
""" 题1：给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC" """
import collections

def minWindow(s,t):
    need = collections.defaultdict(int) # 记录t中字符出现次数
    window = collections.defaultdict(int) # 记录窗口中响应的字符出现的次数
    for c in t:
        need[c] += 1    
    left,right = 0,0 
    valid = 0 # 用于记录window中t中字符是否出现完
    start = 0
    length = len(s) + 1

    while right < len(s):
        c = s[right] # 即将加入window的字符c
        right += 1 # 右移窗口
        # 1) 窗口内数据的一系列更新
        if c in need:
            window[c] += 1
            if window[c] == need[c]: # window中字符c出现的次数已经达到need所需要的次数时，valid进行更新
                valid += 1
        # 2)判断窗口左侧边界是否要收缩
        while valid == len(need):
            # 更新最小覆盖子串
            if right-left < length:
                start = left
                length = right-left
            # d是将移出窗口的字符
            d = s[left]
            # 左移窗口
            left += 1
            # 3)进行窗口内数据的一系列更新
            if d in need:
                if window[d] == need[d]: 
                    valid -= 1
                window[d] -= 1
    return '-1' if length == len(s) + 1 else s[start:start+length]

print(minWindow("ADOBECODEBANC","ABC"))

 