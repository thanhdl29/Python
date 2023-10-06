class PhanSo:
    def __init__(self, tu=0, mau=1):
        self.__tu = tu
        self.__mau = mau

    @property
    def tu(self):
        return self.__tu

    @tu.setter
    def tu(self, tu):
        self.__tu = tu

    @property
    def mau(self):
        return self.__mau

    @mau.setter
    def mau(self, mau):
        if(mau != 0):
            self.__mau = mau
        else:
            print("Mẫu số không hợp lệ!")

    def xuat(self):
        print(f"{str(self.tu)}\{str(self.mau)}")

    def __str__(self) -> str:
        return "{}/{}".format(self.__tu,self.__mau)

    @staticmethod
    # Dùng @staticmethod để self không được truyền mặc định vào tham số của hàm
    def __TimUCLN(a, b):
        while a != b:
            if a > b:
                a -=b
            else:
                b -= a
        return a

    def RutGon(self):
        ucln = self.__TimUCLN(self.tu, self.mau)
        self.tu /= ucln
        self.mau /= ucln

    def __add__(self, other):
        '''Cộng 2 phân số ps1 + ps2'''
        kq = PhanSo()
        kq.tu = self.tu * other.mau + self.mau * other.tu
        kq.mau = self.mau * other.mau
        kq.RutGon()
        return kq

    def __sub__(self, other):
        '''Trừ 2 phân số ps1 - ps2'''
        kq = PhanSo()
        kq.tu = self.tu * other.mau - self.mau * other.tu
        kq.mau = self.mau * other.mau
        kq.RutGon()
        return kq
    #Nhân quy 2 số âm
    def __multiadd__(self, orther):
        if self.mau == orther.mau:
            self.tu = int(self.tu) + int(orther.tu)
            self.mau = int(self.mau)
            self.RutGon()
        else:
            self.mau = int(self.mau)*int(orther.mau)
            self.tu = int(self.tu)*int(orther.mau) + int(self.mau)*int(orther.tu)
            self.RutGon()
        return self

    def __mul__(self, other):
        '''Nhân 2 phân số ps1 * ps2'''
        kq = PhanSo()
        kq.tu = self.tu *  other.tu
        kq.mau = self.mau * other.mau
        kq.RutGon()
        return kq

    def __truediv__(self, other):
        '''Chia 2 phân số ps1 / ps2'''
        kq = PhanSo()
        kq.tu = self.tu *  other.mau
        kq.mau = self.mau * other.tu
        kq.RutGon()
        return kq

    def TinhGT(self):
        return self.tu / self.mau

    #Hàm kiểm tra phân số dương
    def KTPSAmDuong(self):
        if (self.tu / self.mau < 0):
            return False
        return True

# a = PhanSo()
# a.tu = 2
# a.mau = 3
# b = PhanSo(3, 6)
# print(f"{a} + {b} = {a+b}")
# print(f"{a} - {b} = {a-b}")
# print(f"{a} * {b} = {a*b}")
# print(f"{a} / {b} = {a/b}")

class DanhSachPhanSo:
    def __init__(self) -> None:
        self.dsps = []

    def ThemPhanSo(self, ps: PhanSo):
        self.dsps.append(ps)

    def xuat(self):
        for ps in self.dsps:
            print(ps)

    #Đếm số phân số âm trong mảng
    def DemPSAm(self):
        dem = 0
        for ps in self.dsps:
            if(int(ps.tu) < 0 or int(ps.mau) < 0):
                dem += 1
        return dem

    def SoSanhPS(self, a :PhanSo, b:PhanSo):
        if(a.TinhGT() == b.TinhGT()):
            return True
        else:
            return False
            # return int(a.tu)*int(b.mau) < (b.tu)*int(a.mau)

    def TimPSDuongNhoNhat(self):
        for ps in self.dsps:
            if (int(ps.tu) > 0 and int(ps.mau) > 0) or (int(ps.tu) < 0 and int(ps.mau) < 0):
                min = ps
                break

        for ps in self.dsps:
            if(int(ps.tu) > 0 and int(ps.mau) > 0) or (int(ps.tu) < 0 and int(ps.mau) < 0):
                if(dsps.SoSanhPS(ps, min)):
                    min = ps
        return min.xuat()

    def SoSanh(self, x: PhanSo, y: PhanSo):
        if(x.mau == y.mau and x.tu == y.tu):
            return True
        return False
    def TimVtPsX(self, x: PhanSo):
        vt = [p for p in range(0, len(self.dsps)) if self.SoSanh(self.dsps[p], x)]
        return vt
    def TongTatCaPSAm(self):
        sum = PhanSo()
        for ps in self.dsps:
            if(int(ps.tu)<0 or int(ps.mau)<0):
                sum.__multiadd__(ps)
        return sum
    def DocTuFile(self, fileName: str):
        f = open(fileName, 'r', encoding="utf8")
        line = f.readline()
        sp = line.split(',')
        for i in sp:
            frac = i.split('/')
            ps = PhanSo()
            ps.tu = frac[0]
            ps.mau = frac[1]
            dsps.ThemPhanSo(ps)
        return dsps.dsps

ps0 = PhanSo(1,2)
ps1 = PhanSo(-1,-20)
ps2 = PhanSo(-2,3)
ps3 = PhanSo(1,2)
ps4 = PhanSo(31,5)
dsps = DanhSachPhanSo()
dsps.ThemPhanSo(ps0)
dsps.ThemPhanSo(ps1)
dsps.ThemPhanSo(ps2)
dsps.ThemPhanSo(ps3)
dsps.ThemPhanSo(ps4)
dsps.xuat()

print("Phân số âm trong danh sách là: ", dsps.DemPSAm())
print("Phân số dương nhỏ nhất là: ")
kq = dsps.TimPSDuongNhoNhat()

ps= PhanSo(1,2)
list =dsps.TimVtPsX(ps)
print("vị trí cần tìm: ")
for i in list:
    print(i+1)
#print(f"Tổng số âm trong danh sách là: {dsps.TongTatCaPSAm()}")

dsps.DocTuFile("phanso.txt")
