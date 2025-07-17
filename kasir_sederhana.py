import os

total = 0
menu = []
harga = []
    
while True:
    print("Daftar Menu:\n"
    "1.  Nasi Goreng             Rp.12000 \n"
    "2.  Ayam Geprek             Rp.15000 \n"
    "3.  Mie Goreng/Rebus        Rp.5000 \n"
    "4.  Es Teh/Hangat           Rp.4000 \n"
    "5.  Es Jeruk                Rp.6500 \n"
          "") 

    while True: 
        try:
            kode = int(input("Masukkan pilihan menu :"))
            porsi = int(input("Jumlah porsi : "))
            if kode == 1:
                menu.append("Nasi Goreng")
                harga.append(12000)
                total += porsi * 12000
            elif kode == 2:
                menu.append("Ayam Geprek")
                harga.append(15000)
                total += porsi * 15000
            elif kode == 3:
                menu.append("Mie Goreng/Rebus")
                harga.append(5000)
                total += porsi * 5000
            elif kode == 4:
                menu.append("Es Teh/Hangat")
                harga.append(4000)
                total += porsi * 4000
            elif kode == 5:
                menu.append("Es Jeruk")
                harga.append(6500)
                total += porsi * 6500
            else:
                print("Kode yang dimasukkan salah")

            print("Menu yang anda pesan : ", menu)
            print("Harga menu : ", harga)
            print("Jumlah porsi : ", porsi)
            print("Total yang dibayar : ", total, '\n')


            lanjut = input("Lanjut Belanja (y/t) : ")
            if lanjut == "y":
                print("")
                break
            elif lanjut == "t":
                print("")


            bayar = int(input("Masukkan uang yang harus dibayar : "))
            if bayar > total:
                print("Kembalian : ", bayar - total)
                os._exit(0)
                break
            elif bayar == total:
                print("Uang pas")
                os._exit(0)
                break
            else:
                print("uang yang anda bayar kurang", bayar - total)
                os._exit(0)
                break
        except ValueError:
            print("Masukkan harus berupa angka.")
            break