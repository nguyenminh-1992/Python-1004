from classdinhnghia import classchung

class class1004:
    listclass1004 = []

    def themhocvien(self):
        ten = input("Nhap ten: ")
        tuoi = int(input("Nhap tuoi: "))
        quequan = input("Nhap que quan: ")
        lop = int(input("Nhap lop: "))
        tienganh = int(input("Nhap diem tieng anh: "))
        tinhoc = int(input("Nhap diem tin hoc: "))
        
        hocvien = classchung(ten,tuoi,quequan,lop,tienganh,tinhoc)
        self.listclass1004.append(hocvien)

    def hienthihocvien(self):
        print("{:<15}{:<10}{:<15}{:<10}{:<15}{:<15}".format("Ten","Tuoi","Quequan","Lop","TiengAnh","Tinhoc"))
        for i in self.listclass1004:
            print("{:<15}{:<10}{:<15}{:<10}{:<15}{:<15}".format(i.ten,i.tuoi,i.quequan,i.lop,i.tienganh,i.tinhoc))
    
    #tim kiem:

#test = class1004()
#test.themhocvien()
#test.hienthihocvien()
