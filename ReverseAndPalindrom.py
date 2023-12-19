def reversed(num):
  sum=0
  while num>0:
    temp=num%10
    sum=(sum*10)+temp
    num=num//10
  return sum

num=int(input("Enter the number :: "))
print("Reversed of a number :: ")
n1=reversed(num)
print(n1)
print("Check the original number is palindrom or not :: %d" %num)
if(n1== num):
  print("The given number is Palindrome")
else:
  print("The given number is not palindrome")
