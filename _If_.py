import math

1 # a = int(input())
# if a>0:
#   print(a+1)
# else:
#   print(a)

2 # a = int(input())
# if a>0:
#   print(a+1)
# else:
#   print(a-2)

3 # a = int(input())
# if a>0:
#   print(a+1)
# elif a<0:
#   print(a-2)
# elif a==0:
#   a = 10
#   print(a)

4 # a = int(input())
# b = int(input())
# c = int(input())
# s = 0
# q = 0
# for i in range(a+1,b):
#   s += 1
# for i in range(b+1,c):
#   q += 1
# print(s+q)










6 # a = int(input())
# b = int(input())
# if a>b:
#   print(a)
# elif a<b:
#   print(b)

7 # a = int(input())
# b = int(input())
# if a>b:
#   print(b)
# elif a<b:
#   print(a)

8 # a = int(input())
# b = int(input())
# if a>b:
#   print(a,b)
# if a<b:
#   print(b,a)

9 # a = int(input())
# b = int(input())
# if a>b:
#   son = a
#   sonb = b
#   b = son
#   a = sonb
#   print(a,b)
# elif a<b:
#   print(a,b)

10 # a = int(input())
# b = int(input())
# c = a+b
# if a!=b:
#     a=c
#     b=c
#     print(a,b)
# elif a==b:
#     a=0
#     b=0
#     print(a,b)

11 # a = int(input())
# b = int(input())
# if a!=b:
#   print(a+b)
# if a==b:
#   a = 0
#   b = 0
#   print(a,b)

12 # a = int(input())
# b = int(input())
# c = int(input())
# if a>b:
#     if a>c:
#         print(a)
# if b>a:
#     if b>c:
#         print(b)
# if c>a:
#     if c>b:
#         print(c)

13 # a = int(input())
# b = int(input())
# c = int(input())
# if a>b>c or c>b>a:
#     print(b)
# if b>a>c or c>a>b:
#     print(a)
# if a>c>b or b>c>a:
#     print(c)

14 # a = int(input())
# b = int(input())
# c = int(input())
# if a>b>c:
#     print(c,a)
# if a<b<c:
#     print(a,c)
# if b<a<c:
#     print(b,c)
# if b>a>c:
#     print(c,b)
# if a>c>b:
#     print(b,a)
# if a<c<b:
#     print(a,b)

15 # a = int(input())
# b = int(input())
# c = int(input())
# if a>b and b>c:
#     print(a,b)
# if a<b and b<c:
#     print(c,b)
# if b<a and a<c:
#     print(a,c)
# if b>a and a>c:
#     print(b,a)
# if a>c and c>b:
#     print(a,c)
# if a<c and c<b:
#     print(b,c)

16 # a = int(input())
# b = int(input())
# c = int(input())
# if a<b<c:
#     print(a*2,b*2,c*2)
# else:
#     print(-a,-b,-c)

17 # a = int(input())
# b = int(input())
# c = int(input())
# if a<b<c or a>b>c:
#     print(a*2,b*2,c*2)
# else:
#     print(-a,-b,-c)

18 # a = int(input())
# b = int(input())
# c = int(input())
# if a==b and a!=c and b!=c:
#     print(c)
# elif a==c and a!=b and b!=c:
#     print(b)
# elif b==c and b!=a and a!=c:
#     print(a)
# elif a==b and b==c:
#     print("Kiritishga xatolik")
# else:
#     print("Xatolik")

19 # a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if a==b==c:
#     print(d)
# if a==b==d:
#     print(c)
# if a==c==d:
#     print(b)
# if b==c==d:
#     print(a)

20 # a = int(input())
# b = int(input())
# c = int(input())
# ab = abs(a-b)
# ac = abs(a-c)
# if ab>ac:
#     print("Eng qisqa masofa AB:",ac)
# else:
#     print("Eng qisqa masofa AC:",ab)

21 # x = int(input())
# y = int(input())
# if y==0 and x==0:
#     print(0)
# elif y==0 or x==0:
#     print(3)
# else:
#     print(1,2)

22 # x = int(input())
# y = int(input())
# if x>0 and y>0:
#     print("I chorakka joylashgan")
# if x<0 and y>0:
#     print("II chorakka joylashghan")
# if x<0 and y<0:
#     print("III chorakka joylashgan")
# if x>0 and y<0:
#     print("IV chorakka joylashgan")

23 # x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# x3 = int(input())
# y3 = int(input())
# if x1==x2:
#     x = x3
#     y = y1
#     print(x,y)
# if x2==x3:
#     x = x1
#     y = y3
#     print(x,y)

24 # x = float(input())
# if x>0:
#     print(2*sin(x))
# elif x<=0:
#     print(x-6)

25 # x = int(input())
# if x<-2 or x>2:
#     print(2*x)
# else:
#     print(-3*x)

26 # x = int(input())
# if x<=0:
#     print(-x)
# elif 0<x<2:
#     print(x**2)
# elif x>=2 :
#     print(4)

27 # x = float(input())
# if x<0:
#     print(0)
# elif x%2==1:
#     print(1)
# elif x%2==0:
#     print(-1)

28 # a = int(input())
# if a%4 == 0:
#   if a%100 == 0:
#     if a%400 == 0:
#       print(366)
#     else:
#       print(365)
#   else:
#     print(366)

29 # a = int(input())
# if a%2==1 and a>0:
#     print("Musbat toq")
# elif a%2==1 and a<0:
#     print("Manfiy toq")
# elif a%2==0 and a>0:
#     print("Musbat guft")
# elif a%2==0 and a<0:
#     print("Manfiy gufr")
# elif a==0:
#     print("Nolga teng")

30 # a = int(input())
# if a%2==1 and a>9 and a<100:
#     print("Ikkixonali toq")
# elif a%2==1 and a>99 and a<1000:
#     print("Uchxonali toq")
# elif a%2==0 and a>9 and a<100:
#     print("Ikkixonali guft")
# elif a%2==0 and a>99 and a<1000:
#     print("Uchxonali guft")
# elif a%2==0 and a>0 and a<10:
#     print("Birxonali guft")
# elif a%2==1 and a>0 and a<10:
#     print("Birxonali toq")