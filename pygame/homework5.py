# import numpy as np

# def FIFO (mylist, n):
#     print("hello Fifo")
#     count = 0 # 缺页数量
#     array = np.array([11, 11, 11, 11])
#     print(array)


# def LRU (mylist, n):
#     print("hello lru")


# def Clock (mylist, n):
#     print("hello, clock")



# mylist = [0, 9, 8, 4, 4, 3, 6, 5, 1, 5, 0, 2, 1, 1, 1, 1, 8, 8, 5, 
# 3, 9, 8, 9, 9, 6, 1, 8, 4, 6, 4, 3, 7, 1, 3, 2, 9, 8, 6, 2, 9, 2, 7, 
# 2, 7, 8, 4, 2, 3, 0, 1, 9, 4,7, 1, 5, 9, 1, 7, 3, 4, 3, 7, 1, 0, 3, 5,
# 9, 9, 4, 9, 6, 1, 7, 5, 9, 4, 9, 7, 3, 6, 7, 7, 4, 5, 3, 5, 3, 1, 5, 6, 1, 
# 1, 9, 6, 6, 4, 0, 9, 4, 3]


# print("hello" == "hello")

# n = input()
# str = input()

# if str == "LRU" :
#     LRU(mylist, n)

# elif str == "FIFO":
#     FIFO(mylist, n)

# elif str == "Clock":
#     Clock(mylist, n)
    
# else :
#     print("WRONG AL")

print('\n'.join([''.join([(" missU"[(x-y) % len(" missU")] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))

# print('\n'.join([''.join([('黎娟'[(x-y) % len('黎娟')]
#                            if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ')#此处是根据心形曲线公式来的(x2+y2-1)3-x2y3=0
#                           for x in range(-30, 30)])#定义高
#                  for y in range(30, -30, -1)]))#定义宽

# import time
# sentence = "Dear, I love you forever!"    ## 将该字符串以心形文字打印出来
# for char in sentence.split():
#    allChar = []
#    for y in range(12, -12, -1):
#        lst = []
#        lst_con = ''
#        for x in range(-30, 30):
#             formula = ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3
#             if formula <= 0:
#                 lst_con += char[(x) % len(char)]
#             else:
#                 lst_con += ' '
#        lst.append(lst_con)
#        allChar += lst
#    print('\n'.join(allChar))
#    time.sleep(1)