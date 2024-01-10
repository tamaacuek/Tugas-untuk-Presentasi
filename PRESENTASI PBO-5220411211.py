class Farm:
    def __init__(self, jenis_tanah, tempat_menanam, lama_panen):
        self.jenis_tanah = jenis_tanah
        self.tempat_menanam = tempat_menanam
        self.lama_panen = lama_panen
       
class Jagung(Farm):
    def __init__(self, jenis_tanah, tempat_menanam, lama_panen, 
                 cara_menanam, benih):
        super().__init__(jenis_tanah, tempat_menanam, lama_panen)
        self.cara_menanam = cara_menanam
        self.benih = benih
        

    def tambah_benih(self, new_benih):
        self.benih.append(new_benih)

    def hapus_benih(self, old_benih):
        if old_benih in self.benih:
            self.benih.remove(old_benih)
    def info(self):
        return f"Jagung ditanam di {self.tempat_menanam} dengan benih {', '.join(self.benih)}\n" \
               f"Jenis Tanah: {self.jenis_tanah}\n " \
               f"lama Panen: {self.lama_panen}\n " \
               f"Cara menanam: {self.cara_menanam}\n " \
              
class Padi(Farm):
    def __init__(self, jenis_tanah, tempat_menanam, lama_panen, jenis_padi):
        super().__init__(jenis_tanah, tempat_menanam, lama_panen)
        self.jenis_padi = jenis_padi
        self.status_tanam= False
    
    def start_farm(self):
        self.status_tanam = True
        print(f"{self.jenis_padi} telah ditanam.")

    def stop_farm(self):
        self.status_tanam = False
        print(f"{self.jenis_padi} layu.")

    def panen(self):
        if self.status_tanam:
            print(f"{self.jenis_padi} sedang dipanen!")
        else:
            print(f"Untuk memanen padi, tanam terlebih dahulu.")
    def info(self):
        return f"Padi ditanam di {self.tempat_menanam} dengan benih {self.jenis_padi}\n" \
               f"Jenis Tanah: {self.jenis_tanah}\n " \
               f"lama Panen: {self.lama_panen}\n " \
               f"Status Tanam: {'Sedang ditanam' if self.status_tanam else 'Belum ditanam'}"
    
class Padi_Hibrida(Padi):
    def __init__(self, jenis_tanah, tempat_menanam, lama_panen, jenis_padi, jenis_air):
        super().__init__(jenis_tanah, tempat_menanam, lama_panen, jenis_padi)
        self.jenis_air = jenis_air

    def siram(self):
        if self.status_tanam:
            print(f"Padi {self.jenis_padi} sedang disirami dengan air {self.jenis_air} ")
        else:
            print(f"Untuk menyiram, tanam padi terlebih dahulu!")

    def info(self):
        return f"Padi ditanam di {self.tempat_menanam} dengan benih {self.jenis_padi}\n" \
               f"Jenis Tanah: {self.jenis_tanah}\n " \
               f"lama Panen: {self.lama_panen}\n " \
               f"Status Tanam: {'Sedang ditanam' if self.status_tanam else 'Belum ditanam'}"
        

def kontrol_jagung():
    jenis_tanah = input("Masukkan jenis tanah: ")
    tempat_menanam = input("Masukkan tempat menanam: ")
    lama_panen = int(input("Masukkan lama panen (bulan): "))
    cara_menanam = input("Masukkan cara menanam: ")
    benih = input("Masukkan benih (pisahkan dengan koma jika lebih dari satu): ").split(',')
    
    jagung = Jagung(jenis_tanah, tempat_menanam, lama_panen, cara_menanam, benih)
    
    while True:
        print("========= Jagung =======")
        print("1. Tambah benih")
        print("2. Hapus benih")
        print("3. Informasi")
        print("4. Kembali")

        choice = input("Pilih menu (1-4): ")

        if choice == "1":
            new_benih = input("Masukkan benih baru: ")
            jagung.tambah_benih(new_benih)
            print(f"Benih {new_benih} berhasil ditambahkan!")

        elif choice == "2":
            old_benih = input("Masukkan benih yang ingin dihapus: ")
            jagung.hapus_benih(old_benih)
            print(f"Benih {old_benih} berhasil dihapus!")

        elif choice == "3":
            print(jagung.info())

        elif choice == "4":
            break

def kontrol_padi():
    jenis_padi = input("Masukkan jenis padi: ")
    tempat_menanam = input("Masukkan tempat menanam: ")
    jenis_tanah = input("Masukkan jenis tanah: ")
    lama_panen = int(input("Masukkan lama panen (bulan): "))
    padi = Padi(jenis_tanah, tempat_menanam, lama_panen, jenis_padi)
    
    while True:
        print("========= Padi =======")
        print("1. Start farm")
        print("2. Stop farm")
        print("3. Panen")
        print("4. Informasi")
        print("5. Kembali")

        choice = input("Pilih menu (1-5): ")

        if choice == "1":
            padi.start_farm()
            
        elif choice == "2":
            padi.stop_farm()
        
        elif choice == "3":
            padi.panen()
        
        elif choice == "4":
            print(padi.info())
        
        elif choice == "5":
            break

def kontrol_padi_hibrida():
    jenis_tanah = input("Masukkan jenis tanah: ")
    tempat_menanam = input("Masukkan tempat menanam: ")
    lama_panen = int(input("Masukkan lama panen (bulan): "))
    jenis_padi = input("Masukkan jenis padi: ")
    jenis_air = input("Masukkan jenis air: ")
    
    padi_hibrida = Padi_Hibrida(jenis_tanah, tempat_menanam, lama_panen, jenis_padi, jenis_air)
    
    while True:
        print("========= Padi Hibrida =======")
        print("1. Siram")
        print("2. Tanam Padi")
        print("3. Stop menanam")
        print("4. Panen Padi")
        print("5. Informasi")
        print("6. Kembali")

        choice = input("Pilih menu (1-3): ")

        if choice == "1":
            padi_hibrida.siram()

        elif choice == "2":
            padi_hibrida.start_farm()
        
        elif choice == "3":
            padi_hibrida.stop_farm()

        elif choice == "4":
            padi_hibrida.panen()
            
        elif choice == "5":
            print(padi_hibrida.info())
        


        elif choice == "6":
            break

def main():
    while True:
        print("Menu:")
        print("1. Jagung")
        print("2. Padi")
        print("3. Padi Hibrida")
        print("4. Keluar")

        choice = input("Pilih menu (1-4): ")

        if choice == "1":
            kontrol_jagung()

        elif choice == "2":
            kontrol_padi()

        elif choice == "3":
            kontrol_padi_hibrida()
        
        elif choice == "4":
            print("Program selesai")
            break
        
        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")

if __name__ == "__main__":
    main()
