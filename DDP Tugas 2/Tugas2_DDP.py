from os import sep
import random
import string
print("***** SELAMAT DATANG DI NF BANK *****")

def menu():
    select = input("Masukkan pilihan anda: ")
    if (select == '1'):
        nama, setoran, norek = rekening()
        simpan_rekening(nama, setoran, norek)
    elif (select == '2'):
        setortunai()
        pass
    elif (select == '3'):
        tariktunai()
        pass   
    elif (select == '4'):
        transfer()
        pass
    elif (select == '5'):
        LihatTransfer()
        pass
    elif (select == '6'):
        print("Terima kasih atas kunjungan Anda...")
        pass
    else:
        print("Piliha anda salah. Mohon ulangi.")
        menu()

def rekening():
    print()
    print('*** MEMBUAT REKENING BARU ***')
    nama = input("Masukkan Nama : ")
    setoran = input("Masukkan Setoran Awal : ")
    norek = "REK" + ''.join(random.choice(string.digits) for _ in range(3))
    print(f"Pembukaan rekening dengan nomor {norek} atas nama {nama} berhasil")
    return nama, norek, setoran
#Gunawan (110220123)

def simpan_rekening(nama, norek, setoran):
    file_rek = open("nasabah.txt","a+")
    file_rek.write(norek + " " + nama + " " + setoran + "\n")
    file_rek.close()
    print()
    awal()

def setortunai():
    print()
    print('*** SETOR UANG TUNAI ***')
    rek_user = input("Masukkan nomor rekening: ")
    nominal = eval(input("Masukkan jumlah uang yang ingin disetorkan: "))
    f = open('nasabah.txt', "rt")
    dataNasabah = []
    listtransfer = []
    uang = []
    for each_line in f:
        dataNasabah.append(each_line.split())
        listtransfer.append(each_line.split())
    for y in range(len(dataNasabah)):
        uang.append(dataNasabah[y][2])
        uang = list(map(int,uang))
    for x in range(len(dataNasabah)):
        if (rek_user.upper() == listtransfer[x][0]):
                total = uang[x] + nominal
                print("Setor tunai sebesar", nominal, "dari rekening", rek_user, "berhasil")
                print("Jumlah rekening anda hanya", total)
    print()
    awal()
#belum bisa update .txt
#Muhammad Ghiyatsul Humami (110220108)

def tariktunai():
    print()
    print("*** TARIK TUNAI ***")
    rek_user = input("Masukkan nomor rekening: ")
    nominal = eval(input("Masukkan jumlah uang yang ingin ditarik: "))
    f = open('nasabah.txt')
    dataNasabah = []
    uang = []
    for each_line in f:
        dataNasabah.append(each_line.split())
    for y in range(len(dataNasabah)):
        uang.append(dataNasabah[y][2])
        uang = list(map(int,uang))
    for x in range(len(dataNasabah)):
        if rek_user.upper() in dataNasabah[x]:
            if uang[x] < nominal :
                print("Uang di rekening anda tidak cukup")
            else:
                total = uang[x] - nominal
                print("Tarik tunai sebesar", nominal, "dari rekening", rek_user, "berhasil")
                print("Sisa rekening anda hanya", total)
    print()
    awal()
#belum bisa update txt
#Ameri Yulina (11022069)

def transfer():
    print()
    print("*** TRANSFER ***")
    rek_user = input("Masukkan nomor rekening: ")
    rek_tujuan = input("Masukkan nomor rekening tujuan: ")
    nominal = eval(input("Masukkan jumlah uang yang ingin ditransfer: "))
    f = open('nasabah.txt', "a+")
    dataNasabah = []
    uang = []
    user = rek_user.upper()
    tujuan = rek_tujuan.upper()
    for each_line in f:
        dataNasabah.append(each_line.split())
    for y in range(len(dataNasabah)):
        uang.append(dataNasabah[y][2])
        uang = list(map(int,uang))
    for x in range(len(dataNasabah)):
        if dataNasabah[x][0] == rek_user.upper():
            total = uang[x] - nominal
            print(total)
        if dataNasabah[x][0] == rek_tujuan.upper():
            oke = "oke"
    print(f"Transfer sebesar {nominal} dari rekening {rek_user} ke rekening {rek_tujuan} berhasil")
    transfer = "TRF" + ''.join(random.choice(string.digits) for _ in range(3))
    txttransfer = open("transfer.txt", "a")
    txttransfer.write(transfer + " " + user + " " + tujuan + " " + str(nominal) + "\n")
    txttransfer.close()
    f.close()
    print()
    awal()
#Moh Taufiqur Rochman (110220118)

def LihatTransfer():
    print("")
    print('*** LIHAT DATA TRANSFER ***')
    rekening = input('Masukkan nomor rekening sumber transfer: ')
    listtransfer = []
    akuntransfer = []
    rekening = rekening.upper()
    f = open('transfer.txt')
    for each_line in f:
        listtransfer.append(each_line.split())
    for x in range(len(listtransfer)):
        if (listtransfer[x][1] == rekening):
           akuntransfer.append(listtransfer[x])
    if len(akuntransfer) == 0:
        print("Nomor rekening sumber tidak terdaftar.")
        print('')
        awal()
    print("Daftar transfer dari rekening", rekening)
    for y in akuntransfer:
        print(*y)
    print('')
    awal()
# Yazid Ilyas Baihaqi (110220012)

def awal():
    print("MENU :")
    print("[1] Buat rekening")
    print("[2] Setoran tunai")
    print("[3] Tarik tunai")
    print("[4] Transfer")
    print("[5] Lihat daftar transfer")
    print("[6] Keluar")
    menu()
awal()
