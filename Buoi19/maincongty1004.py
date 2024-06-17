from congty1004 import *
test = congty1004()

while(True):
    print("|------------------------------ |")
    print("|CHUONG TRINH QUAN LY NHAN VIEN |")
    print("|1. Them nhan vien              |")
    print("|2. Hien thi nhan vien          |")
    print("|3. Xoa nhan vien               |")
    print("|4. Sua nhan vien               |")
    print("|0. Thoat                       |")
    print("|------------------------------ |")
    
    nhap = int(input("Nhap chuc nang theo so: "))
    if nhap==1:
        soluong = int(input("Nhap so nhan vien muon nhap: "))
        i = 1
        while (i <= soluong):
            print("Nhap hoc vien thu {}".format(i))
            test.themhocvien()
            i+=1
            print("Da them xong hoc vien thu {}".format(i-1))
        test.hienthihocvien()
    elif nhap==2:
        test.hienthihocvien()
    elif nhap==3:
        stt = int(input("Nhap stt muon xoa: "))
        test.xoahocvien(stt)
    elif nhap==4:
        stt = int(input("Nhap stt muon sua: "))
        test.suahocvien(stt)
    elif nhap==0:
        print("Goodbye")
        break
    else:
        print("Nhap sai vui long nhap lai")
