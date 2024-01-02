'''
1.

   1
  2 3
 4 5 6
7 8 9 10

2.

* * * * * 
 * * * * 
  * * * 
   * * 
    * 

3.

55555
4444
333
22
1

4.

1 2 3
4 5 6
7 8 9

5.

1
2 3
4 5 6

6.

* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *

7.

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

# 8. 
# 1 2 3 
# 4 5 6
# 7 8 9

9. 
* * * * *
* * * *
* * *
* * 
*

10.
*
* *
* * *
* * * *

11.
1
2 3
4 5 6
7 8 9 10

12.
    *
   ***
  *****
 *******
*********

13. 
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *

14.

7 7 7 7 7 7 7
6 6 6 6 6 6
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
'''

# for input 
num=int(input("Enter the number :: "))


n=4
print(n)
number=1
for i in range(1,n+1):
    for j in range(n-i):
        print(end=" ")
    for k in range(1,i+1):
        print(number, end=" ")
        number=number+1
    print()


n=5
print(n)
for i in range(n,0,-1):
    for j in range(n-i):
        print(end=" ")
    print('* '*i)


n=5
for i in range(n,0,-1):
    print(f'{i}'*i)


for i in range(1, 10, 3):
    for j in range(i, i + 3):
        print(j, end=" ")
    print()


num = 1
n = 3
for i in range(n):
    for j in range(i + 1):
        print(num, end=" ")
        num +=1
    print()



for i in range(num):
    for j in range(num+1):
        print("*", end=" ")
    print()
print()

 
for i in range(1,num+1):
  for j in range(1,i+1):
    print(j,end=" ")
  print()

print()
# 2.
for i in range(1,num+1):
  for j in range(1,num+1):
    print(j, end=" ")
  print()

print()
# 3.
for i in range(1, num + 1):
    for j in range((i - 1) * num + 1, i * num + 1):
        print(j, end=" ")
    print()  # Move to the next line after each row is printed

print()
# 4.
for i in range(num):
    for j in range(num-i):
       print("*",end=" ")
    print()

print()

5.

for i in range(num):
   for j in range(i+1):
      print("*",end=" ")
   print()

print()

6.
number =1
for i in range(num):
   for j in range(i):
      print(number,end=" ")
      number +=1
   print()

print()

# 7.
for i in range(1, num+1):
   print(" " *(num-i)+ "*" *(2*i-1))

n = 6
for i in range(n):
    for j in range(i-1):
        print(" ", end="")
print("*")

# 8.
for i in range(num):
    for j in range(num - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        print('*', end='')
    print()
for i in range(num - 1):
    for j in range(i + 1):
        print(' ', end='')
    for j in range(2*(num - i - 1) - 1):
        print('*', end='')
    print()

print()

for i in range (num, 0, -1):  
    num1 = i  
    for j in range(0, i):  
        print(num1, end=' ')  
    print("\r")
print()