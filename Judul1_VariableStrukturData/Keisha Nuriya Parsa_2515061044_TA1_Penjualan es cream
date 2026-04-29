class Node:
    def __init__(self, rasa, harga):
        self.rasa = rasa
        self.harga = harga
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None


    def insert_back(self, rasa, harga):
        new_node = Node(rasa, harga)
        if self.head is None:
            self.head = new_node

        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node


    def display(self):
        if self.head is None:
            print("Data kosong")
            return
        current = self.head
        nomor = 1

        print("\n=== MENU ES KRIM ===")

        while current is not None:
            print(
                nomor,
                ".",
                current.rasa,
                "- Rp",
                current.harga
            )

            current = current.next
            nomor += 1


    def search_menu(self, nomor):

        current = self.head
        count = 1
        while current is not None:
            if count == nomor:
                return current
            current = current.next
            count += 1

        return None



def main():

    data = SinglyLinkedList()

    data.insert_back("Coklat",10000)
    data.insert_back("Vanila",12000)
    data.insert_back("Stroberi",15000)

    pilih = 0

    while pilih != 3:

        print("\n=== SISTEM PENJUALAN ES KRIM ===")
        print("1. Tampilkan Menu")
        print("2. Beli Es Krim")
        print("3. Keluar")

        try:
            pilih = int(
                input("Pilih: ")
            )

        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            data.display()

        elif pilih == 2:
            data.display()
            try:
                nomor = int(
                    input("Pilih nomor menu: ")
                )
                menu = data.search_menu(nomor)

                if menu is None:
                    print("Menu tidak ditemukan")
                    continue

                jumlah = int(
                    input("Jumlah beli: ")
                )
                total = menu.harga * jumlah


                print("\n=== STRUK PEMBELIAN ===")
                print("Rasa   :",menu.rasa)
                print("Harga  :",menu.harga)
                print("Jumlah :",jumlah)
                print("Total  : Rp",total)


            except ValueError:
                print("Input harus angka")


        elif pilih == 3:
            print("Program selesai.")


        else:
            print("Pilihan tidak valid!")



if __name__ == "__main__":
    main()
