import pandas as pd

def login_dokter():
    df_dokter = pd.read_csv("data_dokter.csv")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    dokter = df_dokter[(df_dokter["Username"] == username) & (df_dokter["Password"] == password)]
    
    if dokter.empty:
        print("Username atau password salah.")
        return None
    else:
        print(f"Selamat datang, {dokter.iloc[0]['Nama Dokter']}!")
        return dokter.iloc[0]["ID Dokter"]

def lihat_dan_edit_jadwal(id_dokter):
    df_jadwal = pd.read_csv("jadwal_dokter.csv")
    jadwal_dokter = df_jadwal[df_jadwal["ID Dokter"] == id_dokter]
    
    if jadwal_dokter.empty:
        print("Tidak ada jadwal untuk dokter ini.")
    else:
        print("\nJadwal Anda:")
        print(jadwal_dokter.to_string(index=False))

        edit = input("\nApakah Anda ingin mengedit jadwal? (y/n): ").lower()
        if edit == "y":
            id_jadwal = int(input("Masukkan ID Jadwal yang ingin diubah: "))
            jadwal_baru = input("Masukkan jadwal baru: ")
            df_jadwal.loc[df_jadwal["ID Dokter"] == id_dokter, "Jadwal"] = jadwal_baru
            df_jadwal.to_csv("jadwal_dokter", index=False)
            print("Jadwal berhasil diperbarui.")
        else:
            print("Jadwal tidak diubah.")

def diagnosa_pasien():
    df_pasien = pd.read_csv("pasien.csv")
    nik_pasien = int(input("Masukkan NIK Pasien: "))
    pasien = df_pasien[df_pasien["nik"] == nik_pasien]
    
    if pasien.empty:
        print("Pasien tidak ditemukan.")
        return
    
    print(f"\nData Pasien: {pasien.iloc[0]['name']}, Umur: {pasien.iloc[0]['age']}")

    diagnosa = input("Masukkan Diagnosa: ")
    tindakan = input("Masukkan Tindakan (Rawat Inap/Resep Obat): ").lower()

    df_diagnosa = pd.read_csv("data_diagnosa.csv")
    new_diagnosa = pd.DataFrame({
        "NIK Pasien": [nik_pasien],
        "Diagnosa": [diagnosa],
        "Tindakan": [tindakan.capitalize()]
    })
    df_diagnosa = pd.concat([df_diagnosa, new_diagnosa], ignore_index=True)
    df_diagnosa.to_csv("data_diagnosa.csv", index=False)

    print(f"Diagnosa untuk pasien {pasien.iloc[0]['name']} telah dicatat.")

    if tindakan == "rawat inap":
        atur_rawat_inap()
    elif tindakan == "resep obat":
        atur_resep_obat()
    else:
        print("Tindakan tidak dikenali.")

def atur_rawat_inap():
    df_rawat_inap = pd.read_csv("data_kamar.csv")
    print("\nDaftar Kamar Rawat Inap:")
    print(df_rawat_inap.to_string(index=False))
    
    nomor_kamar = int(input("\nMasukkan Nomor Kamar untuk rawat inap: "))
    kamar = df_rawat_inap[df_rawat_inap["Nomor Kamar"] == nomor_kamar]
    
    if not kamar.empty and kamar.iloc[0]["Status"] == "Kosong":
        df_rawat_inap.loc[df_rawat_inap["Nomor Kamar"] == nomor_kamar, "Status"] = "Terisi"
        df_rawat_inap.to_csv("data_kamar.csv", index=False)
        print(f"Kamar {nomor_kamar} telah diatur untuk pasien.")
    else:
        print("Kamar tidak tersedia atau sudah terisi.")

def atur_resep_obat():
    obat = input("Masukkan nama obat yang diresepkan: ")
    dosis = input("Masukkan dosis obat: ")
    durasi = input("Masukkan durasi penggunaan obat (misal: 5 hari): ")

    print(f"Resep obat untuk pasien: {obat}, Dosis: {dosis}, Durasi: {durasi} telah dicatat.")


def main():
    id_dokter = login_dokter()
    if not id_dokter:
        return
    
    while True:
        print("\nMenu:")
        print("1. Lihat dan Edit Jadwal Dokter")
        print("2. Mendiagnosa Pasien")
        print("3. Keluar")
        
        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            lihat_dan_edit_jadwal(id_dokter)
        elif pilihan == "2":
            diagnosa_pasien()
        elif pilihan == "3":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
