import pandas as pd

def tampilkan_dokter(df):
    print("\nDaftar Dokter:")
    print(df.to_string(index=False))

def ubah_jadwal(df):
    try:
        id_dokter = int(input("Masukkan ID Dokter yang ingin diubah jadwalnya: "))
        if id_dokter in df["ID Dokter"].values:
            print("\nInformasi jadwal saat ini:")
            dokter = df.loc[df["ID Dokter"] == id_dokter]
            print(f"Hari: {dokter['Hari'].values[0]}")
            print(f"Jam: {dokter['Jam'].values[0]}")

            hari_baru = input("Masukkan hari baru (kosongkan jika tidak ingin mengubah): ").strip().capitalize()
            jam_baru = input("Masukkan jam baru (kosongkan jika tidak ingin mengubah): ").strip()

            if hari_baru:
                df.loc[df["ID Dokter"] == id_dokter, "Hari"] = hari_baru
                print("Hari berhasil diperbarui.")
            if jam_baru:
                df.loc[df["ID Dokter"] == id_dokter, "Jam"] = jam_baru
                print("Jam berhasil diperbarui.")

            if not hari_baru and not jam_baru:
                print("Tidak ada perubahan yang dilakukan.")
            else:
                df.to_csv("jadwal_dokter.csv", index=False)
        else:
            print("ID Dokter tidak ditemukan.")
    except ValueError:
        print("Input tidak valid. Masukkan ID Dokter yang benar.")

def edit_ketersediaan(df):
    try:
        id_dokter = int(input("Masukkan ID Dokter yang ingin diubah ketersediaannya: "))
        if id_dokter in df["ID Dokter"].values:
            status_baru = input("Masukkan ketersediaan baru (Ya/Tidak): ").strip().capitalize()
            if status_baru in ["Ya", "Tidak"]:
                df.loc[df["ID Dokter"] == id_dokter, "Tersedia"] = status_baru
                df.to_csv("jadwal_dokter.csv", index=False)
                print("Ketersediaan berhasil diperbarui.")
            else:
                print("Status ketersediaan tidak valid. Harus 'Ya' atau 'Tidak'.")
        else:
            print("ID Dokter tidak ditemukan.")
    except ValueError:
        print("Input tidak valid. Masukkan ID Dokter yang benar.")

def menu_jadwal():
    data_dokter = pd.read_csv("jadwal_dokter.csv")

    while True:
        print("\nMenu:")
        print("1. Tampilkan Daftar Dokter")
        print("2. Ubah Jadwal Dokter")
        print("3. Edit Ketersediaan Dokter")
        print("4. Keluar")

        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            tampilkan_dokter(data_dokter)
        elif pilihan == "2":
            ubah_jadwal(data_dokter)
        elif pilihan == "3":
            edit_ketersediaan(data_dokter)
        elif pilihan == "4":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    menu_jadwal()
