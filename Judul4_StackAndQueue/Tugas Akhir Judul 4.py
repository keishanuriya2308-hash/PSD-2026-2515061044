class QueuePrinter:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, file):
        self.queue.append(file)
        print(f"File '{file}' berhasil ditambahkan ke antrean")

    def dequeue(self):
        if self.is_empty():
            print("Antrean printer kosong")
            return

        file = self.queue.pop(0)
        print(f"File '{file}' sedang dicetak")

    def peek(self):
        if self.is_empty():
            print("Antrean printer kosong")
            return

        print(f"File berikutnya: {self.queue[0]}")

    def display(self):
        if self.is_empty():
            print("Antrean printer kosong")
            return

        print("\n=== ANTREAN PRINTER ===")

        for i, file in enumerate(self.queue, start=1):
            print(f"{i}. {file}")


def main():
    printer = QueuePrinter()

    while True:
        print("\n===== SISTEM ANTRIAN PRINTER =====")
        print("1. Tambah File")
        print("2. Cetak File")
        print("3. Lihat File Berikutnya")
        print("4. Tampilkan Antrean")
        print("5. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            nama_file = input("Masukkan nama file: ")
            printer.enqueue(nama_file)

        elif pilih == "2":
            printer.dequeue()

        elif pilih == "3":
            printer.peek()

        elif pilih == "4":
            printer.display()

        # Keluar
        elif pilih == "5":
            print("Program selesai")
            break

        else:
            print("Pilihan tidak valid")


if __name__ == "__main__":
    main()