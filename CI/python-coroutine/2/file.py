# -*- encoding=utf-8 -*-

with open('empty-1G.txt', 'w') as f:
    for i in range(1024*1024):
        for j in range(1024):
            f.write('c')
        f.flush()

