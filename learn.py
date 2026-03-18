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



