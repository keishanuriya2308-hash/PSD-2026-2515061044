## a. Judul Program 
Mengurutkan usia mahasiswa
## b. Deskripsi Singkat
Program ini dibuat untuk mengurutkan data usia mahasiswa menggunakan algoritma Selection Sort. Data usia yang awalnya tidak beraturan akan diurutkan dari yang terkecil ke terbesar (ascending) agar lebih mudah dibaca dan dianalisis.
## c. code
<img width="717" height="852" alt="image" src="https://github.com/user-attachments/assets/4338efbc-41fe-4a2d-bd50-4d960a5d6004" />
<img width="584" height="308" alt="image" src="https://github.com/user-attachments/assets/ba481e24-a315-462b-bbcc-ca5ae461d9f5" />
## Penjelasan
Pertama, terdapat fungsi tukar() yang digunakan untuk menukar posisi dua data dalam list. Fungsi ini bekerja dengan menyimpan sementara salah satu nilai ke dalam variabel temp, lalu menukar posisi kedua data tersebut. Fungsi ini dipanggil saat proses sorting ketika ditemukan data yang perlu ditukar posisinya.

Selanjutnya, terdapat fungsi selection_sort() yang merupakan inti dari program. Pada fungsi ini digunakan dua perulangan (loop). Perulangan pertama digunakan untuk menentukan posisi data yang akan diisi, sedangkan perulangan kedua digunakan untuk mencari nilai terkecil dari sisa data yang belum terurut. Jika ditemukan nilai yang lebih kecil, maka indeksnya akan disimpan, kemudian dilakukan pertukaran dengan elemen pada posisi awal menggunakan fungsi tukar(). Proses ini dilakukan berulang sampai seluruh data terurut.

Kemudian, pada fungsi main(), program akan meminta pengguna untuk memasukkan jumlah mahasiswa. Setelah itu, pengguna diminta untuk memasukkan usia masing-masing mahasiswa satu per satu. Data yang dimasukkan akan disimpan ke dalam sebuah list bernama usia. Pada bagian ini juga digunakan try-except untuk memastikan input yang dimasukkan berupa angka, sehingga program tidak error.

Terakhir, terdapat bagian if __name__ == "__main__": yang berfungsi untuk menjalankan fungsi main() ketika program dieksekusi.

## d. outputnya
<img width="1900" height="471" alt="Screenshot 2026-05-02 201522 (1)" src="https://github.com/user-attachments/assets/815c7f84-c719-460f-859b-4c82c1d1f942" />
## Penjelasan 
Pada bagian output, program pertama menampilkan data sebelum diurutkan menggunakan print(). Setelah itu, fungsi selection_sort() dipanggil untuk mengurutkan data. Terakhir, program menampilkan hasil data yang sudah terurut dengan perulangan for, sehingga semua nilai usia ditampilkan secara berurutan dari yang terkecil ke terbesar.
## e. Link Youtube
https://youtu.be/YOHu6KImlKQ?si=0nay_EYu741JIgi3
