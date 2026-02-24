# Simulasi Buku Telepon Sederhana

def tampilkan_menu():
    print("\n===== MENU BUKU TELEPON =====")
    print("1. Tambah Kontak")
    print("2. Lihat Semua Kontak")
    print("3. Cari Kontak")
    print("4. Ubah Kontak")
    print("5. Hapus Kontak")
    print("6. Keluar")

def tambah_kontak(buku_telepon):
    nama = input("Masukkan nama: ")
    if nama in buku_telepon:
        print("Kontak sudah ada!")
    else:
        nomor = input("Masukkan nomor telepon: ")
        buku_telepon[nama] = nomor
        print("Kontak berhasil ditambahkan.")

def lihat_kontak(buku_telepon):
    if not buku_telepon:
        print("Buku telepon kosong.")
    else:
        print("\nDaftar Kontak:")
        for nama, nomor in buku_telepon.items():
            print(f"{nama} : {nomor}")

def cari_kontak(buku_telepon):
    nama = input("Masukkan nama yang dicari: ")
    if nama in buku_telepon:
        print(f"Nomor telepon {nama} adalah {buku_telepon[nama]}")
    else:
        print("Kontak tidak ditemukan.")

def ubah_kontak(buku_telepon):
    nama = input("Masukkan nama yang ingin diubah: ")
    if nama in buku_telepon:
        nomor_baru = input("Masukkan nomor telepon baru: ")
        buku_telepon[nama] = nomor_baru
        print("Kontak berhasil diperbarui.")
    else:
        print("Kontak tidak ditemukan.")

def hapus_kontak(buku_telepon):
    nama = input("Masukkan nama yang ingin dihapus: ")
    if nama in buku_telepon:
        del buku_telepon[nama]
        print("Kontak berhasil dihapus.")
    else:
        print("Kontak tidak ditemukan.")

# Program utama
buku_telepon = {}

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        tambah_kontak(buku_telepon)
    elif pilihan == "2":
        lihat_kontak(buku_telepon)
    elif pilihan == "3":
        cari_kontak(buku_telepon)
    elif pilihan == "4":
        ubah_kontak(buku_telepon)
    elif pilihan == "5":
        hapus_kontak(buku_telepon)
    elif pilihan == "6":
        print("Terima kasih telah menggunakan Buku Telepon.")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")