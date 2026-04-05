nama_kamu = input("Masukkan nama kamu: ")
print("hai " + nama_kamu + ", selamat datang di pembelajaran mejadi sofware engineering")

umur_kamu = input("Masukkan umur kamu: ")
umur = int(umur_kamu)

if umur < 7 and umur > 0:
    print("kamu masih anak-anak")
elif umur >= 7 and umur < 13:
    print("kamu masuk sekolah dasar")
elif umur >= 12 and umur < 15:
    print("kamu masuk sekolah menengah pertama")
elif umur >= 15 and umur < 18:
    print("kamu masuk sekolah menengah atas")
elif umur >= 18 and umur < 25:
    print("kamu masuk perguruan tinggi")
else:    print("kamu sedang bekerja atau sudah pensiun")

print("Pilih game kamu")
print("1. hitung luas persegi")
print("2. Tebak angka random")

pilihan_game = input("Masukkan pilihan game kamu (1/2): ")

if pilihan_game == "1":
    def hitung_luas_persegi(sisi):
        luas = sisi * sisi
        return luas
    sisi = input("Masukkan panjang sisi persegi: ")
    sisi_persegi = int(sisi)
    luas_persegi = hitung_luas_persegi(sisi_persegi)
    print("Luas persegi dengan sisi " + str(sisi_persegi) + " adalah " + str(luas_persegi))


print("Selamat bermain " + nama_kamu)
print("Semoga kamu bisa menang dalam game ini")

print("mari kita bermain tebak angka")
import random
angka_rahasia = random.randint(1, 100)
tebakan = 0
keluar = input("Apakah kamu ingin keluar? (y/n): ")
while tebakan != angka_rahasia:
    tebakan = int(input("Masukkan tebakan kamu (1-100): "))
    if tebakan < angka_rahasia:
        print("Tebakan kamu terlalu rendah")
    elif tebakan > angka_rahasia:
        print("Tebakan kamu terlalu tinggi")
    elif tebakan != angka_rahasia:
        if keluar == "y":
            print("Terima kasih sudah bermain, sampai jumpa lagi " + nama_kamu)
        else:
            print("Kamu memilih untuk melanjutkan bermain, semoga kamu bisa menang dalam game ini")
    else:
        print("Selamat! Tebakan kamu benar!")
        
point = 100

if tebakan == angka_rahasia:
    print("Kamu mendapatkan " + str(point) + " poin")
elif tebakan != angka_rahasia:
    print("Kamu mendapatkan " + str(point - 5) + " poin")
else:
    print("Kamu mendapatkan 0 poin")

print("Terima kasih sudah bermain, sampai jumpa lagi " + nama_kamu)
        