## a. Judul Program
Program Queue Sistem Antrean Printer
## b. Deskripsi Singkat
Program ini merupakan implementasi struktur data Queue (FIFO — First In First Out) menggunakan bahasa Python untuk mengelola sistem antrean printer, di mana file yang pertama masuk akan menjadi file pertama yang dicetak.
## c. code 
<img width="512" height="547" alt="image" src="https://github.com/user-attachments/assets/8e6ed114-bb77-4e7b-942e-000d1091edd4" />
<img width="456" height="522" alt="image" src="https://github.com/user-attachments/assets/6b208375-fcb2-439a-8bd4-c41b720236d7" />
<img width="437" height="521" alt="image" src="https://github.com/user-attachments/assets/e3cbaced-d24a-4b46-a2f7-c1fdd7f8bc52" />

# Penjelasan

Source code di atas merupakan program Python yang menerapkan struktur data Queue (antrian) untuk membuat sistem antrean printer, di mana program dimulai dengan pembuatan class QueuePrinter yang berfungsi sebagai tempat pengelolaan data antrean menggunakan list kosong self.queue, kemudian terdapat method is_empty() untuk mengecek apakah antrean kosong, method enqueue() untuk menambahkan file ke bagian belakang antrean, method dequeue() untuk mengambil dan mencetak file paling depan sesuai konsep FIFO (First In First Out), method peek() untuk melihat file berikutnya tanpa menghapusnya dari antrean, serta method display() untuk menampilkan seluruh daftar file yang sedang berada dalam antrean printer, lalu pada bagian main() program menampilkan menu interaktif menggunakan perulangan while True sehingga pengguna dapat memilih menu tambah file, cetak file, lihat file berikutnya, tampilkan antrean, atau keluar dari program, sedangkan bagian if __name__ == "__main__": digunakan agar fungsi utama main() dapat dijalankan otomatis ketika file Python dieksekusi secara langsung.

## d. ouput code
<img width="416" height="512" alt="image" src="https://github.com/user-attachments/assets/47135c56-632f-43c1-8638-35232c0e2b32" />
<img width="341" height="507" alt="image" src="https://github.com/user-attachments/assets/ca9fcc49-1166-4960-bd77-32d3c2be5ccc" />
# Penjelasan

Output dari program Queue Sistem Antrean Printer menampilkan menu utama yang berisi pilihan untuk menambahkan file, mencetak file, melihat file berikutnya, menampilkan seluruh antrean, dan keluar dari program, kemudian ketika pengguna memilih menu tambah file maka program akan menampilkan pesan bahwa file berhasil dimasukkan ke antrean, saat memilih cetak file program akan mengambil file paling depan dan menampilkan pesan bahwa file sedang dicetak sesuai konsep FIFO (First In First Out), ketika memilih lihat file berikutnya program akan menampilkan nama file yang berada di posisi paling depan antrean tanpa menghapusnya, lalu saat memilih tampilkan antrean program akan menampilkan seluruh daftar file beserta nomor urut antreannya, sedangkan jika antrean kosong maka program akan menampilkan pesan “Antrean printer kosong”, dan apabila pengguna memilih keluar maka program akan menampilkan pesan “Program selesai” lalu menghentikan sistem.

## e. Link Youtube
https://youtu.be/cmY9WXjX6kU
