def pilihanpilih() :
    pilih=(input("Masukkan kata :"))
    list=(pilih)
    len(pilih)
    if(len(pilih)%2==0) :
        print("Huruf paling ujung pada kata", pilih, "adalah", (pilih[-3:]))
    else :
        print("Huruf paling ujung pada kata", pilih, "adalah",(pilih[:3]))
    return (pilih)

pilihanpilih()
