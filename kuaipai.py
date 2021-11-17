# -*- coding:utf-8 -*-
import os
import csv
import xlrd
import time
import random
import requests
from lxml import etree
# 快排
# def partition(arr, low, high):
#     i = (low - 1)  # 最小元素索引
#     print('最小元素索引: ', i)
#     pivot = arr[high]
#     print("标记元素： ", pivot)
#     for j in range(low, high):
#         # 当前元素小于或等于 pivot
#         if arr[j] <= pivot:
#             i = i + 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return (i + 1)
#
# # arr[] --> 排序数组
# # low  --> 起始索引
# # high  --> 结束索引
# # 快速排序函数
# def quickSort(arr, low, high):
#     if low < high:
#         pi = partition(arr, low, high)
#         print('----'*20)
#         print(pi)
#         print(arr)
#         quickSort(arr, low, pi - 1)
#         quickSort(arr, pi + 1, high)
#
#
# arr = [10, 7, 8, 9, 1, 5]
# print('原始列表:', arr)
# n = len(arr)
# print("索引:", 0, n-1)
# quickSort(arr, 0, n - 1)
# print("排序后的数组:")
# for i in range(n):
#     print("%d" % arr[i])


def quick_sort(s):
    # 结束条件
    if len(s) < 2:
        return
    # 从列表取出一个元素作为基准值
    p = s[0]
    L = [] # 小于
    E = [] # 等于
    R = [] # 大于
    # 把s里的元素放入3个队列
    while len(s) > 0:
        if s[-1] < p:
            L.append(s.pop())
        elif s[-1] == p:
            E.append(s.pop())
        else:
            R.append(s.pop())

    print('L:', L)
    print("E:", E)
    print("R:", R)
    print('----' * 20)
    quick_sort(L)
    quick_sort(R)
    s.extend(L)
    s.extend(E)
    s.extend(R)

if __name__ == '__main__':
    # s = [111,5,7,9,3,2,1,4,6,11,45,75]
    s = [5, 7, 9, 3, 6, 1, 4, 2]
    print('s:', s)
    print('----' * 20)
    quick_sort(s)
    print('s:', s)