# Class 1: Menilai/merepresentasikan objek Transaksi tunggal
class Transaksi:
    def __init__(self, tanggal, jenis, kategori, nominal, **kwargs):
        self.tanggal = tanggal
        self.jenis = jenis  # "Pemasukan" atau "Pengeluaran"
        self.kategori = kategori
        self.nominal = float(nominal)
        # Menggunakan **kwargs untuk menangkap atribut bervariasi (misal: catatan, metode_bayar)
        self.atribut_tambahan = kwargs

    def format_ke_baris(self):
        """Fungsi 1: Mengubah data transaksi menjadi string untuk disimpan di file."""
        keterangan = self.atribut_tambahan.get("catatan", "-")
        return f"{self.tanggal}|{self.jenis}|{self.kategori}|{self.nominal}|{keterangan}"


# Class 2: Pengolah & Analisis Kumpulan Data Keuangan
class AnalisisKeuangan:
    def __init__(self, data_raw):
        self.data_raw = data_raw  # List of string dari file text

    def hitung_total(self, *args):
        """Fungsi 2: Menggunakan *args untuk menjumlahkan beberapa nilai nominal secara fleksibel."""
        total = 0.0
        for nilai in args:
            total += float(nilai)
        return total

    def dapatkan_semua_transaksi(self):
        """Fungsi 3: Mengolah data mentah dari file menjadi list of dictionary."""
        transaksi_list = []
        # Lewati baris pertama (header)
        for baris in self.data_raw[1:]:
            if not baris.strip():
                continue
            parts = baris.strip().split("|")
            if len(parts) >= 5:
                transaksi_list.append({
                    "tanggal": parts[0],
                    "jenis": parts[1],
                    "kategori": parts[2],
                    "nominal": float(parts[3]),
                    "catatan": parts[4]
                })
        return transaksi_list

    def urutkan_transaksi_terbesar(self):
        """Fungsi 4: Menggunakan lambda untuk mengurutkan transaksi dari nominal terbesar."""
        daftar = self.dapatkan_semua_transaksi()
        # Penggunaan lambda sebagai key pada sorted()
        daftar_terurut = sorted(daftar, key=lambda x: x["nominal"], reverse=True)
        return daftar_terurut

    def buat_ringkasan(self):
        """Fungsi 5: Membuat teks laporan ringkasan total pemasukan & pengeluaran."""
        daftar = self.dapatkan_semua_transaksi()
        
        # Filter nominal pemasukan dan pengeluaran
        pemasukan = [t["nominal"] for t in daftar if t["jenis"].lower() == "pemasukan"]
        pengeluaran = [t["nominal"] for t in daftar if t["jenis"].lower() == "pengeluaran"]

        # Menggunakan *args pada hitung_total
        total_in = self.hitung_total(*pemasukan) if pemasukan else 0.0
        total_out = self.hitung_total(*pengeluaran) if pengeluaran else 0.0
        saldo = total_in - total_out

        ringkasan = f"Total Pemasukan  : Rp {total_in:,.2f}\n"
        ringkasan += f"Total Pengeluaran : Rp {total_out:,.2f}\n"
        ringkasan += f"Sisa Saldo        : Rp {saldo:,.2f}\n"
        return ringkasan