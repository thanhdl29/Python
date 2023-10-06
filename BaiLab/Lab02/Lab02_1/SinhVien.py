

import datetime


class SinhVien:
    # Biến của lớp, chung cho tất cả đối tương thuộc lớp
    truong = "Đại học Đà Lạt"
    # Hàm khởi tạo, hàm tạo lập:Khởi gán các thuộc tính của đối tuọng

    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime) -> None:
        self.__maSo = maSo  # thuộc tính private
        self.__hoTen = hoTen  # thuộc tính private
        self.__ngaySinh = ngaySinh

    # cho phép truy suất tới thuộc tính từ bên ngoài thông qua trường mSo

    @property
    def maSo(self):
        return self.__maSo

    @property
    def hoTen(self):
        return self.__hoTen

    @property
    def ngaySinh(self):
        return self.__ngaySinh

    # cho phép thay đooir giá trị thuộc tính maSo
    @maSo.setter
    def maSo(self, maSo):
        if self.laMaSoHopLe(maSo):
            self.__maSo = maSo
    # phương thức tĩnh: các phương thức không truy xuất gì đến thuộc tính, hành vi của lớp
    # những phương thức này không cần truyền tham số mặc định self
    # Đây không phải là một hành vi (Phương thức) của 1 đối tượng thuộc lớp

    @staticmethod
    def laMaSoHopLe(maSo: int):
        return len(str(maSo)) == 7

    # phương thức cuẩ lớp, chỉ truy xuất tới các biến thành viên của lớp
    # Kông truy xuất được các thuộc tính riêng của đối tượng
    @classmethod
    def doiTenTruong(self, tenmoi):
        self.truong = tenmoi
    

    # Tuong tự ghi đè phương thức toString()

    def __str__(self) -> str:
        return f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}"

    # Hành vi của đối tượng sinh viên
    def xuat(self):
        print(f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}")

# f = open("DanhSachSinhVien.txt", "r")
# print(f.read())
