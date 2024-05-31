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
        test.themhocvien
    elif nhap==2:
        test.hienthihocvien
    elif nhap==3:
        print("Xoa hoc vien")
    elif nhap==4:
        print("Sua hoc vien")
    elif nhap==0:
        print("Goodbye")
        break
    else:
        print("Nhap sai vui long nhap lai")

    




