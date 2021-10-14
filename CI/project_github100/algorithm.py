# -*- coding: UTF-8 -*-
""" 
穷举法 - 暴力破解法，对所有的可能性进行验证，直到找到正确答案。
贪婪法 - 在对问题求解时，总是做出在当前看来最好的选择，不追求最优解，快速找到满意解。
分治法 - 把一个复杂的问题分成两个或更多的相同或相似的子问题，再把子问题分成更小的子问题，直到可以直接求解的程度，最后将子问题的解进行合并得到原问题的解。
回溯法 - 又称为试探法，按选优条件向前搜索，当搜索到某一步发现原先选择并不优或达不到目标时，就退回一步重新选择。
动态规划 - 基本思想也是将待求解问题分解成若干个子问题，先求解并保存这些子问题的解，避免产生大量的重复运算。 """
#回溯法
import sys
import time

# 定义棋盘大小
SIZE = 5
# 定义一个全局变量，用于记录第total种巡游方式。
total = 0

def print_board(board):
    for row in board:
        for col in row:
            print(str(col).center(4))
        print()

def patrol(board, row, col, step=1):
    if row >= 0 and row < SIZE and \
        col >= 0 and col < SIZE and \
        board[row][col] == 0:
        board[row][col] = step
        # 当最后一步恰好等于 25（本案例5*5）时，打印输出巡游路线
        if step == SIZE * SIZE:
            global total
            total += 1
            print '第{total}种走法: '
            print_board(board)
        # 下一步可能会走的位置
        patrol(board, row - 2, col - 1, step + 1)
        patrol(board, row - 1, col - 2, step + 1)
        patrol(board, row + 1, col - 2, step + 1)
        patrol(board, row + 2, col - 1, step + 1)
        patrol(board, row + 2, col + 1, step + 1)
        patrol(board, row + 1, col + 2, step + 1)
        patrol(board, row - 1, col + 2, step + 1)
        patrol(board, row - 2, col + 1, step + 1)
        board[row][col] = 0

def main():
	# 生成5*5的棋盘
    board = [[0] * SIZE for _ in range(SIZE)]
    #设定巡游起点为索引（4,4）
    patrol(board, SIZE - 1, SIZE - 1)

if __name__ == '__main__':
    main()




#动态规划
# def main():
#     items = list(map(int,input().split()))
#     overall = partial =items[0]
#     for i in range(1,len(items)):
#         partial = max(items[i],partial+items[i])
#         overall = max(partial,overall)
#     print(overall)

# if __name__ == '__main__':
#     main()

