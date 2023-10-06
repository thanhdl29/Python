#ex1: Tính
a = float(input('Nhap so thu nhat:'))
b = float(input('Nhap so thu hai:'))
tong = a+b
print('tong la: ' +str(tong))
thuong=a/b
print('thuong la: '+ str(thuong))
luythua= a**b
print(str(a)+ ' ^ '+ str(b) +'la: ' + str(luythua))

#ex2: Tính diện tích hình chữ tròn khi biết bán kính
from math import pi
r = float(input('Nhap ban kinh: '))
print('dien tich la:' +str(r**2*pi))

#ex3: Xuất tất cả các số nguyên tố trong 1 khoảng cho trước
import math 
def KT_SoNguyenTo (n):
    if n ==1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i ==0:
            return False
    return True
def LietKe_SNT(a, b):
   for i in range(a, b + 1):
       if KT_SoNguyenTo(i):
           print(i, end=' ')
          
a = int(input('Nhap so thu nhat: '))
b = int(input('Nhap so thu hai: '))
if a > b:
    print('So thu nhat phai lon hon so thu 2')
else:
    LietKe_SNT(a, b)

#ex4: Kiểm tra 1 số nguyên n có phải là số Fibonacci hay không
import math
num=int(input("Nhap so can kiem tra\n"))
temp= 1
k= 0
a= 0
summ =0
while summ <= num:
    summ = temp + k
    temp = summ
    k = temp
    if summ == num:
        a = a+1
        print("{} la so fibonnaci".format(num))
        break
if a == 0:
    print("{} khong la so fibonnaci".format(num))

