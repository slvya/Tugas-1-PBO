class segitiga:
    def __init__(self,tinggi):
        self.tinggi = tinggi
    def GambarSegitiga(self):
        t= self.tinggi
        a = ""
        i = 0
        while(i<t):
            j = t 
            u = 0
            while(j>i):
                a += '*'
                j-=1
            i+=1
            a += '\n'
        print(a)

a=segitiga(5)
a.GambarSegitiga()