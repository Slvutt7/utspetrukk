import os
from keuangan_app import fileio, processing, validasi

def main():
    # Inisialisasi file data pertama kali menggunakan mode 'x'
    fileio.inisialisasi_file()
    
    while True:
        print("\n===============================")
        print("   APLIKASI KEUANGAN PRIBADI   ")
        print("===============================")
        print("1. Tambah Transaksi Baru")
        print("2. Lihat Ringkasan & Urutkan Transaksi")
        print("3. Cetak Laporan ke File Text")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1-4): ").strip()
        
        if pilihan == '1':
            print("\n--- Tambah Transaksi ---")
            tanggal = input("Masukkan tanggal (contoh: 2026-06-01): ").strip()
            jenis_raw = input("Jenis (Pemasukan / Pengeluaran): ").strip()
            
            try:
                # Validasi menggunakan modul validasi (try/except, raise)
                jenis = validasi.validasi_pilihan_jenis(jenis_raw)
                kategori = input("Masukkan kategori (misal: Gaji, Makan, Transport): ").strip()
                if not kategori:
                    raise ValueError("Kategori tidak boleh kosong!")
                    
                nominal_str = input("Masukkan nominal (angka): ").strip()
                nominal = validasi.validasi_angka_positif(nominal_str, "Nominal")
                
                catatan = input("Catatan tambahan (opsional): ").strip()
                if not catatan:
                    catatan = "-"
                    
                # Membuat objek Transaksi (menggunakan **kwargs)
                trx = processing.Transaksi(tanggal, jenis, kategori, nominal, catatan=catatan)
                
                # Menyimpan data menggunakan mode 'a' di fileio
                fileio.tambah_transaksi(trx.format_ke_baris())
                print("✅ Transaksi berhasil disimpan!")
                
            except ValueError as e:
                print(f"❌ {e}")
            except Exception as e:
                print(f"❌ Terjadi kesalahan: {e}")
                
        elif pilihan == '2':
            print("\n--- Ringkasan & Analisis Transaksi ---")
            data_mentah = fileio.baca_transaksi()
            if len(data_mentah) <= 1:
                print("Belum ada data transaksi yang tersimpan.")
            else:
                analisis = processing.AnalisisKeuangan(data_mentah)
                print(analisis.buat_ringkasan())
                
                print("\n📋 Daftar Transaksi (Urut dari Nominal Terbesar via Lambda):")
                sorted_list = analisis.urutkan_transaksi_terbesar()
                for idx, t in enumerate(sorted_list, 1):
                    print(f"{idx}. [{t['tanggal']}] {t['jenis']} - {t['kategori']} : Rp {t['nominal']:,.2f} (Catatan: {t['catatan']})")
                    
        elif pilihan == '3':
            print("\n--- Cetak Laporan ---")
            data_mentah = fileio.baca_transaksi()
            if len(data_mentah) <= 1:
                print("Belum ada data untuk dilaporkan.")
            else:
                analisis = processing.AnalisisKeuangan(data_mentah)
                ringkasan = analisis.buat_ringkasan()
                fileio.tulis_laporan(ringkasan)
                
        elif pilihan == '4':
            print("Terima kasih telah menggunakan aplikasi keuangan!")
            break
        else:
            print("❌ Pilihan tidak valid, silakan masukkan angka 1-4.")

if __name__ == '__main__':
    # Blok __main__ untuk pengujian lokal aplikasi utama
    main()