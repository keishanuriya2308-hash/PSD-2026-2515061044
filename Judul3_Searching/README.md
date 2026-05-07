## a. Judul Program
Program Pencarian Data Menggunakan Algoritma Binary Search
## b. Deskripsi Singkat
Program ini dibuat menggunakan bahasa Python untuk mencari sebuah data pada array menggunakan metode Binary Search. Algoritma ini bekerja dengan cara membandingkan nilai tengah array dengan data yang dicari, kemudian mempersempit area pencarian ke kiri atau ke kanan hingga data ditemukan. Binary Search hanya dapat digunakan pada data yang sudah terurut secara menaik.
## c. code
<img width="461" height="690" alt="image" src="https://github.com/user-attachments/assets/074347a8-c80d-40ed-bb52-0ed82b425a23" />
<img width="383" height="138" alt="image" src="https://github.com/user-attachments/assets/a2713385-b269-4091-855a-fafcb20ff75c" />


## Penjelasan 
Program diawali dengan pembuatan fungsi binary_search(arr, n, target) yang berfungsi untuk melakukan pencarian data pada array. Di dalam fungsi tersebut terdapat variabel low yang digunakan sebagai indeks awal array dan high sebagai indeks akhir array. Program kemudian menjalankan perulangan selama area pencarian masih tersedia dengan kondisi low <= high. Selanjutnya program menghitung indeks tengah menggunakan rumus mid = (low + high) // 2, lalu menampilkan indeks dan nilai tengah yang sedang dicek. Setelah itu program membandingkan nilai tengah dengan target yang dicari. Jika nilai tengah sama dengan target maka program mengembalikan indeks data menggunakan return mid. Jika target lebih besar dari nilai tengah maka pencarian dipindahkan ke bagian kanan array dengan mengubah nilai low = mid + 1, sedangkan jika target lebih kecil maka pencarian dipindahkan ke bagian kiri array dengan mengubah nilai high = mid - 1. Proses tersebut dilakukan secara berulang sampai data ditemukan atau area pencarian habis. Jika data tidak ditemukan maka fungsi mengembalikan nilai -1.
Pada fungsi main(), program meminta pengguna memasukkan jumlah elemen array sebanyak 5 data. kemudian program membuat list kosong untuk menyimpan data. Setelah itu pengguna memasukkan data array secara urut menaik yaitu 12, 23, 27, 45, dan 67. Selanjutnya program meminta pengguna memasukkan angka yang ingin dicari yaitu 27, lalu memanggil fungsi binary_search() untuk melakukan pencarian data. Hasil pencarian kemudian disimpan pada variabel hasil. Jika data ditemukan maka program menampilkan posisi indeks data, sedangkan jika data tidak ditemukan maka program akan menampilkan pesan bahwa data tidak ditemukan. Pada bagian akhir terdapat if __name__ == "__main__": yang digunakan untuk menjalankan fungsi utama program saat file dijalankan secara langsung.


## d. Output Code
<img width="1600" height="462" alt="44905302-9b6e-4783-a581-de6f6055a01f" src="https://github.com/user-attachments/assets/9de87e5f-0ae7-4a97-8f16-47b4e1c6f38e" />


## Penjelasan
Program langsung mengecek nilai tengah array yaitu 27 pada indeks ke-2, karena nilai tersebut sama dengan angka yang dicari maka program langsung menampilkan bahwa data ditemukan pada indeks ke-2 tanpa perlu melakukan pencarian ulang ke bagian kiri atau kanan array.

## e. Link Youtube
https://youtu.be/vvNBOEUdiak?si=52zDS-8rkuVpG8gm
  
