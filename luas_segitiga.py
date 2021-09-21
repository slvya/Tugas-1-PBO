class Segitiga():
    def __init__(self,a,t):
         self.alas = a
         self.tinggi = t
    def  hitungluas(self):
        return 0.5 * self.alas * self.tinggi

def main():
        s = Segitiga(4, 8)
        print('panjang alas segitiga adalah\t:',s.alas)
        print('tinggi segitiga adalah\t:',s.tinggi)

        print('Luas Segitiga adalah\t:',s.hitungluas())
main()