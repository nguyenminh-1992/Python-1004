from classdinhnghia import *

class congty1004:
    listnhanvien = []

    def themnhanvien(self):
        print("1. Can bo")
        print("2. Truong phong")
        print("3. Giam doc")
        nhap = int(input("Chon loai nhan vien: "))
        if nhap==1:
            manv = "CB"
        elif nhap==2:
            manv = "TP"
        elif nhap ==3:
            manv = "GD"
        else:
            print("Khong dung vui long nhap lai")
 # CB1, TP1, TP2, CB2, CB3, CB4, GD1, GD2
 # CB1     
        n = 1
        id = manv + str(n)
        for i in self.listnhanvien:
            if (i.id == id):
                n+=1
                id = manv + str(n)
    
        #CB, TP, GD
        ten = input("Nhap ten: ")
        tuoi = int(input("Nhap tuoi: "))
        quequan = input("Nhap que quan: ")
        ngaycong = int(input("So ngay cong: "))      
        if manv=="CB":
            luong = ngaycong * 100000
        elif manv=="TP":
            luong = ngaycong * 200000
        else:
            luong = ngaycong * 300000
        nhanvien = classchung(ten,tuoi,quequan,ngaycong)
        nhanvien.id = id
        nhanvien.luong = luong
        self.listnhanvien.append(nhanvien)

    def hienthinhanvien(self):
        print("{:<15}{:<15}{:<10}{:<15}{:<10}{:<15}".format("ID","Ten","Tuoi","Quequan","Ngay cong","Luong"))
        for i in self.listnhanvien:
            print("{:<15}{:<15}{:<10}{:<15}{:<10}{:<15}".format(i.id,i.ten,i.tuoi,i.quequan,i.ngaycong,i.luong))

