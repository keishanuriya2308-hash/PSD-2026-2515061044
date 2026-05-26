class Node:
    def __init__(self, nilai):
        self.nilai = nilai
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, nilai):
        if root is None:
            return Node(nilai)

        if nilai < root.nilai:
            root.left = self.insert(root.left, nilai)
        elif nilai > root.nilai:
            root.right = self.insert(root.right, nilai)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.nilai, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.nilai, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.nilai, end=" ")

    def search(self, root, key):
        if root is None or root.nilai == key:
            return root

        if key < root.nilai:
            return self.search(root.left, key)

        return self.search(root.right, key)

    def min_value(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current

    def delete(self, root, key):
        if root is None:
            return root

        if key < root.nilai:
            root.left = self.delete(root.left, key)

        elif key > root.nilai:
            root.right = self.delete(root.right, key)

        else:
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            temp = self.min_value(root.right)
            root.nilai = temp.nilai
            root.right = self.delete(root.right, temp.nilai)

        return root


bst = BST()

while True:
    print("\n=== PROGRAM DATA NILAI MAHASISWA ===")
    print("1. Tambah Nilai")
    print("2. Tampilkan Inorder")
    print("3. Tampilkan Preorder")
    print("4. Tampilkan Postorder")
    print("5. Cari Nilai")
    print("6. Hapus Nilai")
    print("7. Keluar")

    try:
        pilih = int(input("Pilih menu: "))
    except ValueError:
        print("Input harus angka!")
        continue

    if pilih == 1:
        try:
            nilai = int(input("Masukkan nilai mahasiswa: "))
            bst.root = bst.insert(bst.root, nilai)
            print("Nilai berhasil ditambahkan")
        except ValueError:
            print("Input harus angka!")

    elif pilih == 2:
        print("Data Inorder : ", end="")
        bst.inorder(bst.root)
        print()

    elif pilih == 3:
        print("Data Preorder : ", end="")
        bst.preorder(bst.root)
        print()

    elif pilih == 4:
        print("Data Postorder : ", end="")
        bst.postorder(bst.root)
        print()

    elif pilih == 5:
        try:
            cari = int(input("Masukkan nilai yang dicari: "))
            hasil = bst.search(bst.root, cari)

            if hasil:
                print(f"Nilai {cari} ditemukan")
            else:
                print(f"Nilai {cari} tidak ditemukan")

        except ValueError:
            print("Input harus angka!")

    elif pilih == 6:
        try:
            hapus = int(input("Masukkan nilai yang dihapus: "))
            bst.root = bst.delete(bst.root, hapus)
            print("Nilai berhasil dihapus")
        except ValueError:
            print("Input harus angka!")

    elif pilih == 7:
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid")