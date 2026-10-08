import json

nama_file = "data.json"

def baca_data () :

    try :
        with open (nama_file, "r", encoding="utf-8") as f :
            return json.load(f)
    except FileNotFoundError :
        return []

    except json.JSONDecodeError as e :
        if e.doc.strip () == "":
            return []

        print("[ERROR] Isi file data.json rusak / formatnya salah.")
        return []

def simpan_data (data) :
    with open (nama_file, "w", encoding="utf-8") as f :
        json.dump(data, f, indent=4)

def input_angka (pesan) :
    while True :
        try : 
            return int(input(pesan))
        except ValueError :
            print("[ERROR] Input harus berupa angka.")

def tampilkan_data () :
    data = baca_data ()
    if data is None:
        return
    if len (data) == 0 :
        print ("data barang masih kosong")
        return

    print ("===== daftar barang ====")
    nomor = 1
    for barang in data :
        nama = barang ["nama"]
        stok = barang ["stok"]
        harga = barang ["harga"]
        print(f"{nomor}. {nama} - Stok: {stok}, Harga: {harga}")
        nomor = nomor + 1

def tambah_data () :
    print ("===== tambah data barang =====")
    data = baca_data ()
    if data is None :
        return

    nama = input ("nama barang :")
    stok = input_angka ("stok barang :")
    harga = input_angka ("harga barang :")

    barang_baru = {
        "nama": nama,
        "stok": stok,
        "harga": harga
    }

    data.append(barang_baru)
    simpan_data(data)
    print ("data barang berhasil ditambahkan")

while True :
        print ("program inventaris barang")
        print ("1. tampilkan data barang")
        print ("2. tambah data barang")
        print ("3. keluar")

        pilihan = input ("pilih menu (1/2/3) :")

        if pilihan == "1" :
            tampilkan_data ()
        elif pilihan == "2" :
            tambah_data ()
        elif pilihan == "3" :
            print ("program selesai")
            break
        else :
            print ("pilihan tidak valid, silakan pilih menu 1, 2, atau 3.")