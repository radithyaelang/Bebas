def absen():
    siswa = []
    
    print("=== Sistem Absen Sederhana ===\n")
    
    while True:
        print("\n1. Tambah Siswa")
        print("2. Lihat Daftar Absen")
        print("3. Keluar")
        
        pilihan = input("\nPilih menu (1-3): ")
        
        if pilihan == "1":
            nama = input("Masukkan nama siswa: ")
            status = input("Status (Hadir/Sakit/Izin/Alpa): ")
            siswa.append({"nama": nama, "status": status})
            print(f"✓ {nama} ditambahkan ke daftar absen")
            
        elif pilihan == "2":
            if siswa:
                print("\n--- Daftar Absen ---")
                for i, data in enumerate(siswa, 1):
                    print(f"{i}. {data['nama']} - {data['status']}")
            else:
                print("Belum ada data siswa")
                
        elif pilihan == "3":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    absen()