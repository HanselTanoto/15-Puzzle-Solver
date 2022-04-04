# 15-Puzzle Solver
>15-_Puzzle Solver_ menggunakan algoritma _Branch and Bound_

## Deskripsi Singkat
15-_Puzzle_ adalah suatu teka teki dengan papan permainan berbentuk persegi yang tersusun atas 16 buah kotak (_tile_). Kotak-kotak tersebut akan diisi oleh susunan angka acak dari 1 hingga 15 dan 1 _tile_ sisanya adalah _tile_ kosong. Tujuan (_objective_) dari teka teki ini adalah melakukan pergeseran pada _tile-tile_ tersebut (dalam arah kiri, kanan, atas, dan bawah) dengan memanfaatkan tile kosong tadi sedemikian sehingga diperoleh susunan kotak dengan nilai terurut dari 1 hingga 15 dan diakhiri oleh _tile_ kosong di pojok kanan bawah. Program ini akan menyelesaikan persoalan 15-_Puzzle_ ini dengan menggunakan algoritma _branch and bound_.

Algoritma _Branch and Bound_ (B&B) pada umumnya digunakan pada persoalan-persoalan optimasi yaitu dengan cara meminimalkan atau memaksimalkan fungsi objektif dengan tetap tidak melanggar _constraint_ yang ditetapkan. B&B dapat dikatakan merupakan penggabungan dari algoritma BFS (_Breadth First Search_) dan _Least Cost Search_, dimana setiap simpul pada pohon pencarian B&B memiliki suatu nilai _cost_ / biaya dan simpul ekspannya akan dipilih berdasarkan nilai _cost_-nya tersebut (maksimasi/minimasi). Sama seperti algoritma _backtracking_, simpul yang tidak mengarah ke solusi akan “dipangkas” (di-_pruning_) menggunakan suatu fungsi pembatas. Umumnya, fungsi pembatas akan memangkas simpul yang _cost_-nya tidak lebih baik dari nilai _cost_ terbaik saat itu atau simpul yang tidak _feasible_ karena melanggar suatu _constraint_.

## _Requirement_ Program
1. Program ini menggunakan bahasa pemrograman __Python__
2. Program ini dapat dijalankan pada sistem operasi __Windows__
3. Program ini dapat dijalankan melalui __Command Prompt (cmd)__ dan __Windows Powershell__
4. _Driver_ pada pustaka ini menggunakan modul __os__, __time__, __sys__, __heapq__, dan __random__ yang sudah termasuk ke dalam Python _Standard Library_.

## Cara Menggunakan Program
1. _Clone repository_ ini menggunakan _command_:
   ```
   git clone https://github.com/HanselTanoto/Convex-Hull.git
   ```
   atau unduh _zip file_ dari _repository_ ini lalu di_extract_. 
2. Buka terminal lalu ubah directory ke folder src pada program ini.
4. Jalankan program _driver_ dengan mengetikkan _command_:
   ```
   python main.py
   ```
5. Akan muncul pilihan menu untuk me-_load_ _puzzle_ dari _file_ eksternal berformat .txt (pilih 1), membangkitkan _puzzle_ sembarang (pilih 2), atau keluar dari program (pilih 3).
6. Apabila memilih 1, _user_ akan diminta memasukkan _path file_ berisi _puzzle_ yang ingin diselesaikan. Sedangkan jika memilih 2, program akan langsung memproses puzzle dan _user_ tidak perlu memasukkan _input_ apapun.
7. Setelah proses selesai, hasil dari pemecahan _puzzle_ akan ditampilkan ke layar.

## _Author_
[Hansel Valentino Tanoto](https://github.com/HanselTanoto) - K-01 / 13520046
