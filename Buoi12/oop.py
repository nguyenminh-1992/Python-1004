# O O P
# Object Oriented Programming (Lập trình HƯỚNG đối tượng)
#1. Kế thừa
#2. Đóng gói
#3. Tính đa hình
#4. Tính trừu tượng

#Quản lý lớp (thông tin về lớp, tính chất của lớp)
#Định nghĩa về lớp: có các sinh viên. 
#Sinh viên (tên, tuổi, quê quán,...)
#Sinh viên (học, thi, chơi, ăn, ngủ,..)

class Python1004():
#Thuộc tính: Tên, tuổi, quê quán,...
#Phương thức: Ăn, học, thi, chơi,...
    #Định nghĩa về khai báo
    def __init__(self,name, age, country):
        self.ten = name
        self.tuoi = age
        self.quequan = country
    #sv1 (ten, tuoi, quequan), sv2, sv3
    def hocpython(self):
        print("Phai hoc du 40h python")
    def play(self):
        print("Sau khi hoc xong se duoc choi")
    def time(self):
        print("Thoi gian hoc bat dau tu 19h30")

sv1 = Python1004("Minh",20,"HN")
#sv1.ten = minh
sv2 = Python1004("Hai",21,"HN1")
sv3 = Python1004("Tran",22,"HN2")

#print(sv1.quequan)
#print(sv2.ten)
#print(sv3.ten)

#sv1.hocpython()

#Tự định nghĩa 1 class
#Nhập tay để thêm các thành viên trong class
#Nhập số đối tượng, thêm các thuộc tính
#In ra danh sách các đối tượng sau khi nhập
#Minh - 20 - HN
mangloppython1004 = []
soluong = int(input("Nhap so luong: "))
for i in range(soluong):
    ten = input("Nhap ten: ")
    tuoi = int(input("Nhap tuoi:"))
    quequan = input("Nhap que quan: ")
    sv = Python1004(ten,tuoi,quequan)
    mangloppython1004.append(sv)
for j in mangloppython1004:
    print('{} - {} - {}'.format(j.ten,j.tuoi,j.quequan))
