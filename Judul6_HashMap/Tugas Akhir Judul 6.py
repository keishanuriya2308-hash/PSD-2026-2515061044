class HashMap:
    def __init__(self):
        self.data = {}

    def tambah_mahasiswa(self, npm, nama):
        self.data[npm] = nama
        print("Data berhasil ditambahkan!")

    def cari_mahasiswa(self, npm):
        if npm in self.data:
            print(f"NPM  : {npm}")
            print(f"Nama : {self.data[npm]}")
        else:
            print("Data tidak ditemukan!")

    def hapus_mahasiswa(self, npm):
        if npm in self.data:
            del self.data[npm]
            print("Data berhasil dihapus!")
        else:
            print("Data tidak ditemukan!")

    def tampilkan_data(self):
        if len(self.data) == 0:
            print("Belum ada data mahasiswa.")
        else:
            print("\n=== DATA MAHASISWA ===")
            for npm, nama in self.data.items():
                print(f"NPM: {npm} | Nama: {nama}")


def main():
    sistem = HashMap()

    while True:
        print("\n===== SISTEM DATA MAHASISWA =====")
        print("1. Tambah Data")
        print("2. Cari Data")
        print("3. Hapus Data")
        print("4. Tampilkan Semua Data")
        print("5. Keluar")

        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            npm = input("Masukkan NPM : ")
            nama = input("Masukkan Nama: ")
            sistem.tambah_mahasiswa(npm, nama)

        elif pilihan == "2":
            npm = input("Masukkan NPM yang dicari: ")
            sistem.cari_mahasiswa(npm)

        elif pilihan == "3":
            npm = input("Masukkan NPM yang akan dihapus: ")
            sistem.hapus_mahasiswa(npm)

        elif pilihan == "4":
            sistem.tampilkan_data()

        elif pilihan == "5":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()class HashMap:
    def __init__(self):
        self.data = {}

    def tambah_mahasiswa(self, npm, nama):
        self.data[npm] = nama
        print("Data berhasil ditambahkan!")

    def cari_mahasiswa(self, npm):
        if npm in self.data:
            print(f"NPM  : {npm}")
            print(f"Nama : {self.data[npm]}")
        else:
            print("Data tidak ditemukan!")

    def hapus_mahasiswa(self, npm):
        if npm in self.data:
            del self.data[npm]
            print("Data berhasil dihapus!")
        else:
            print("Data tidak ditemukan!")

    def tampilkan_data(self):
        if len(self.data) == 0:
            print("Belum ada data mahasiswa.")
        else:
            print("\n=== DATA MAHASISWA ===")
            for npm, nama in self.data.items():
                print(f"NPM: {npm} | Nama: {nama}")


def main():
    sistem = HashMap()

    while True:
        print("\n===== SISTEM DATA MAHASISWA =====")
        print("1. Tambah Data")
        print("2. Cari Data")
        print("3. Hapus Data")
        print("4. Tampilkan Semua Data")
        print("5. Keluar")

        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            npm = input("Masukkan NPM : ")
            nama = input("Masukkan Nama: ")
            sistem.tambah_mahasiswa(npm, nama)

        elif pilihan == "2":
            npm = input("Masukkan NPM yang dicari: ")
            sistem.cari_mahasiswa(npm)

        elif pilihan == "3":
            npm = input("Masukkan NPM yang akan dihapus: ")
            sistem.hapus_mahasiswa(npm)

        elif pilihan == "4":
            sistem.tampilkan_data()

        elif pilihan == "5":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()v