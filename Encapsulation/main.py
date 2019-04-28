class Student:
    total = 0
    def __init__(self, nama, usia, keahlian):
        self.__nama = nama
        self.__usia = usia
        self.__keahlian = keahlian
        Student.total += 1

    def getNama(self):
        print(self.__nama)

    def getTahunLahir(self, year):
        self.__usia = self.__usia - year

    def show(self):
        print('Nama     : '+ self.__nama)
        print('Usia     : '+ str(self.__usia))
        print('Keahlian : '+ self.__keahlian)

murid = Student('Syahrul', 20, 'Rekayasa Perangkat Lunak')

murid.show()
print('Jumlah Siswa : ' + str(Student.total))

