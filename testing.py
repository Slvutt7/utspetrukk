import unittest
from keuangan_app.validasi import validasi_angka_positif, validasi_pilihan_jenis
from keuangan_app.processing import AnalisisKeuangan

class TestKeuanganApp(unittest.TestCase):
    
    def test_validasi_angka_positif_valid(self):
        """Uji 1: Memastikan angka positif valid berhasil dikonversi."""
        hasil = validasi_angka_positif("50000", "Nominal")
        self.assertEqual(hasil, 50000.0)

    def test_validasi_angka_positif_negatif(self):
        """Uji 2: Memastikan angka negatif atau nol memunculkan ValueError."""
        with self.assertRaises(ValueError):
            validasi_angka_positif("-1000", "Nominal")

    def test_validasi_angka_positif_huruf(self):
        """Uji 3: Memastikan input huruf/string pada angka memunculkan ValueError."""
        with self.assertRaises(ValueError):
            validasi_angka_positif("lima_ribu", "Nominal")

    def test_validasi_pilihan_jenis(self):
        """Uji 4: Memastikan validasi jenis transaksi (Pemasukan/Pengeluaran)."""
        hasil = validasi_pilihan_jenis("pemasukan")
        self.assertEqual(hasil, "Pemasukan")
        
        with self.assertRaises(ValueError):
            validasi_pilihan_jenis("Hutang")

    def test_hitung_total_args(self):
        """Uji 5: Memastikan fungsi *args menghitung total nominal dengan benar."""
        data_dummy = ["TANGGAL|JENIS|KATEGORI|NOMINAL|KETERANGAN", "2026-01-01|Pemasukan|Gaji|1000000|Bulanan"]
        analisis = AnalisisKeuangan(data_dummy)
        total = analisis.hitung_total(100000, 250000, 150000)
        self.assertEqual(total, 500000.0)

if __name__ == '__main__':
    unittest.main()