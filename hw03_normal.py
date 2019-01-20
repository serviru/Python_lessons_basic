__author__ = "Кравченко Сергей Иванович"

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
     res = []
    last=0
    next=1
    for i in range(m+1):
        # print ("i={}, last={}, next={}".format(i,last,next))
        if i >= n: res.append(next)
        last,next = next,next+last
    return res

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    res=origin_list[:]
    for i in range(1,len(origin_list)):
        j=i
        while (res[j]<res[j-1]) and (j>0):
            res[j],res[j-1] = res[j-1],res[j]
            j-=1
    return res


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(func,iter):
    res=[]
    for i in iter:
        if func(i):
            res.append(i)
    return res

def my_iter_filter(func,iter):
    for i in iter:
        if func(i):
            yield i

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def isparallelogramm(a1,a2,a3,a4):
    def centerpoint(a,b):
        return ((a[0]+b[0])/2,(a[1]+b[1])/2)
    if a1 == a3: return False
    return centerpoint(a1,a3) == centerpoint(a2,a4)
