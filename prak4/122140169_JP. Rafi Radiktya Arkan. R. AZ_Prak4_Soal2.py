import math

class BangunDatar:
    def hitungLuas(self):
        pass
    
class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi
    
    def hitungLuas(self):
        return self.sisi ** 2
        
class Lingkaran(BangunDatar):
    def __init__(self, radius):
        self.radius = radius
    
    def hitungLuas(self):
        return math.pi * self.radius ** 2
        
persegi = Persegi(5)
lingkaran = Lingkaran(3)

print(f"Luas Persegi: {persegi.hitungLuas()}")
print(f"Luas Lingkaran: {lingkaran.hitungLuas()}")
