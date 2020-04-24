import sympy as sym
import numpy as num

# DataList
DataBaseKunci = ['GYBNQKURP', 'BAACBACBB']
menu = [1, 2]
menuKunci = [0, 1, 2, 3]

# Matriks
MatrixAwal = [[0] for i in range(3)]
KunciMatrix = [[0] * 3 for i in range(3)]
MatrixAkhir = [[0] for i in range(3)]

# enkripsi
class Enkripsi():
    def __init__(self, awal, Encrypt):
        self.Encrypt = Encrypt
        self.awal = awal

    def NgubahASCII(self):
        k = 0
        for baris in range(3):
            for kolom in range(3):
                KunciMatrix[baris][kolom] = ord(self.Encrypt[k]) % 65
                k += 1
    
    def PerkalianMatrix(self, MatrixAwal):
        for baris in range(3):
            for kolom in range(1):
                MatrixAkhir[baris][kolom] = 0
                for i in range(3):
                    MatrixAkhir[baris][kolom] += KunciMatrix[baris][i] * MatrixAwal[i][kolom]
                MatrixAkhir[baris][kolom] = MatrixAkhir[baris][kolom] % 26
    
    def Hasil(self):
        self.NgubahASCII()
        
        for baris in range(3):
            MatrixAwal[baris][0] = ord(self.awal[baris]) % 65
        
        self.PerkalianMatrix(MatrixAwal)
        
        HasilCipher = []
        for baris in range(3):
            HasilCipher.append(chr(MatrixAkhir[baris][0] + 65))
        print("Hasil Cipher Text: ", ''.join(HasilCipher))

# deskripsi
class Deskripsi():
    def __init__(self, awal, Descrypt):
        self.Descrypt = Descrypt
        self.x = awal

    def NgubahASCII(self):
        k = 0
        for baris in range(3):
            for kolom in range(3):
                KunciMatrix[baris][kolom] = ord(self.Descrypt[k]) % 65
                k += 1
    
    def Invers(self):
        global KunciMatrix
        self.NgubahASCII()
        UbahMatrix = sym.Matrix(KunciMatrix)
        DetMatrix = UbahMatrix.det()
        KofMin = UbahMatrix.adjugate()
        UbahArray = num.array(KofMin)
        KunciMatrix = DetMatrix * UbahArray % 26

    def PerkalianDes(self, MatrixAwal):
        self.Invers()
        for baris in range(3):
            for kolom in range(1):
                MatrixAkhir[baris][kolom] = 0
                for i in range(3):
                    MatrixAkhir[baris][kolom] += (KunciMatrix[baris][i] * MatrixAwal[i][kolom])
                MatrixAkhir[baris][kolom] = MatrixAkhir[baris][kolom] % 26
    
    def Hasil(self):
        self.NgubahASCII()
        
        for baris in range(3):
            MatrixAwal[baris][0] = ord(self.x[baris]) % 65
        
        self.PerkalianDes(MatrixAwal)
        
        HasilCipher = []
        for baris in range(3):
            HasilCipher.append(chr(MatrixAkhir[baris][0] + 65))
        print("Hasil Cipher Text: ", ''.join(HasilCipher))


# Mulai Game
if __name__ == "__main__":
    
    print("========== SELAMAT DATANG DI PROGRAM HILL CIPHER ==========")
    print(">>>>>>> Program Ini Hanya Membuat Kode Dari 3 HUruf <<<<<<<")
    while True:
        
        print('''Choose one
        1. Encryption
        2. Description
        ''')
        while True:
            try:   
                pilih = int(input('jawab : '))

            except:
                print('Ada Kesalahan, Masukkan angka yang benar!!')
                
            else:
                if pilih in menu:    
                    if pilih == 1:
                        while True:
                            masukkan = str(input('Masukkan 3 huruf yang ingin di enskripsi :'))
                            if len(masukkan) == 3:
                                upper = masukkan.upper()
                                print('Pilih Kunci Yang Akan Dipakai')
                                print('\t1. GYBNQKURP\n', '\t2. BAACBACBB\n\n', '\t0. Input Sendiri')
                                while True:
                                    try:
                                        JawabKunci = int(input('Masukkan Pilihan: '))
                                    except:
                                        print('Ada Kesalahan, Masukkan angka yang benar!!')
                                    else:
                                        if JawabKunci in menuKunci:
                                            if JawabKunci == 0:
                                                while True:
                                                    kunci = str(input('Masukkan 9 huruf sebagai kunci enkripsi :'))
                                                    if len(kunci) == 9:
                                                        kata = kunci.upper()
                                                        HasilData = Enkripsi(upper, kata)
                                                        HasilData.Hasil()
                                                        break
                                                    elif len(kunci) < 9:
                                                        print('Huruf yang dimasukkan kurang')
                                                    else:
                                                        print('Masukkan 9 Huruf saja')
                                                break
                                            else:
                                                HasilData = Enkripsi(upper, DataBaseKunci[JawabKunci - 1])
                                                HasilData.Hasil()
                                                break
                                        else:
                                            print('Masukkan pilihan menu yang tepat!!')
                                    # break
                                break
                            elif len(masukkan) < 3:
                                print('Huruf yang dimasukkan kurang')
                            else:
                                print('Masukkan 3 Huruf saja')
                        break

                    elif pilih == 2:
                        while True:
                            masukkan = input('Masukkan 3 huruf yang ingin di deskripsi :')
                            if len(masukkan) == 3:
                                upper = masukkan.upper()
                                print('Pilih Kunci Yang Akan Dipakai')
                                print('\t1. GYBNQKURP\n', '\t2. BAACBACBB\n\n', '\t0. Input Sendiri')
                                while True:
                                    try:
                                        JawabKunci = int(input('Masukkan Pilihan: '))
                                    except:
                                        print('Ada Kesalahan, Masukkan angka yang benar!!')
                                    else:
                                        if JawabKunci in menuKunci:
                                            if JawabKunci == 0:
                                                while True:
                                                    kunci = input('Masukkan 9 huruf sebagai kunci deskripsi :')
                                                    if len(kunci) == 9:
                                                        kata = kunci.upper()
                                                        HasilData = Deskripsi(upper, kata)
                                                        HasilData.Hasil()
                                                        break
                                                    elif len(kunci) < 9:
                                                        print('Huruf yang dimasukkan kurang')
                                                    else:
                                                        print('Masukkan 9 Huruf saja')
                                                break
                                            else:
                                                HasilData = Deskripsi(upper, DataBaseKunci[JawabKunci - 1])
                                                HasilData.Hasil()
                                                break
                                        else:
                                            print('Masukkan pilihan menu yang tepat!!')
                                break
                            elif len(masukkan) < 3:
                                print('Huruf yang dimasukkan kurang')
                            else:
                                print('Masukkan 3 Huruf saja')
                        break
                else:
                    print('Masukkan pilihan menu yang tepat!!')
        
        lagi = input('Apakah mau menggunakannya lagi? (y/n)')
        if lagi == 'n' or lagi == 'N':
            print('''
            Program selesai semoga kode kalian aman. :)
            ''')
            break
        else:
            print()
