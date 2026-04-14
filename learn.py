import random

# ── Fungsi didefinisikan di luar blok if ──────────────────────────
def hitung_luas_persegi(sisi):
    luas = sisi * sisi
    return luas

# ── Sambutan ──────────────────────────────────────────────────────
nama_kamu = input("Masukkan nama kamu: ")
print("Hai " + nama_kamu + ", selamat datang di pembelajaran menjadi software engineering")

# ── Cek umur (Bug 1 diperbaiki: tidak ada overlap) ────────────────
umur_kamu = input("Masukkan umur kamu: ")
umur = int(umur_kamu)

if 0 < umur < 7:
    print("Kamu masih anak-anak")
elif 7 <= umur < 12:        # SD: 7 - 11 tahun
    print("Kamu masuk sekolah dasar")
elif 12 <= umur < 15:       # SMP: 12 - 14 tahun (Bug 1: overlap dihapus)
    print("Kamu masuk sekolah menengah pertama")
elif 15 <= umur < 18:       # SMA: 15 - 17 tahun
    print("Kamu masuk sekolah menengah atas")
elif 18 <= umur < 25:       # Kuliah: 18 - 24 tahun
    print("Kamu masuk perguruan tinggi")
else:
    print("Kamu sedang bekerja atau sudah pensiun")

# ── Pilih game ────────────────────────────────────────────────────
print("\nPilih game kamu:")
print("1. Hitung luas persegi")
print("2. Tebak angka random")

pilihan_game = input("Masukkan pilihan game kamu (1/2): ")

if pilihan_game == "1":
    # Bug 2 diperbaiki: fungsi sudah dipindahkan ke atas
    sisi = input("Masukkan panjang sisi persegi: ")
    sisi_persegi = int(sisi)
    luas_persegi = hitung_luas_persegi(sisi_persegi)
    print("Luas persegi dengan sisi " + str(sisi_persegi) + " adalah " + str(luas_persegi))

elif pilihan_game == "2":
    # Bug 3 diperbaiki: game 2 hanya jalan jika dipilih
    print("\nMari kita bermain tebak angka!")
    angka_rahasia = random.randint(1, 100)
    tebakan = 0
    menang = False

    # Bug 4 diperbaiki: pertanyaan keluar di DALAM loop, bukan sebelumnya
    while tebakan != angka_rahasia:
        tebakan = int(input("Masukkan tebakan kamu (1-100): "))
        if tebakan < angka_rahasia:
            print("Tebakan kamu terlalu rendah")
        elif tebakan > angka_rahasia:
            print("Tebakan kamu terlalu tinggi")
        else:
            # else ini pasti tebakan == angka_rahasia
            print("Selamat! Tebakan kamu benar!")
            menang = True
            break

        # Tanya keluar hanya jika tebakan masih salah
        while True:
            keluar = input("Apakah kamu ingin keluar? (y/n): ")
            if keluar == "y":
                print("Kamu memilih keluar dari game.")
                break
            elif keluar == "n":
                print("Oke, lanjutkan menebak!")
                break
            else:
                print("Input tidak valid. Masukkan 'y' atau 'n'.")

        if keluar == "y":
            break  # keluar dari while tebak angka

    # Poin dihitung lewat flag menang
    point = 1000 - abs(angka_rahasia - tebakan)  # Poin berdasarkan seberapa dekat tebakan terakhir
    if menang:
        print("Kamu mendapatkan " + str(point) + " poin")
    else:
        print("Kamu mendapatkan 0 poin karena tidak berhasil menebak")

    # Validasi keluar setelah game selesai
    if menang:
        while True:
            lanjut = input("Game selesai! Apakah kamu ingin keluar? (y/n): ")
            if lanjut == "y":
                print("Sampai jumpa lagi, " + nama_kamu + "!")
                break
            elif lanjut == "n":
                print("Oke, kamu tetap di sini. Terima kasih sudah bermain!")
                break
            else:
                print("Input tidak valid. Masukkan 'y' untuk keluar atau 'n' untuk tetap.")

else:
    print("Pilihan tidak valid")

print("\nTerima kasih sudah bermain, sampai jumpa lagi " + nama_kamu)
        