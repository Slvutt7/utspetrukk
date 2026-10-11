def validasi_angka_positif(nilai_str, nama_field="Nilai"):
    """
    Memvalidasi input string menjadi angka positif.
    Menggunakan try/except (ValueError), raise, dan assert sesuai ketentuan tugas.
    """
    try:
        angka = float(nilai_str)
    except ValueError:
        raise ValueError(f"Error: '{nama_field}' harus berupa angka yang valid!")

    if angka <= 0:
        raise ValueError(f"Error: '{nama_field}' tidak boleh bernilai nol atau negatif!")

    assert angka > 0, f"AssertionError: {nama_field} gagal divalidasi."

    return angka

def validasi_pilihan_jenis(jenis):
    """Memastikan jenis transaksi hanya 'Pemasukan' atau 'Pengeluaran'."""
    jenis_clean = jenis.strip().capitalize()
    if jenis_clean not in ["Pemasukan", "Pengeluaran"]:
        raise ValueError("Error: Jenis transaksi harus bernilai 'Pemasukan' atau 'Pengeluaran'!")
    return jenis_clean
