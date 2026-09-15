buku = {
    "judul": "Funiculi Funicula",
    "penulis": "Toshikazu Kawaguchi",
    "tahun": 2015
}

while True:
    print("Pengelola buku sang Andi")
    print("1. Tampilkan data buku")
    print("2. Tambahkan data penerbit buku")
    print("3. Ubah penulis buku")
    print("4. Hapus data penerbit buku")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan menu (1-5): ")

    if pilihan == "1":
        print("Data buku:")
        print("Judul:", buku["judul"])
        print("Penulis:", buku["penulis"])
        print("Tahun:", buku["tahun"])

        if "penerbit" in buku:
            print("Penerbit:", buku["penerbit"])

    elif pilihan == "2":
        penerbit = input("Masukkan nama penerbit buku: ")
        buku["penerbit"] = penerbit
        print("Data penerbit dari buku berhasil ditambahkan.")
        print("Penerbit:", buku["penerbit"])

    elif pilihan == "3":
        penulis_buku_baru = input("Masukkan nama penulis buku yang baru: ")

        while penulis_buku_baru == "":
            print("Nama penulis jangan kosong ya, gaada buku tanpa penulis")
            penulis_buku_baru = input("Masukkan nama penulis buku yang baru: ")

        buku["penulis"] = penulis_buku_baru
        print("Data penulis dari buku berhasil diubah.")

    elif pilihan == "4":
        if "penerbit" in buku:
            del buku["penerbit"]
            print("Data penerbit dari buku berhasil dihapus, sanak.")
        else:
            print("Data penerbit gaada bos, cari lagi ya.")

    elif pilihan == "5":
        print("Anda telah keluar dari program ini bos, makasih udah make ini program.")
        break
