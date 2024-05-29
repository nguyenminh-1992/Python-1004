class class1004():
    def inthongtin(self):
        print("Lop 1004")

class class1005():
    def inthongtin(self):
        print("Lop 1005")


def kiemtra(sv):
    sv.inthongtin()

sv1 = class1004()
sv2 = class1005()
kiemtra(sv1)
#sv1.inthongtin
kiemtra(sv2)
#sv2.inthongtin