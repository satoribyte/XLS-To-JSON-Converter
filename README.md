Program ini dirancang untuk membaca file .xls yang berisi tabel HTML, mengekstraksi data dari tabel tersebut, dan kemudian menggabungkan semua data ke dalam satu file JSON. Program ini juga secara otomatis menginstal dependensi yang diperlukan jika belum ada di sistem (seperti BeautifulSoup dan tqdm).

### Cara Kerja Program:

1. **Cek dan Instal Modul:**
   Program pertama-tama memeriksa apakah modul `BeautifulSoup` (dari library `bs4`) dan `tqdm` sudah diinstal di sistem. Jika belum terpasang, program akan secara otomatis menginstal modul-modul tersebut menggunakan `pip`.

2. **Mengimpor Modul:**
   Setelah modul terinstal, mereka akan diimpor untuk digunakan dalam program. 
   - `BeautifulSoup` digunakan untuk mem-parsing konten HTML dari file `.xls`.
   - `tqdm` digunakan untuk menampilkan progress bar selama proses file berlangsung.

3. **Lokasi File dan Output:**
   Program bekerja di direktori tempat file Python ini dijalankan. File-file `.xls` akan diproses dari direktori tersebut, dan hasilnya disimpan dalam file JSON bernama `combined_data.json` di lokasi yang sama.

4. **Mem-parsing File HTML:**
   - Program membaca setiap file `.xls` yang di dalamnya berisi tabel HTML.
   - Setiap tabel memiliki `id="tblExport"`, yang menjadi target pencarian saat parsing. 
   - Program mengekstraksi judul kolom dari baris pertama tabel dan mengekstrak data dari baris berikutnya.
   - Jika panjang data dalam satu baris sesuai dengan jumlah kolom, data tersebut akan disimpan dalam bentuk dictionary dengan kolom sebagai kunci dan nilai data sebagai isi.

5. **Penomoran Otomatis:**
   Kolom bernama "No." diisi secara otomatis berdasarkan urutan data, dimulai dari 1 hingga n (jumlah total data). Ini menggantikan nilai asli yang mungkin ada di kolom "No." dari tabel sumber.

6. **Menggabungkan Data:**
   Data dari semua file `.xls` yang ditemukan dalam folder digabungkan menjadi satu list. List ini kemudian disimpan dalam format JSON dengan indentasi 4 spasi untuk memudahkan pembacaan.

7. **Proses dan Progress Bar:**
   Program menggunakan `tqdm` untuk menampilkan progress bar yang menunjukkan kemajuan proses dalam membaca dan memproses file `.xls`. Ini memberikan umpan balik visual bagi pengguna tentang berapa banyak file yang telah diproses.

8. **Output File:**
   Setelah semua file diproses, data disimpan dalam file `combined_data.json`. Nama file ini bersifat statis, dan akan ditimpa setiap kali program dijalankan ulang.

### Fungsi Utama dalam Program:

1. **`install(package)`:**
   Fungsi ini memanggil `pip` untuk menginstal paket yang diperlukan jika belum ada di sistem.

2. **`check_and_install(package, alias=None)`:**
   Fungsi ini memeriksa apakah modul sudah ada. Jika tidak, maka modul akan diinstal dan diimpor ke dalam program.

3. **`parse_html_table(html_content)`:**
   Fungsi ini digunakan untuk mem-parsing konten HTML yang berisi tabel. Ia mengekstrak kolom dari baris pertama dan data dari baris berikutnya, lalu mengembalikannya dalam bentuk list of dictionaries.

4. **`read_xls_files(folder)`:**
   Fungsi ini bertanggung jawab untuk membaca semua file `.xls` dalam folder yang ditentukan. Setiap file diproses dengan fungsi `parse_html_table()` dan data digabungkan ke dalam satu list.

### Hal yang Perlu Diperhatikan:

- Program ini berasumsi bahwa file `.xls` berisi konten HTML dengan tabel yang memiliki `id="tblExport"`.
- File output `combined_data.json` akan ditimpa setiap kali program dijalankan. Pastikan untuk membackup data lama jika diperlukan.
- Jika terjadi error selama pembacaan file `.xls`, program akan mencetak pesan kesalahan namun tetap melanjutkan proses file lainnya.

### Penggunaan:
Jalankan program ini di lingkungan Python (seperti Termux). Jika modul yang diperlukan belum diinstal, program akan secara otomatis menanganinya. Data dari file `.xls` akan di-gabungkan menjadi satu file JSON yang dapat digunakan untuk kebutuhan lain.
