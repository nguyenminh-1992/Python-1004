from class1004 import *

test = class1004()

while(True):
    print("|------------------------------|")
    print("|CHUONG TRINH QUAN LY HOC VIEN-|")
    print("|1. Them hoc vien              |")
    print("|2. Hien thi hoc vien          |")
    print("|3. Xoa hoc vien               |")
    print("|4. Sua hoc vien               |")
    print("|0. Thoat                      |")
    print("|------------------------------|")
    
    nhap = int(input("Nhap chuc nang theo so: "))
    if nhap==1:
        soluong = int(input("Nhap so hoc vien muon nhap: "))
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
        stt = int(print("Nhap stt muon xoa: "))
        test.xoahocvien(stt)
    elif nhap==4:
        stt = int(print("Nhap stt muon sua: "))
        test.suahocvien(stt)
    elif nhap==0:
        print("Goodbye")
        break
    else:
        print("Nhap sai vui long nhap lai")

    




