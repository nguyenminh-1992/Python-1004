#Bkacad (name, age, country)
#1004, 1005, 1006, 1007,... (malop, startdate)
class person():
    def __init__(self,name, age, country):
        self.ten = name   #minh
        self.tuoi = age
        self.quequan = country
    def eat(self):
        print("Eat dinner")
    def __sport(self):
        print("Play sport")

class bkacad():
    def __init__(self,name, age, country):
        self.ten = name   
        self.tuoi = age
        self.quequan = country
    def study(self):
        print("Study python")
    def eat(self):
        print("Eat breakfast")

class python1004(bkacad, person):  #python kế thừa từ cha -> bkacad
    def __init__(self,name, age, country):
        self.ten = name   
        self.tuoi = age
        self.quequan = country    

sv1 = python1004("Minh",20,"HN")
sv1.study()
sv1.eat()