num=11
if num > 1:
  for i in range(2,int(num/2)+1):
    if num % i ==0:
      print("Not a prime number")
      break
  else:
    print("{0} is prime number :: ".format(num))
else:
  print("is not a prime number :: ")
