class Bkacad():
    __name = "Bkacad"
    def exam(self):
        print("Bat buoc phai thi")
    def __tinhluong(self):
        print("Phai tinh luong")

class python1004(Bkacad):  #Đơn kế thừa
    pass

class python1005(Bkacad):  #Đa kế thừa
    clazz = "BKCad"
    def __init__(self,name,age):
        self.ten = name
        self.tuoi = age
# __init__ : magic method (Google)
std1004 = python1004()      
std1005 = python1005("minh",21)

std1004.exam()
#std1005.__tinhluong()

dt = Bkacad()
print(dt.__name)
print(std1005.clazz)
print(std1005.ten)
print(std1005.tuoi)

#Định nghĩa
#Khởi tạo
#Test