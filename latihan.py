class Mobil:
    def _init_(self,merek,warna,model,tahun):
        self.merek = merek
        self.warna = warna
        self.model = model
        self.tahun = tahun
        self.kecepatan = 0
        self.mesin_hidup = False
    def nyalakan_mesin (self):
        """methode untuk menyalakan mesin"""
        if not self.mesin_hidup:
            self.mesin_hidup = True
            print(f"mesin mobil {self.merek}  {self.model} dinyalakan!")
        else:
            print("mesin sudah hidup")

    def matikan_mesin(self):
        """methode unutk mematikan mesin"""
        if self.mesin_hidup and self.kecepatan == 0:
            self.mesin_hidup = False
            print(f"mesin {self.merek}  {self.model} dimatikan!")
        elif self.kecepatan > 0 :
            print("kurangi kecepatan mesin terlebih dahulu untuk mematikan mesin!")
        else:
            print('mesin sudah mati')

    def gas(self, tambah_kecepatan):
        """Methode untuk menambahkan kecepatan"""
        if self.mesin_hidup:
            self.kecepatan += tambah_kecepatan
            print(f"kecepatan sekarang : {self.kecepatan}")
        else:
            print("silahkan nyalakan mobil terlebih dahulu! ")

    def rem(self, kurangi_keceptan):
        """methode untuk mengurangi kecepatan"""
        if self.kecepatan >= kurangi_keceptan:
            self.kecepatan -= kurangi_keceptan
            print(f"kecepatan sekarang:{self.kecepatan} km/h")
        else:
            self.kecepatan = 10
            print("mobil telah berhenti!")

    def info_Mobil(self):
            """methode untuk menampilkan informasi mobil"""

            status_mesin = "hidup" if self.mesin_hidup else "mati"
            print(f"""
                INFO MOBIL :
                Merek : {self.merek}
                model : {self.model}
                tahun : {self.tahun}
                warna : {self.warna}
                kecepatan : {self.kecepatan} km/h 
                status mesin: {status_mesin}
                    """)


mobil_afri = Mobil("Honda", "Hitam", "CRV", 2012)
mobil_lama = Mobil("Toyota ", "Hitam", "cefat rusak", 2009)


mobil_afri.info_Mobil()
mobil_afri.nyalakan_mesin ()
mobil_lama.gas(10)
mobil_afri.rem(40)
mobil_afri.matikan_mesin()