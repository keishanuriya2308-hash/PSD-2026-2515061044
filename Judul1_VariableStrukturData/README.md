## a. Judul Program
Sistem Penjualan Es Krim Menggunakan Singly Linked List
## b. Deskripsi Singkat
Program Sistem Penjualan Es Krim merupakan program sederhana yang digunakan untuk menampilkan daftar menu es krim, memilih rasa yang tersedia, melakukan transaksi pembelian, serta menghitung total harga berdasarkan jumlah pembelian. Program ini mensimulasikan sistem penjualan sederhana seperti pada kasir, di mana pengguna dapat melihat menu, memilih produk, lalu memperoleh hasil transaksi berupa struk pembelian.
## c. Kode Sumber
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/17f288e7-fa30-48ed-a58a-6b302bd2d46f" />
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/628a7936-d915-458b-bfc2-13f601303e15" />
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/55fc9b42-296f-43c3-802a-f5da6d4c19f8" />
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/c4fe63eb-6403-4611-9f22-b52443f4090b" />
## Penjelasan Kode
1. Class Node
class Node digunakan untuk membuat node penyimpan data rasa, harga, dan pointer next.
self.rasa menyimpan nama rasa es krim.
self.harga menyimpan harga es krim.
self.next menghubungkan node ke node berikutnya.

2. Class SinglyLinkedList
class SinglyLinkedList digunakan untuk membuat linked list satu arah.
self.head = None berfungsi sebagai penunjuk node pertama.

3. Fungsi Insert Data
insert_back() digunakan untuk menambah menu ke belakang linked list.
new_node = Node(rasa, harga) membuat node baru.
if self.head is None mengecek apakah list kosong.
current digunakan untuk menelusuri node sampai akhir.
current.next = new_node menyambungkan node baru.

4. Fungsi Display
display() digunakan untuk menampilkan seluruh menu es krim.
current = self.head memulai traversal dari head.
while current is not None membaca semua node satu per satu.

5. Fungsi Search Menu
search_menu() digunakan untuk mencari menu berdasarkan nomor pilihan.
if count == nomor memeriksa apakah data ditemukan.
return current mengembalikan menu yang ditemukan.

6. Program Utama
data = SinglyLinkedList() membuat objek linked list.
data.insert_back(...) memasukkan data menu ke linked list.
while pilih != 3 menjalankan program sampai pengguna keluar.
pilih = int(input(...)) menerima pilihan menu dari pengguna.

7. Proses Pembelian
menu = data.search_menu(nomor) mencari menu yang dipilih.
jumlah = int(input(...)) menerima jumlah pembelian.
total = menu.harga * jumlah menghitung total pembayaran.

8. Output Transaksi
print(...) digunakan menampilkan rasa, harga, jumlah, dan total pembelian.

## d. Program Keluaran
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/40d7a578-072d-4d1b-b7c8-fe13224040ff" />
1. Output Menu Utama

Program menampilkan pilihan untuk melihat menu, membeli es krim, atau keluar.

2. Output Tampilkan Menu

Program menampilkan daftar rasa es krim beserta harganya.

3. Output Pembelian

Program menerima pilihan menu dan jumlah pembelian dari pengguna.

4. Output Transaksi

Program menghitung dan menampilkan rasa yang dipilih, harga, jumlah beli, dan total pembayaran.

5. Output Jika Input Salah

Program menampilkan pesan kesalahan jika input tidak valid atau menu tidak ditemukan.

6. Output Keluar

Program menampilkan pesan selesai saat pengguna keluar dari program.

## e. Tautan YouTube
https://youtu.be/AUJkl_6KbO0?si=TjWhWA6RLTqj2b_n
