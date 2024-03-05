class Mahasiswa:
    def __init__(self, nama, kelas, prodi, fakultas, tempat_tinggal, asal):
        self.nama = nama
        self.kelas = kelas
        self.prodi = prodi
        self.fakultas = fakultas
        self.tempat_tinggal = tempat_tinggal
        self.asal = asal

    def info(self):
        print("Nama:", self.nama)
        print("Kelas:", self.kelas)
        print("Prodi:", self.prodi)
        print("Fakultas:", self.fakultas)
        print("Tempat Tinggal:", self.tempat_tinggal)
        print("Asal:", self.asal)

# Contoh penggunaan
mhs1 = Mahasiswa("Muhammad Zidan", "A", "Pendidikan Komputer", "FKIP", "Samarinda", "Samarinda")
mhs1.info()


