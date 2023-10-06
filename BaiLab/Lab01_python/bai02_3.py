import math


def SoNT(n):
    kt = True
    if (n < 2):
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if (n % i == 0):
            kt = False
            break
    return kt


a = int(input("Mời nhập điểm bắt đầu: "))
b = int(input("Mời nhập điểm kết thúc: "))
for n in range(a+1, b):
    kq = SoNT(n)
    if kq == True:
        print(n, end=" ")
