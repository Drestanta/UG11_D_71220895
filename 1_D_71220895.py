def pilihan():
    print("Halo Selamat datang di bioskop! ")
    print("Dimanakah kamu ingin menonton? ")
    print("1) XXI Empire")
    print("2) XXI Amplaz")
    print("3) XXI JCM")
    pilihan=int(input("Masukkan pilihanmu :"))
    if(pilihan>=4) :
        print("Pilihan tidak tersedia.")
        exit()

    print(" 1. Frozen")
    print(" 2. Keramat")
    print(" 3. KKN di Desa Penari")
    pilihan2=int(input("Pilih nomor film:"))
    if(pilihan2>=4) :
        print("Pilihan tidak tersedia.")
        exit()

    print(" 1. Reguler")
    print(" 2. Dolby almos")
    print(" 3. Premier")
    pilihan3=int(input("Pilih nomor tipe layar:"))
    if(pilihan3>=4) :
        print("Pilihan tidak tersedia.")
        exit()
    jumlahtiket=input("Berapa banyak tiket?")

    print("Mau nonton jam berapa: ")
    print(" 1. 12.35")
    print(" 2. 14.45")
    print(" 3. 16.55")
    print(" 4. 19.05")
    pilihan4 = int(input("Masukkan pilihan anda: "))
    if pilihan4 == 1 :
        print("Oke berhasil!, silahkan dinikmati di jam 12.35 ")
    elif pilihan4 == 2 :
        print("Oke berhasil!, silahkan dinikmati di jam 14.45 ")
    elif pilihan4 == 3 :
        print("Oke berhasil!, silahkan dinikmati di jam 16.55 ")
    elif pilihan4 == 4 :
        print("Oke berhasil!, silahkan dinikmati di jam 19.05")

pilihan()
