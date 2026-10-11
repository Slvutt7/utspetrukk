import os

NAMA_FILE = "data_keuangan.txt"

def inisialisasi_file():
    """Mode 'x': Membuat file data pertama kali. Menangani FileExistsError."""
    try:
        with open(NAMA_FILE, 'x') as f:
            # Menulis header awal file
            f.write("TANGGAL|JENIS|KATEGORI|NOMINAL|KETERANGAN\n")
        print("File data berhasil dibuat!")
    except FileExistsError:
        # File sudah ada, jadi aman dilompati
        pass

def tambah_transaksi(data_str):
    """Mode 'a': Menambahkan data transaksi baru ke baris akhir file."""
    with open(NAMA_FILE, 'a') as f:
        f.write(data_str + "\n")

def baca_transaksi():
    """Mode 'r': Membaca data transaksi secara iteratif baris per baris. 
    Menangani FileNotFoundError."""
    transaksi_list = []
    try:
        with open(NAMA_FILE, 'r') as f:
            # Pembacaan iteratif baris demi baris sesuai ketentuan
            for baris in f:
                transaksi_list.append(baris.strip())
        return transaksi_list
    except FileNotFoundError:
        print(f"Peringatan: File {NAMA_FILE} belum ditemukan. Silakan input data terlebih dahulu.")
        return []

def tulis_laporan(isi_laporan):
    """Mode 'w': Menulis file laporan ringkasan keuangan baru."""
    with open("laporan_keuangan.txt", 'w') as f:
        f.write("=== LAPORAN KEUANGAN PRIBADI ===\n")
        f.write(isi_laporan)
    print("Laporan berhasil disimpan ke 'laporan_keuangan.txt'!")