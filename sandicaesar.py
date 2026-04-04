# Program Otomatisasi: Analisis Frekuensi dan Brute-Force
teks_sandi = "KHOOR ZRUOG"
daftar_abjad = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("--- TAHAP 1: PENGHITUNGAN FREKUENSI HURUF ---")
# Menggunakan dictionary untuk mencatat kemunculan huruf
buku_catatan = {}
for karakter in teks_sandi:
    if karakter != ' ': # Memastikan spasi tidak ikut terhitung
        buku_catatan[karakter] = buku_catatan.get(karakter, 0) + 1

# Menampilkan hasil dari yang paling banyak muncul
for karakter, jumlah in sorted(buku_catatan.items(), key=lambda x: x[1], reverse=True):
    print(f"Huruf '{karakter}' terdeteksi sebanyak: {jumlah} kali")

print("\n--- TAHAP 2: SIMULASI BRUTE-FORCE (1-25) ---")
# Mencoba memutar kunci mundur satu per satu
for coba_kunci in range(1, 26):
    hasil_dekripsi = ""
    for karakter in teks_sandi:
        if karakter in daftar_abjad:
            # Rumus modulo 26 agar abjad berputar seperti roda
            posisi_baru = (daftar_abjad.index(karakter) - coba_kunci) % 26
            hasil_dekripsi += daftar_abjad[posisi_baru]
        else:
            hasil_dekripsi += karakter # Spasi dibiarkan saja
            
    print(f"[Kunci {coba_kunci:02d}] menghasilkan teks -> {hasil_dekripsi}")