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

## Struktur Data

File `.xls` harus memiliki struktur tabel HTML dengan `id="tblExport"`. Contoh data `.xls` dapat dilihat di bawah ini:

### Contoh Data `.xls`

**File `data_example.xls`:**

```html
<table id="tblExport">
  <tr>
    <th>No.</th>
    <th>Guest Name</th>
    <th>ID Number</th>
    <th>Gender</th>
    <th>Place, Date Of Birth</th>
    <th>Email</th>
    <th>No.Handphone</th>
    <th>No.Telp</th>
    <th>Guest Type</th>
  </tr>
  <tr>
    <td>1</td>
    <td>John Doe</td>
    <td>KTP(1234567890123456)</td>
    <td>Male</td>
    <td>Jakarta, 1 January 1990</td>
    <td>johndoe@example.com</td>
    <td>08123456789</td>
    <td>0211234567</td>
    <td>Regular</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Jane Smith</td>
    <td>KTP(6543210987654321)</td>
    <td>Female</td>
    <td>Bandung, 15 March 1992</td>
    <td>janesmith@example.com</td>
    <td>08234567890</td>
    <td>0223456789</td>
    <td>Regular</td>
  </tr>
  <tr>
    <td>3</td>
    <td>Alice Johnson</td>
    <td>KTP(1122334455667788)</td>
    <td>Female</td>
    <td>Surabaya, 25 December 1985</td>
    <td>alicejohnson@example.com</td>
    <td>08345678901</td>
    <td>0234567890</td>
    <td>VIP</td>
  </tr>
</table>
```
### Contoh Output JSON
Setelah menjalankan program, data dari file .xls akan dikonversi ke format JSON dan disimpan dalam file combined_data.json. Berikut adalah contoh struktur file JSON yang dihasilkan:

```json
[
    {
        "No.": "1",
        "Guest Name": "John Doe",
        "ID Number": "KTP(1234567890123456)",
        "Gender": "Male",
        "Place, Date Of Birth": "Jakarta, 1 January 1990",
        "Email": "johndoe@example.com",
        "No.Handphone": "08123456789",
        "No.Telp": "0211234567",
        "Guest Type": "Regular"
    },
    {
        "No.": "2",
        "Guest Name": "Jane Smith",
        "ID Number": "KTP(6543210987654321)",
        "Gender": "Female",
        "Place, Date Of Birth": "Bandung, 15 March 1992",
        "Email": "janesmith@example.com",
        "No.Handphone": "08234567890",
        "No.Telp": "0223456789",
        "Guest Type": "Regular"
    },
    {
        "No.": "3",
        "Guest Name": "Alice Johnson",
        "ID Number": "KTP(1122334455667788)",
        "Gender": "Female",
        "Place, Date Of Birth": "Surabaya, 25 December 1985",
        "Email": "alicejohnson@example.com",
        "No.Handphone": "08345678901",
        "No.Telp": "0234567890",
        "Guest Type": "VIP"
    }
]

```
### Penggunaan:
Jalankan program ini di lingkungan Python (seperti Termux). Jika modul yang diperlukan belum diinstal, program akan secara otomatis menanganinya. Data dari file `.xls` akan di-gabungkan menjadi satu file JSON yang dapat digunakan untuk kebutuhan lain.

## Dukung Saya di Trakteer

[![Dukung Saya di Trakteer](https://cdn.trakteer.id/images/embed/trbtn-icon.png?date=18-11-2023)](https://trakteer.id/deni_gentar_candana/tip?open=true)

