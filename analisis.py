def analisis_finansial(data):
    """Fungsi untuk menganalisis performa finansial dari dataset"""
    total_pendapatan = sum([item['pendapatan'] for item in data])
    total_pengeluaran = sum([item['pengeluaran'] for item in data])
    net_income = total_pendapatan - total_pengeluaran
    
    print(f"Total Pendapatan: {total_pendapatan}")
    print(f"Total Pengeluaran: {total_pengeluaran}")
    print(f"Net Income (Pendapatan Bersih): {net_income}")
    
    if net_income > 0:
        print("Kinerja keuangan positif (untung).")
    elif net_income < 0:
        print("Kinerja keuangan negatif (rugi).")
    else:
        print("Kinerja keuangan netral (break even).")
    
    # Analisis bulanan
    for bulan in data:
        print(f"\nBulan: {bulan['bulan']}")
        print(f"Pendapatan: {bulan['pendapatan']}")
        print(f"Pengeluaran: {bulan['pengeluaran']}")
        surplus = bulan['pendapatan'] - bulan['pengeluaran']
        if surplus > 0:
            print("Status: Surplus")
        elif surplus < 0:
            print("Status: Defisit")
        else:
            print("Status: Break Even")

def input_data():
    """Fungsi untuk menginput data keuangan pengguna"""
    data = []
    bulan_list = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    
    for bulan in bulan_list:
        print(f"\nInput data untuk bulan: {bulan}")
        pendapatan = float(input("Masukkan pendapatan: "))
        pengeluaran = float(input("Masukkan pengeluaran: "))
        data.append({"bulan": bulan, "pendapatan": pendapatan, "pengeluaran": pengeluaran})
    
    return data

def menu():
    """Menu utama program"""
    while True:
        print("\n--- Menu Program Analisis Finansial ---")
        print("1. Input Data Keuangan")
        print("2. Analisis Data Keuangan")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ")
        
        if pilihan == "1":
            global data_finansial
            data_finansial = input_data()
        elif pilihan == "2":
            if not data_finansial:
                print("Data keuangan belum diinput. Silakan pilih menu 1 untuk mengisi data.")
            else:
                analisis_finansial(data_finansial)
        elif pilihan == "3":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Variabel global untuk menyimpan data finansial
data_finansial = []

# Menjalankan menu utama
menu()