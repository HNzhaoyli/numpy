"今天开始学习numpy基础篇"
'''1 基础知识'''
import numpy as np
a = np.arange(15).reshape(3,5)#arange 返回的是数组，而不是列表
print(a)
print(a.ndim,a.shape,a.size,a.dtype.name,a.itemsize)
#     维度   形状   大小   类型  每个元素的字节大小
'''[[ 0  1  2  3  4]
    [ 5  6  7  8  9]
    [10 11 12 13 14]]
2 (3, 5) 15 int32 4'''
print("2****************")


'''2 创建数组'''
a = np.array([1,2,3,4])
b = np.array([[1,2,3,4],[5,6,7,8]])
print(a)
print(b)
'''
[1 2 3 4]
[[1 2 3 4]
 [5 6 7 8]]
'''
print("*****************************")
a = np.zeros((3,4))
print(a)
b = np.ones((2,3),dtype=int)
print(b)
print("**********************************")

#arange 函数返回数组
a = np.arange(1,10,2) #(start,end,step)   必须在numpy里边才可以用
print(a)#[1 3 5 7 9]
b = np.arange(1,3,0.5)#支持小数  range()不支持
a = np.random.random((2,3))
print(a,"3****************")
'''3 打印数组'''
'''当你打印一个数组，numpy会类似于嵌套列表的方法显示
    0  最后的轴从左往右打印
    0  次后的轴从上到下打印
    0  剩下的轴从上到下打印，每个切片通过一个空行与下一个隔开'''
a = np.arange(6)#1d
b = np.arange(6).reshape(2,3)#2d
c = np.arange(24).reshape(2,3,4)#3d
print(a,b,c)
print("***********")
print(np.arange(10000).reshape(100,100))
print("4********************")
"""4基本运算"""
a = np.array([1,2,3,4])
b = np.arange(4)
c = a - b
print(c)#[1 1 1 1]
#sin(c)  #numpy 中的乘法运算符*按元素计算 ，矩阵乘法可以使用dot函数
a = np.array([[1,2],
             [3,4]])
b = np.array([[1,2],
             [3,4]])
print(a*b) #对应位置相乘
print(b.dot(a))#矩阵相乘

a = np.ones((2,3))
a *= 3
print(a) #每个位置乘以3

a = np.linspace(1,10,3)#(start,end,num)
print(a)

"""sum,min,max  涉及到轴方向运算
axis = 0  #列相加
axis = 1  #行相加"""
a = np.arange(12).reshape(3,4)
print(a)
print(a.sum(axis = 0))
print(a.sum(axis = 1))
print("5********************")
"""5 通用函数ufunc
numpy 提供的常见数学函数如 sin  cos exp  ,这些叫做通用函数ufunc
numpy 里边，函数作用是按照数组的元素运算，产生一个数组作为输出"""

a = np.arange(12).reshape((3,4))
print(a)
