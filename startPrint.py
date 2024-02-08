'''
1. 
1 2 3 
4 5 6
7 8 9

2.
1
1 2
1 2 3
1 2 3 4

3.
1
2 3
4 5 6
7 8 9 10 

4. 
   1
  2 3
 4 5 6
7 8 9 10

5.
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
'''
#  1
for i in range(1, 10,3):
  for j in range(i, i+3):
    print(j, end=" ")
  print()

print()
# 2
for i in range(1, 5):
  for j in range(1, i+1):
    print(j, end=" ")
  print()

# 3
number =1
for i in range(5):
   for j in range(i):
      print(number,end=" ")
      number +=1
   print()

print()
# 4
n=4
number = 1
for i in range(1,n+1):
  for j in range(n-i):
    print(end=" ")
  for k in range(1, i+1):
    print(number, end=" ")
    number=number+1
  print()

print()
# 5
n=5
for i in range(n,0,-1):
  num=i
  for j in range(0,i):
    print(num, end=" ")
  print("\r")

