year=int(input("Enter the year :: "))
if(year%400==0 or year %100 !=0 and year %4 ==0):
  print("{0} is a leap year".format(year))
else:
  print("%d is not a leap year" %year)