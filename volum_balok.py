class Balok():
    def __init__(self,p,l,t):
         self.panjang = p
         self.lebar = l
         self.tinggi = t
    def  hitungVolume(self):
        return self.panjang * self.lebar * self.tinggi

def main():
        b = Balok(10, 4, 3)
        print('panjang balok adalah\t:',b.panjang)
        print('lebar balok adalah\t:',b.lebar)
        print('Tinggi balok adalah\t:',b.tinggi)
        print('Volume balok adalah\t:',b.hitungVolume())
main() 