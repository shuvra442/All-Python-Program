def swap(n1,n2):
  # n1,n2=n2,n1
  return n2,n1

n1=int(input("Enter the number of n1 :: "))
n2=int(input("Enter the number of n2 :: "))
print("Before the swap the number is {0} {1}".format(n1,n2))
n1,n2=swap(n1,n2)
print("After the swap the number is {0} {1}" .format(n1,n2))
