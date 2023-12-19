num=int(input("Enter the number :: ")) 
sum =0
temp=num
while(temp >0):
  digit = temp %10
  sum +=digit**3
  temp //=10
if num == sum:
  print("{0} is a Armstrong number ".format(num))
else:
  print("{0} is not a Armstrong number ".format(num))