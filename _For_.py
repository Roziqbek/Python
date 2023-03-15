import math


13 # n = int(input())
# s = 0
# for i in range(1,n+1):
#     s = (s + i/10)
# print(s)

14 # n = int(input())
# s = 0
# for i in range(1,n+1):
#     s = s + (2*i-1)
# print(s)

15 # a = int(input())
# n = int(input())
# s = 1
# for i in range(n):
#     s = s * a
# print(s)

16 # a = int(input("Sonni kiriting: "))
# n = int(input("Darajasini kiriting: "))
# for i in range(1,n+1):
#     print(pow(a,i))

17 # a = int(input("Sonni kiriting: "))
# n = int(input("Darajaning kiriting: "))
# s = 0
# for i in range(n+1):
#     b = a**i
#     s = s + b
# print(s)

18 # a = int(input())
# n = int(input())
# s = 0
# d = 0
# for i in range(n+1):
#     b = (-a)**i
#     s += b
# print(s)

19 # n = int(input())
# s = 1
# for i in range(1,n+1):
#     s *= i
# print(s)

20 # n = int(input())
# s = 0
# for i in range(1,n+1):
#     s = s + math.factorial(i)
# print(s)

23 # n = int(input())
# x = int(input())
# b = 0
# s = 0
# for i in range(n+1):
#     b = (-1)**i*(x)**(2*i+1)/(math.factorial(2*i+1))
#     s += b
# print(s)














29 # a = int(input())
# b = int(input())
# for i in range(a,b+1):
#   print(i)

30 # n = int(input())
# a = int(input())
# b = int(input())
# for i in range(a,b+1):
#   print(1-math.sin(i))

31 # def new_function(n):
#   if n == 0:
#     return 2
#   else:
#     return 2+1/new_function(n-1)
# print(new_function(int(input())))

32 # def new_function(k):
#   if k==0:
#     return 1
#   else:
#     return (new_function(k-1)+1)/k
# print(new_function(int(input())))

33 # def new_function(k):
#   if k==2 or k==1:
#     return 1
#   else:
#     return (new_function(k-2)+new_function(k-1))
# print(new_function(int(input())))

34 # def new_function(k):
#   if k==1:
#     return 1
#   elif k==2:
#     return 2
#   else:
#     return (new_function(k-2)+2*(new_function(k-1)))/3
# print(new_function(int(input())))

###################################################### Fibonachi son
# n = 10
# son1 = 0
# son2 = 1
# for i in range(n):
#   continue1 = son1 + son2
#   son1 = son2
#   son2 = continue1
#   print(continue1)

#######################################################

35 # def new_function(k):
#   if k == 1:
#     return 1
#   elif k == 2:
#     return 2
#   elif k == 3:
#     return 3
#   else:
#     return new_function(k-1)+new_function(k-2)-2*(new_function(k-3))
# print(new_function(int(input())))


36 # k = int(input())
# s = 0
# for i in range(1,k+1):
#   s += (i**k)
# print(s)


37 # n = int(input())
# s = 0
# for i in range(1,n+1):
#   s += i**i
# print(s)

38 # n = int(input())
# s = 0
# for i in range(1,n+1):
#   s = s + i**(n-i+1)
# print(s)

39 # n = int(input())
# for i in range(n+1):
#   for j in range(i):
#     print(i)

40 # a = int(input())
# b = int(input())
# for i in range(a+1,b):
#   for j in range(i):
#     print(i)
