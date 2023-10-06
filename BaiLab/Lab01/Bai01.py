#ex1: Write a Python program to print 
# the following string in a specific format
a = """Twinkle, twinkle, little star, 
            How I wonder what you are! 
                Up above the world so high,
                Like a diamond in the sky.
        Twinkle, twinkle, little star,
            How I wonder what you are"""
print(a)
#ex2: Write a Python program to get 
# the Python version you are using
import sys
print("Python version: " + sys.version)
#ex3: Write a Python program to display 
# the current date and time.
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
#ex4: Write a Python program which accepts 
# the radius of a circle from the user and compute the area.
from math import pi
r = float(input('Nhap ban kinh: '))
print('dien tich la:' +str(r**2*pi))
#ex5:Write a Python program which 
# accepts the user's first and last name and print
#  them in reverse order with a space between them.
firstName = input('Nhap ho: ')
lastName = input('Nhap ten: ')
print('Ten ban la'+lastName + ' '+ firstName)
#ex6 Write a Python program which accepts a 
# sequence of comma-separated numbers from user 
# and generate a list and a tuple with those numbers
# li ='%s' %(['3','5','7','23']) #kieu du lieu list
# tup = '%r' %(('3','5','7','23')) #kieu du lieu tuple
# print(li)
# print(tup)
#ex7: rite a Python program to accept a filename
#  from the user and print the extension of that
filename = input("Filename: ")
file = filename.split(".")
print ("duoi file la : " + str(file[-1]))
#ex8:  Write a Python program to display the first
#  and last colors from the following list
color_list = ["Red","Green","White" ,"Black"]
print( "%s %s"%(color_list[0],color_list[-1]))
#ex9:Write a Python program to display the examination
#  schedule. (extract the date from exam_st_date)
exam_st_date = (11, 12, 2014)
print(' The examination will start from :%i/%i/%i' %exam_st_date)
#ex10: Write a Python program that accepts an 
# integer (n) and computes the value of n+nn+nnn 
a = int(input("Nhap so nguyen: "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print('tong n+nn+nnn la: '+n1+n2+n3)
#ex12: Write a Python program to print 
#the calendar of a given month and year.
import calendar
m = int(input("Nhap thang : "))
y = int(input("Nhap nam : "))
print(calendar.month(y, m))
#ex14: Write a Python program to calculate number of days between two dates
from datetime import date
NgayDau = date(2014, 7, 2)
NgayCuoi = date(2014, 7, 11)
delta = NgayCuoi - NgayDau
print(delta.days)
#ex15: Write a Python program to get the
# volume of a sphere with radius 6
r= 6
v = 4/3*pi*(r**3)
print('the tich hinh cau la: ' + str(v))
#ex16: Write a Python program to get the 
# difference between a given number and 17,
#  if the number is greater than 17 return
#  double the absolute difference
def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2 
print(difference(100))
print(difference(9))
#ex17:  Write a Python program to test whether
#  a number is within 100 of 1000 or 2000
def near_thousand(n):
    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))   
print(near_thousand(2200))
#ex18: Write a Python program to calculate
#  the sum of three given numbers, if the
#  values are equal then return three times 
# of their sum.
def tongBaSo(x, y, z):
    tong = x + y + z  
    if x == y == z:
        tong = tong * 3
    return tong
print(tongBaSo(9,2,16))
print(tongBaSo(2,2,2))
#ex20: Write a Python program to get a 
# string which is n (non-negative integer) 
# copies of a given string.
def larger_string(str, n):
   result = ""
   for i in range(n):
      result = result + str
   return result

print(larger_string('abc', 2))
print(larger_string('.py', 3))

#ex21:  Write a Python program to find 
# whether a given number (accept from the user)
#  is even or odd, print out an appropriate 
# message to the user
num = int(input("Nhap so: "))
if (num % 2) == 0:
   print("{0} la so chan".format(num))
else:
   print("{0} la so le".format(num))
#ex22: Write a Python program to count the 
# number 4 in a given list
def list_count_4(nums):
  count = 0  
  for num in nums:
    if num == 4:
      count = count + 1

  return count

print(list_count_4([1, 4, 6, 7, 4]))
print(list_count_4([1, 4, 6, 4, 7, 4]))
#ex24:  Write a Python program to test whether
#  a passed letter is a vowel or not
def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels
print(is_vowel('c'))
print(is_vowel('e'))
#ex25: 
def is_group_member(group_data, n):
   for value in group_data:
       if n == value:
           return True
   return False
print(is_group_member([1, 5, 8, 3], 3))
print(is_group_member([5, 8, 3], -1))



