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

def hitung_luas_persegi(sisi):
    luas = sisi * sisi
    return luas

sisi_persegi = input("Masukkan panjang sisi persegi: ")
sisi_persegi = int(sisi_persegi)
luas_persegi = hitung_luas_persegi(sisi_persegi)
print("Luas persegi dengan sisi " + str(sisi_persegi) + " adalah " + str(luas_persegi))

print("Pilih game kamu")
def awalGame():
    print("1. Tebak Angka")
    print("2. Tebak Kata")
    print("3. Keluar")
    pilihan = input("Masukkan pilihan kamu: ")
    if pilihan == "1":
        print("Kamu memilih Tebak Angka") 
    elif pilihan == "2":
        print("Kamu memilih Tebak Kata")
    elif pilihan == "3":
        print("Terima kasih sudah bermain")
    
    
        