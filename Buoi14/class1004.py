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
    
    def intthocvien(self):
        print("{} - {}".format(self.listclass1004[0].ten, self.listclass1004[0].tuoi))


test = class1004()
test.themhocvien()
test.intthocvien()