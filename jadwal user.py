import pandas as pd

def tampilkan_dokter(df):
    print("\nDaftar Dokter:")
    print(df.to_string(index=False))

def pilih_dokter(df, id_dokter):
    dokter = df[df["ID Dokter"] == id_dokter]
    if dokter.empty:
        print("ID Dokter tidak valid.")
        return None
    if dokter.iloc[0]["Tersedia"] == "Tidak":
        print(f"Dokter {dokter.iloc[0]['Nama Dokter']} tidak tersedia saat ini.")
        return None
    return dokter.iloc[0]

def konfirmasi_jadwal(df, id_dokter):
    dokter = pilih_dokter(df, id_dokter)
    if dokter is not None:
        print("\nDetail Jadwal Dokter:")
        print(f"Nama Dokter: {dokter['Nama Dokter']}")
        print(f"Spesialisasi: {dokter['Spesialisasi']}")
        print(f"Jadwal: {dokter['Jadwal']}")
        pilihan = input("Konfirmasi jadwal ini? (Ya/Tidak): ").strip().lower()
        if pilihan == "ya":
            print(f"Jadwal dengan Dokter {dokter['Nama Dokter']} telah dikonfirmasi.")
        else:
            print("Pemilihan jadwal dibatalkan.")

def main():
    data_dokter = pd.read_csv("dokter.csv")

    while True:
        print("\nMenu:")
        print("1. Tampilkan Daftar Dokter")
        print("2. Pilih Dokter & Jadwal")
        print("3. Keluar")

        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            tampilkan_dokter(data_dokter)
        elif pilihan == "2":
            try:
                id_dokter = int(input("Masukkan ID Dokter: "))
                konfirmasi_jadwal(data_dokter, id_dokter)
            except ValueError:
                print("Input tidak valid. Masukkan ID Dokter yang benar.")
        elif pilihan == "3":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
