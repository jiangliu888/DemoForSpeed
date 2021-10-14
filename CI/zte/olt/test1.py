def solution(N):
    # write your code in Python 3.6
    str0 = str(N)    
    if N < 0 and len(str)>2:
        return int(str0[0]+"5"+str[2:])
    elif N > 0:
        res =""
        for i in range(len(str0)):
            if str0[i] > 5:
                res+=str(str0[i])
            else:
                res+="5"+str0[i]
        return int(res)
    else:
        return 50


N = 378
solution(N)