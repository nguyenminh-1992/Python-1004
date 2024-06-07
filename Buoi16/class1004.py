from classdinhnghia import classchung

class class1004:
    listclass1004 = [] #hocvien()

    def themhocvien(self):
        stt = self.listclass1004.__len__() + 1
        ten = input("Nhap ten: ")
        tuoi = int(input("Nhap tuoi: "))
        quequan = input("Nhap que quan: ")
        lop = int(input("Nhap lop: "))
        tienganh = int(input("Nhap diem tieng anh: "))
        tinhoc = int(input("Nhap diem tin hoc: "))
        diemtrungbinh = float((tinhoc+tienganh)/2)
        hocvien = classchung(ten,tuoi,quequan,lop,tienganh,tinhoc)
        hocvien.stt = stt
        if diemtrungbinh>5:
            hocvien.xeploai = "PASS"
        else:
            hocvien.xeploai = "FAILED"
        self.listclass1004.append(hocvien)

    def hienthihocvien(self):
        print("{:<15}{:<15}{:<10}{:<15}{:<10}{:<15}{:<15}{:<15}".format("STT","Ten","Tuoi","Quequan","Lop","TiengAnh","Tinhoc","Xeploai"))
        for i in self.listclass1004:
            print("{:<15}{:<15}{:<10}{:<15}{:<10}{:<15}{:<15}{:<15}".format(i.stt,i.ten,i.tuoi,i.quequan,i.lop,i.tienganh,i.tinhoc,i.xeploai))
    
    def xoahocvien(self,sttcantim):
        for i in self.listclass1004:
            if(i.stt == sttcantim):
                print("Da tim thay hoc vien")
                self.listclass1004.remove(i)
                print("Da xoa hoc vien")
            else:
                print("Khong tim thay hoc vien")
    
    def suahocvien(self,sttcantim):
        for i in self.listclass1004:
            if(i.stt == sttcantim):
                print("Da tim thay hoc vien")
                i.ten = input("Nhap ten muon sua: ")
                i.tuoi = int(input("Nhap tuoi muon sua: "))
            else:
                print("Khong tim thay hoc vien")
    #tim kiem:

#test = class1004()
#test.themhocvien()
#test.hienthihocvien()


