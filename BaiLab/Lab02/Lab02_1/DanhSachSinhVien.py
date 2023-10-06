

from datetime import date, datetime

from SinhVien import SinhVien


class DanhSachSV:
    def __init__(self) -> None:
        self.dssv = []

    def themSinhVien(self, sv: SinhVien):
        self.dssv.append(sv)

    def xuat(self):
        for sv in self.dssv:
            print(sv)

    # tìm sing vien theo mssv, nếu có trả về sinh viên
    def timSVTheoMssv(self, mssv: int):
        return [sv for sv in self.dssv if sv.maSo==mssv]
    # xoá sinh vien có mã số mssv, thông báo xoá đc hoặc ko

    def xoaSvTheoMssv(self, maSo: int) -> bool:
        vt = self.timSVTheoMssv(maSo)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False

    # tìm sinh viên tên Nam
    def timSvTheoTen(self, ten: str):
        return [sv for sv in self.dssv if sv.hoTen.split(' ')[-1].lower() == ten.lower()]

    # tìm những sinh viên sinh trước 15/6/2000
    def timSvSinhTruocNgay(self, ngay: datetime):
        return [sv for sv in self.dssv if sv.ngaySinh < ngay]


# dssv = DanhSachSV()
# sv1 = SinhVien(2015795, "Lê Đại Hải Nam",
#                datetime.strptime("21/7/1998", "%d/%m/%Y"))
# sv2 = SinhVien(2015794, "Nguyễn Hoàng Nhật Tiến",
#                datetime.strptime("10/06/2002", "%d/%m/%Y"))
# sv3 = SinhVien(2015796, "Trần Trung Hiếu",
#                datetime.strptime("8/4/2001", "%d/%m/%Y"))
# sv4 = SinhVien(2015797, "Hoàng Anh",
#                datetime.strptime("10/06/2000", "%d/%m/%Y"))
# sv5 = SinhVien(2015798, "Trần Minh Hiếu",
#                datetime.strptime("8/4/2000", "%d/%m/%Y"))
# dssv.themSinhVien(sv1)
# dssv.themSinhVien(sv2)
# dssv.themSinhVien(sv3)
# dssv.themSinhVien(sv4)
# dssv.themSinhVien(sv5)
# dssv.xuat()

# ten = "Nam"
# mang = dssv.timSvTheoTen(ten)
# print(f"Các sv tên {ten} là:")
# for i in mang:
#     i.xuat()

# ngay = datetime.strptime("15/6/2000", "%d/%m/%Y")
# mang = dssv.timSvSinhTruocNgay(ngay)
# print(f"Các sv sinh trước ngày {ngay} là:")
# for i in mang:
#     i.xuat()
    
# mssv = int(input("Nhập mã số sinh viên cần tìm: "))
# tim = dssv.timSVTheoMssv(mssv)
# print(f"Tìm sinh viên theo mã: {mssv}")
# for i in tim:
#     i.xuat()
