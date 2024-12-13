# IF2150 - Rekayasa Perangkat Lunak 2024
> Tugas Besar - IF2150 - Rekayasa Perangkat Lunak 2024

### Kelompok K01-G11
| NIM      | Nama                            |
| -------- | ------------------------------- |
| 13523051 | Ferdinand Gabe Tua Sinaga       |
| 13523023 | Muhammad Aufa Farabi            |
| 13523037 | Buege Mahara Putra              |
| 13523117 | Ferdin Arsenarendra Purtadi     |
| 13523111 | Muhammad Iqbal Haidar           |

## SIMADA

SIMADA (Sistem Manajemen Sumber Daya Wakanda) adalah sebuah aplikasi yang dirancang untuk membantu admin atau pengguna dalam mengelola sumber daya strategis secara lebih efektif. Dengan adanya SIMADA, admin dapat lebih mudah memantau, mencatat, dan mengelola alokasi sumber daya, seperti vibranium, untuk memastikan penggunaannya tetap efisien dan optimal. Aplikasi ini juga mendukung admin dalam pengambilan keputusan dengan menyediakan informasi real-time terkait ketersediaan dan distribusi sumber daya.

## Menjalankan Program

_Di bawah ini adalah langkah menjalankan program._

1. Clone repository
   ```sh
   git clone https://github.com/iqbalhaidr/IF2150-2024-K01-G11-SIMADA.git
   ```
2. Jalankan Driver
   ```sh
   py ./src/main.py
   ```
   ```sh
   python ./src/main.py
   ```

## Daftar Modul

_Modul yang digunakan pada program ini_

- sqlite3
- tkinter
- pathlib
- sys

## Pembagian Tugas
| NIM      | Nama                            | Tugas                                                                                                        |
| -------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| 13523051 | Ferdinand Gabe Tua Sinaga       | Database, ResourceManager, LogActivity, ResourceControl, Report, ReportManager, UIResource (Log Activity)    |
| 13523023 | Muhammad Aufa Farabi            | UIResource (Daftar Resource, Daftar Inventaris), ResourceControl, Inventaris, ResourceManager                |
| 13523037 | Buege Mahara Putra              | Dokumen                                                                                                      |
| 13523117 | Ferdin Arsenarendra Purtadi     | LogActivity, Report, ReportManager, ResourceControl, Inventaris                                              |
| 13523111 | Muhammad Iqbal Haidar           | ReportManager, ResourceControl                                                                               |

## Tabel Basis Data
<table border="0" style="border-collapse: collapse; text-align: left;">
  <tr>
    <td><b>Resources</b></td>
  </tr>
  <tr>
    <td>
      id<br>
      name<br>
      quantity<br>
      total_quantity<br>
    </td>
  </tr>
</table>

<table border="0" style="border-collapse: collapse; text-align: left;">
  <tr>
    <td><b>Inventaris</b></td>
  </tr>
  <tr>
    <td>
      inventaris_id<br>
      resource_id<br>
      location<br>
      quantity<br>
    </td>
  </tr>
</table>

<table border="0" style="border-collapse: collapse; text-align: left;">
  <tr>
    <td><b>Report</b></td>
  </tr>
  <tr>
    <td>
      report_id<br>
      resource_id<br>
      detail<br>
    </td>
  </tr>
</table>

<table border="0" style="border-collapse: collapse; text-align: left;">
  <tr>
    <td><b>LogActivity</b></td>
  </tr>
  <tr>
    <td>
      log_id<br>
      resource_id<br>
      activity<br>
      timestamp<br>
    </td>
  </tr>
</table>
