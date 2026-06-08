class HashMap:
    def __init__(self):
        self.data = {}

    def tambah_mahasiswa(self, nim, nama):
        self.data[nim] = nama
        print("Data berhasil ditambahkan!")

    def cari_mahasiswa(self, nim):
        if nim in self.data:
            print(f"NIM  : {nim}")
            print(f"Nama : {self.data[nim]}")
        else:
            print("Data tidak ditemukan!")

    def hapus_mahasiswa(self, nim):
        if nim in self.data:
            del self.data[nim]
            print("Data berhasil dihapus!")
        else:
            print("Data tidak ditemukan!")

    def tampilkan_data(self):
        if len(self.data) == 0:
            print("Belum ada data mahasiswa.")
        else:
            print("\n=== DATA MAHASISWA ===")
            for nim, nama in self.data.items():
                print(f"NIM: {nim} | Nama: {nama}")


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
            nim = input("Masukkan NIM : ")
            nama = input("Masukkan Nama: ")
            sistem.tambah_mahasiswa(nim, nama)

        elif pilihan == "2":
            nim = input("Masukkan NIM yang dicari: ")
            sistem.cari_mahasiswa(nim)

        elif pilihan == "3":
            nim = input("Masukkan NIM yang akan dihapus: ")
            sistem.hapus_mahasiswa(nim)

        elif pilihan == "4":
            sistem.tampilkan_data()

        elif pilihan == "5":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()