# Tìm số Fibonacci thứ n (dùng đệ quy và không đệ quy)
# đệ quy
def fibonacci(n):      
    if (n == 0 or n == 1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
n = int(input('nhap so thu tu trong day:'))
print('so o thu tu ' +str(n)+' la: ' +str(fibonacci(n)))
#không đệ quy
def fibonacci(m):
    f0 = 0
    f1 = 1
    fn = 1
    if (m < 0):
        return -1
    elif (m == 0 or m == 1):
        return m
    else:
        for i in range(2, m):
            f0 = f1
            f1 = fn
            fn = f0 + f1
        return fn
m = int(input('nhap so thu tu trong day:'))
print(fibonacci(m))
#ex6: Tính tổng n số Fibonacci đầu tiên (dùng đệ quy và không đệ quy)

#ex7: Tính tổng căn bậc 2 của n số nguyên đầu tiên
import math
n= int(input('nhap vao so n:'))
sum=0
for i in range(0,n+1):
    sum +=i
    print('tong can bac 2 la: ')
    print(math.sqrt(sum))
#ex8: Giải phương trình bậc 2: ax2 + bx + c=0
def giaiPTBac2(a, b, c):
    # kiem tra he so nhap vao
    if (a == 0):
        if (b == 0):
            print ("phuong trinh vo nghiem")
        else:
            print ("phuong trinh co mot nghiem x = ", + (-c / b))
        return 
    # tinh delta
    delta = b * b - 4 * a * c
    # tinh nghiem
    if (delta > 0):
        x1 = (float)((-b + math.sqrt(delta)) / (2 * a))
        x2 = (float)((-b - math.sqrt(delta)) / (2 * a))
        print ("phuong trinh co 2 nghiem x1 = ", x1, " va x2 = ", x2)
    elif (delta == 0):
        x1 = (-b / (2 * a))
        print("phuong trinh co nghiem kep x1 = x2 = ", x1)
    else:
        print("phuong trinh vo nghiem")
 
a = float(input("Nhập so thu nhat, a = "))
b = float(input("Nhập so thu hai, b = "))
c = float(input("Nhập so thu 3(hang so tu do), c = "))
giaiPTBac2(a, b, c)
#ex9: Tính n!
def GiaiThua(n):
    if n == 1:
        return n
    return n * GiaiThua(n-1)
n= int(input('nhap vao so n:'))
print(GiaiThua(n))   
#ex10: In * dạng tam giác dưới như hình bên, đầu vào là số hàng(cột)
n=int(input("nhap vao so hang: "))
print("Tam giac vuong can:")
print("*")
for i in range(1,n-1):
    print("*",end='')
    print((i-1)*" ","*")
print('*'+ (n-1)*"*"+'*')
#ex11: Đổi giờ - phút – giây
from datetime import datetime, timedelta
sec = timedelta(seconds=(int(input('Nhap so giay(s): '))))
print(sec)
time = str(sec)
print('gio-phut-giay la: ' + time)
#ex12: Cho một mảng số nguyên:
#a. Xuât tất cả các số lẻ không chia hết cho 5
#cach 1:
def KTChanLe(num):
    if num%2 != 0:
        return 1
    return 0
def KTChiaHetCho5(num):
    if num%5 == 0:
        return 0
    return 1
mylist = [6,13,8,2,1,26,7,5,19,15,20]
for num in mylist:
    if KTChanLe(num) & KTChiaHetCho5(num) == True:
        print('so le khong chia het cho 5 la: '+ str(num))
#cach 2:
event_list =list(filter(lambda x:(x%5 !=0)&(x&1==1),mylist))
print('so le khong chia het cho 5 la: ')
print(event_list)
#==========================================
#b. Xuất tất cả các số Fibonacci
def fibonacci(x):
    if x == 0:
        return x
    return fibonacci(x-1) + fibonacci(x-2)
#==========================================
#c. Tìm số nguyên tố lớn nhất
def SNT_Max(n):
    numlist = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            numlist.append(d)  
            n /= d
        d += 1
    if n > 1:
       numlist.append(n)
    return numlist
print ("mang nguyen to: ", SNT_Max(28))
print ("so nguyen to lon nhat trong mang: ", max(SNT_Max(28)))
#==========================================
#d. Tìm số Fibonacci bé nhất
import math
def calcFiboTerms(fiboTerms, K):
    i = 3
    fiboTerms.append(0)
    fiboTerms.append(1)
    fiboTerms.append(1)
    while True:
        nextTerm = (fiboTerms[i - 1] +
                    fiboTerms[i - 2])
        if nextTerm > K:
            return 
        fiboTerms.append(nextTerm)
        i += 1 

def findMinTerms(K):
    fiboTerms = []
    calcFiboTerms(fiboTerms, K)
    while K > 0:
        count += K // fiboTerms[j]
        K %= fiboTerms[j] 
        j -= 1     
    return count
K = 17
print(findMinTerms(K))
#==========================================
#e. Tính trung bình cộng của các số lẻ
list = [6,13,8,2,1,26,7,5,19]
s=0
for x in list:
    if x%2 !=0:
        s+=x
print('trung binh cua cong cac so le la: '+str(s/2))
#==========================================
#f. Tính tích các phần tử là số lẻ không chia hết cho 3 trong mảng
#==========================================
#g. Đổi chỗ 2 phần tử của danh sách
a=[2,7]
print (a[::-1]) 
print (list(reversed(a))) 
#==========================================
#h. Đảo ngược trật tự các phần tử của danh sách
orinary_list = [1, 2, 3, 4, 5]
orinary_list.reverse()
print(orinary_list)
#==========================================
#i. Xuất tất cả các số lớn thứ nhì của danh sách
def Find_max_second(a):
    max_1 = max(a[0], a[1])
    max_2 = min(a[0], a[1])
    for i in range(2, len(a)):
        if a[i] > max_1:
            max_2 = max_1
            max_1 = a[i]
        elif (a[i] > max_2) and (max_1 != a[i]):
            max_2 = a[i]
    return max_2

n = int(input("Nhap vao so phan tu cua danh sach: "))
a = []
for i in range(n):
    print("\tPhan tu thu", i+1,"la:", end=" ")
    a.append(int(input()))

print("Danh sach vua nhap la:")
for i in range(n):
    print("\t", a[i], end="")
print("\nPhan tu lon thu hai trong danh sach tren la:", Find_max_second(a))
# #==========================================
#j. Tính tổng các chữ số của tất cả các số trong danh sách
num_list = [2,-4,3.5,8,17,33,5,-9,2.3]
tong = sum(num_list)
print('tong cac phan tu cua danh sach la:'+str(tong))
# #==========================================
#k. Đếm số lần xuất hiện của một số trong danh sách
import collections
l = [1,2,3,1,2,4,5,2,7,9,1,7,121,1,6,3,0]
c = collections.Counter(l)
print('so lan xuat hien cua phan tu 1 la: ')
print(c[1])
# #==========================================
#l. Xuất các số xuất hiện n lần trong danh sách
l = [1,2,3,1,2,4,5,2,7,9,1,7,121,1,6,3,0]
c = collections.Counter(l)
print('so lan xuat hien cua cac phan tu la: ')
print(c)
#m. Xuất các số xuất hiện nhiều lần nhất trong danh sách
a = [1,2,2,3,3,3,4,4,4,4]
b = []
c= []
for i in range(len(a)-1): 
    b.append(a.count(a[i]))

for i in range(len(b)-1):
    if b[i] == max(b):
        c.append(a[i])

print('gia tri xuat hien nhieu nhat = ',c[0])