def fact(n):
  sum =1
  for i in range(1, n+1):
    sum *= i
  return sum

n=int(input("Enter the number :: "))
print(fact(n))