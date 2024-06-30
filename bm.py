import csv

# Fungsi untuk membaca data akun dari file CSV

def rainbow_text(text):
    colors = ['', '', '', '', '', ''] 
    rainbow_text = ''
    for i in range(len(text)):
        rainbow_text += colors[i % len(colors)] + text[i]
    return rainbow_text + '' 

def load_akun():
    try:
        with open('akun.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)
    except FileNotFoundError:
        return []

# Fungsi untuk menyimpan data akun ke file CSV
def simpan_akun(akun):
    fieldnames = ['username', 'password', 'peran', 'status']
    with open('akun.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(akun)

# Fungsi untuk login
def masuk():
    print("=== Masuk ===")
    username = input("Username: ")
    password = input("Password: ")
    akun = load_akun()
    for a in akun:
        if a['username'] == username and a['password'] == password:
            if a['peran'] == 'admin' and a['status'] != 'terverifikasi':
                print("\033[91mAdmin Anda belum diverifikasi. Silakan tunggu persetujuan admin lain.")
                return None
            return a
    print("\033[91mUsername atau password salah.")
    return None

# Fungsi untuk registrasi admin baru
def daftar_admin():
    print("=== Daftar Admin Baru ===")
    username = input("Username: ")
    password = input("Password: ")
    akun = load_akun()

    existing_admins = [admin['username'] for admin in akun if admin['peran'] == 'admin']
    if username in existing_admins:
        print("\033[91mAdmin sudah terdaftar. Silakan masukkan username lain.")
        return
    akun.append({'username': username, 'password': password, 'peran': 'admin', 'status': 'belum terverifikasi'})
    simpan_akun(akun)
    print("\033[92mAdmin berhasil diajukan untuk verifikasi.")

# verif admin
def verifikasi_admin_baru():
    print("=== Verifikasi Admin Baru ===")
    username = input("Masukkan username admin yang akan diverifikasi: ")
    akun = load_akun()
    for admin in akun:
        if admin['username'] == username and admin['peran'] == 'admin' and admin['status'] == 'belum terverifikasi':
            admin['status'] = 'terverifikasi'
            simpan_akun(akun)
            print("\033[92mAdmin berhasil diverifikasi.")
            return
    print("\033[91mAdmin verifikasi tidak valid. Silakan coba lagi.")

def tambah_kategori(kategori_baru):
    with open('pertanyaan.csv', 'a', newline='') as csvfile:
        fieldnames = ['kategori', 'pertanyaan', 'pilihan1', 'pilihan2', 'pilihan3', 'pilihan4', 'skor1', 'skor2', 'skor3', 'skor4']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'kategori': kategori_baru, 'pertanyaan': 'dummy', 'pilihan1': 'dummy', 'pilihan2': 'dummy', 'pilihan3': 'dummy', 'pilihan4': 'dummy', 'skor1': '0', 'skor2': '0', 'skor3': '0', 'skor4': '0'})

# Fungsi untuk menambahkan pertanyaan baru
def tambah_pertanyaan():
    try:
        print("\nTambah Pertanyaan Baru:")
        pertanyaan_baru = {}
        
        kategori_valid = False
        while not kategori_valid:
            print("Pilih Kategori:")
            print("1. Tes Stres")
            print("2. Tes Depresi")
            print("3. Tes Gangguan Kecemasan")
            kategori_input = input("Masukkan nomor kategori (1-3): ")
            
            if kategori_input.isdigit():
                kategori_input = int(kategori_input)
                if kategori_input == 1:
                    pertanyaan_baru['kategori'] = 'Tes Stres'
                    kategori_valid = True
                elif kategori_input == 2:
                    pertanyaan_baru['kategori'] = 'Tes Depresi'
                    kategori_valid = True
                elif kategori_input == 3:
                    pertanyaan_baru['kategori'] = 'Tes Gangguan Kecemasan'
                    kategori_valid = True
                else:
                    print("\033[91mKategori tidak valid, pilih angka 1, 2, atau 3.")
            else:
                print("\033[91mInput harus berupa angka.")
        
        pertanyaan_baru['pertanyaan'] = input("Pertanyaan: ")
        pertanyaan_baru['pilihan1'] = input("Pilihan 1: ")
        pertanyaan_baru['pilihan2'] = input("Pilihan 2: ")
        pertanyaan_baru['pilihan3'] = input("Pilihan 3: ")
        pertanyaan_baru['pilihan4'] = input("Pilihan 4: ")

        skor_valid = False
        while not skor_valid:
            skor1 = input("Skor untuk Pilihan 1 (0-3): ")
            skor2 = input("Skor untuk Pilihan 2 (0-3): ")
            skor3 = input("Skor untuk Pilihan 3 (0-3): ")
            skor4 = input("Skor untuk Pilihan 4 (0-3): ")
            
            if skor1.isdigit() and skor2.isdigit() and skor3.isdigit() and skor4.isdigit():
                skor1 = int(skor1)
                skor2 = int(skor2)
                skor3 = int(skor3)
                skor4 = int(skor4)
                if 0 <= skor1 <= 3 and 0 <= skor2 <= 3 and 0 <= skor3 <= 3 and 0 <= skor4 <= 3:
                    pertanyaan_baru['skor1'] = skor1
                    pertanyaan_baru['skor2'] = skor2
                    pertanyaan_baru['skor3'] = skor3
                    pertanyaan_baru['skor4'] = skor4
                    skor_valid = True
                else:
                    print("\033[91mSemua skor harus dalam rentang 0 hingga 3.")
            else:
                print("\033[91mSemua skor harus berupa bilangan bulat.")
        
        with open('pertanyaan.csv', 'a', newline='') as csvfile:
            fieldnames = ['kategori', 'pertanyaan', 'pilihan1', 'pilihan2', 'pilihan3', 'pilihan4', 'skor1', 'skor2', 'skor3', 'skor4']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(pertanyaan_baru)
        
        print("\033[92mPertanyaan berhasil ditambahkan!")
    except KeyboardInterrupt:
        print("\033[91mTambah pertanyaan dibatalkan.")
    except Exception as e:
        print("\033[91mTerjadi kesalahan saat menambah pertanyaan.")
        print(e)
    
# kategori
def kategori_dipakai(kategori):
    with open('pertanyaan.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['kategori'] == kategori:
                return True
    return False

# Fungsi untuk melihat pertanyaan
def lihat_pertanyaan():
    try:
        with open('pertanyaan.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            pertanyaan_ditemukan = False
            for row in reader:
                print("Pertanyaan:", row['pertanyaan'])
                print("Pilihan Jawaban:")
                print("1.", row['pilihan1'])
                print("2.", row['pilihan2'])
                print("3.", row['pilihan3'])
                print("4.", row['pilihan4'])
                if 'jawaban_benar' in row:  
                    print("Jawaban Benar:", row['jawaban_benar'])
                else:
                    print("\033[91mTidak ada jawaban benar yang tersedia untuk pertanyaan ini.")
                print()
                pertanyaan_ditemukan = True

            if not pertanyaan_ditemukan:
                print("\033[91mBelum ada pertanyaan. Silakan tambahkan pertanyaan terlebih dahulu.")
    except FileNotFoundError:
        print("\033[91mBelum ada pertanyaan. Silakan tambahkan pertanyaan terlebih dahulu.")

# Fungsi untuk mengubah pertanyaan
def ubah_pertanyaan():
    try:
        print("=== Ubah Pertanyaan ===")
        lihat_pertanyaan()
        nomor_pertanyaan = int(input("Pilih nomor pertanyaan yang ingin diubah: "))
        
        pertanyaan = []
        with open('pertanyaan.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                pertanyaan.append(row)
        
        pertanyaan[nomor_pertanyaan - 1]['pertanyaan'] = input("Masukkan pertanyaan baru: ")
        for i in range(4):
            pertanyaan[nomor_pertanyaan - 1][f'pilihan{i+1}'] = input(f"Masukkan pilihan jawaban ke-{i+1} baru: ")
        pertanyaan[nomor_pertanyaan - 1]['jawaban_benar'] = input("Masukkan nomor pilihan jawaban yang benar baru: ")
        
        with open('pertanyaan.csv', 'w', newline='') as csvfile:
            fieldnames = ['pertanyaan', 'pilihan1', 'pilihan2', 'pilihan3', 'pilihan4', 'jawaban_benar', 'skor', 'kategori']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(pertanyaan)
        
        print("\033[92mPertanyaan berhasil diubah.")
    except FileNotFoundError:
        print("\033[91mBelum ada pertanyaan. Silakan tambahkan pertanyaan terlebih dahulu.")

# Fungsi untuk melihat feedback
def lihat_feedback():
    try:
        with open('feedback.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            print("Feedback dari Pengguna:")
            for row in reader:
                print(row['feedback'])
    except FileNotFoundError:
        print("\033[91mBelum ada feedback dari pengguna.")

        
# Fungsi untuk melihat riwayat kuis pengguna
def lihat_riwayat_kuis(username):
    try:
        with open('riwayat_kuis.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            print(f"Riwayat Kuis untuk Pengguna {username}:")
            for row in reader:
                if row['username'] == username:
                    print("Pertanyaan:", row['pertanyaan'])
                    print("Jawaban Pengguna:", row['jawaban_pengguna'])
                    print("Jawaban Benar:", row['jawaban_benar'])
                    if row['jawaban_pengguna'] == row['jawaban_benar']:
                        print("\033[92mHasil: Benar")
                    else:
                        print("\033[91mHasil: Salah")
                    print()
    except FileNotFoundError:
        print("\033[91mBelum ada riwayat kuis untuk pengguna ini.")

def hitung_bobot(skor, total_pertanyaan):
    persentase_skor = (skor / (total_pertanyaan * 3)) * 100
    if persentase_skor <= 30:
        return 'Ringan'
    elif persentase_skor <= 60:
        return 'Sedang'
    else:
        return 'Berat'

# Rekap skor
def lihat_rekap_skor_pengguna():
    try:
        with open('riwayat_kuis.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            rekap_skor = {}
            for row in reader:
                username = row['username']
                if username not in rekap_skor:
                    rekap_skor[username] = {'skor': 0, 'tanggal': []}
                rekap_skor[username]['skor'] += int(row['jawaban_pengguna'] == row['jawaban_benar'])
                rekap_skor[username]['tanggal'].append(row['tanggal'])
                
            sorted_rekap_skor = bubble_sort_rekap_skor(rekap_skor)
            for pengguna, data in sorted_rekap_skor:
                bobot = hitung_bobot(data['skor'])
                print(f"Username: {pengguna}")
                print(f"Total Skor: {data['skor']}")
                print(f"Bobot: {bobot}")
                if len(data['tanggal']) > 10:
                    print("Tanggal (Descending):")
                    tanggal_sorted = sorted(data['tanggal'], reverse=True)
                    for tanggal in tanggal_sorted:
                        print(tanggal)
                print()
    except FileNotFoundError:
        print("\033[91mBelum ada riwayat kuis untuk pengguna.")


# sorting
def bubble_sort_rekap_skor(rekap_skor):
    pengguna_skor = list(rekap_skor.items())
    n = len(pengguna_skor)
    for i in range(n):
        for j in range(0, n-i-1):
            if pengguna_skor[j][1]['skor'] < pengguna_skor[j+1][1]['skor']:
                pengguna_skor[j], pengguna_skor[j+1] = pengguna_skor[j+1], pengguna_skor[j]
    return pengguna_skor


def kuis_pengguna(username):
    try:
        print("=== Kuis Pengguna ===")
        print("Selamat datang di kuis! Silakan pilih kategori pertanyaan:")
        kategori_set = tampilkan_kategori()
        kategori = input("Masukkan kategori pertanyaan (atau masukkan kategori baru): ")

        if kategori not in kategori_set:
            tambah_kategori(kategori)
        
        print("\nSilakan jawab pertanyaan berikut:")
        pertanyaan = []
        with open('pertanyaan.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['kategori'] == kategori:
                    pertanyaan.append(row)

        jumlah_jawaban_benar = 0
        total_pertanyaan = len(pertanyaan)
        skor = 0
        with open('riwayat_kuis.csv', 'a', newline='') as csvfile:
            fieldnames = ['username', 'tanggal', 'pertanyaan', 'jawaban_pengguna', 'jawaban_benar', 'skor']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            for pertanyaan in pertanyaan:
                print("\nPertanyaan:", pertanyaan['pertanyaan'])
                print("Pilihan Jawaban:")
                print("1.", pertanyaan['pilihan1'])
                print("2.", pertanyaan['pilihan2'])
                print("3.", pertanyaan['pilihan3'])
                print("4.", pertanyaan['pilihan4'])
                jawaban_pengguna = input("Masukkan nomor pilihan jawaban Anda: ")
                jawaban_benar = pertanyaan.get('jawaban_benar', '')  
                skor_jawaban = int(pertanyaan.get(f'skor{jawaban_pengguna}', 0))

                writer.writerow({'username': username, 'tanggal': 'date', 'pertanyaan': pertanyaan['pertanyaan'], 'jawaban_pengguna': jawaban_pengguna, 'jawaban_benar': jawaban_benar, 'skor': skor_jawaban})

                if jawaban_pengguna == jawaban_benar:
                    jumlah_jawaban_benar += 1
                    skor += skor_jawaban

            print("\nKuis selesai!")
            if total_pertanyaan > 0:
                print("Total pertanyaan:", total_pertanyaan)
            else:
                print("Tidak ada pertanyaan untuk kategori yang dipilih.")
            with open('riwayat_kuis.csv', 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                rows = list(reader)
            with open('riwayat_kuis.csv', 'a', newline='') as csvfile:
                fieldnames = ['username', 'tanggal', 'pertanyaan', 'jawaban_pengguna', 'jawaban_benar', 'skor']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                for row in rows:
                    if row['username'] == username and row['skor'] == '0':
                        row['skor'] = str(skor)
                    writer.writerow(row)

                else:
                    print("Tidak ada pertanyaan untuk kategori yang dipilih.")

        if skor >= 0 and skor <= 50:
            print("\033[91mPembahasan: Anda mengalami depresi sedang.")

    except FileNotFoundError:
        print("\033[91mFile pertanyaan tidak ditemukan.")

# Fungsi untuk memberikan feedback
def beri_feedback():
    print("=== Beri Feedback ===")
    feedback = input("Masukkan feedback Anda: ")
    
    with open('feedback.csv', 'a', newline='') as csvfile:
        fieldnames = ['feedback']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'feedback': feedback})
    
    print("\033[92mFeedback Anda telah disimpan.")

# Fungsi untuk mencari pertanyaan berdasarkan kategori
def cari_pertanyaan_berdasarkan_kategori(kategori):
    print("Cari Pertanyaan Berdasarkan Kategori:")
    with open('pertanyaan.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['kategori'] == kategori:
                print("Pertanyaan: ", row['pertanyaan'])
                if 'pilihan' in row:  
                    print("Pilihan: ", row['pilihan'])
                else:
                    print("Pilihan: Tidak ada")
                print("Jawaban Benar: ", row.get('jawaban_benar', 'Tidak ada jawaban benar'))

# Fungsi untuk menjalankan program kuis
def main():
    while True:
        print("\n\033[95mSelamat datang!\033[0m")
        print("\033[95m1. Masuk\033[0m")
        print("\033[95m2. Daftar Admin\033[0m")
        print("\033[95m3. Daftar Pengguna\033[0m")
        pilihan = input("\033[95mPilihan: \033[0m")
        
        if pilihan == '1':
            pengguna = masuk()
            if pengguna:
                if pengguna['peran'] == 'admin':
                    menu_admin(pengguna)
                else:
                    menu_pengguna(pengguna)
            else:
                print("\033[91mMasuk gagal. Coba lagi.\033[0m")
        elif pilihan == '2':
            daftar_admin()
        elif pilihan == '3':
            daftar_pengguna()
        else:
            print("\033[91mpilihan tidak valid\033[0m")

def tampilkan_kategori():
    print("=== Daftar Kategori Pertanyaan ===")
    kategori_set = set() 
    with open('pertanyaan.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            kategori_set.add(row['kategori'])
    print("Kategori yang tersedia:")
    for idx, kategori in enumerate(kategori_set):
        print(f"{idx+1}. {kategori}")
    return kategori_set

# searching
def cari_indeks(arr, target, batas_bawah, batas_atas):
    if batas_bawah > batas_atas:
        return -1
    mid = (batas_bawah + batas_atas) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return cari_indeks(arr, target, batas_bawah, mid - 1)
    else:
        return cari_indeks(arr, target, mid + 1, batas_atas)

# Daftar Pengguna
def daftar_pengguna():
    print("=== Pendaftaran Pengguna Baru ===")
    username = input("Username: ")
    password = input("Password: ")
    akun = load_akun()
    
    existing_users = [user['username'] for user in akun]
    if username in existing_users:
        print("\033[91mUsername sudah terdaftar. Silakan masukkan username lain.")
        return
    akun.append({'username': username, 'password': password, 'peran': 'user', 'status': 'terverifikasi'})
    simpan_akun(akun)
    print("\033[92mPendaftaran berhasil. Anda dapat login sekarang.")

def tambahkan_header(filename, fieldnames):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        if not lines:
            with open(filename, 'w') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
    except FileNotFoundError:
        with open(filename, 'w') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

tambahkan_header('feedback.csv', ['feedback'])
tambahkan_header('riwayat_kuis.csv', ['username', 'tanggal', 'pertanyaan', 'jawaban_pengguna', 'jawaban_benar'])
tambahkan_header('pertanyaan.csv', ['kategori', 'pertanyaan', 'pilihan1', 'pilihan2', 'pilihan3', 'pilihan4', 'skor1', 'skor2', 'skor3', 'skor4'])
tambahkan_header('akun.csv', ['username', 'password', 'peran', 'status'])

#lihat pengguna
def lihat_pengguna():
    try:
        with open('akun.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            print("=== Daftar Pengguna ===")
            for row in reader:
                if row['peran'] != 'admin':
                    print(f"Username: {row['username']}, Status: {row['status']}")
    except FileNotFoundError:
        print("\033[91mFile akun tidak ditemukan.")

# Fungsi untuk mengubah informasi pengguna
def ubah_pengguna():
    print("=== Ubah Informasi Pengguna ===")
    username = input("Masukkan username pengguna yang ingin diubah: ")
    status_baru = input("Masukkan status baru (terverifikasi/belum terverifikasi): ")
    akun = load_akun()
    for user in akun:
        if user['username'] == username and user['peran'] == 'user':
            user['status'] = status_baru
            simpan_akun(akun)
            print("\033[92mInformasi pengguna berhasil diubah.")
            return
    print("\033[91mPengguna tidak ditemukan atau bukan pengguna.")

# Fungsi untuk menghapus pengguna
def hapus_pengguna():
    print("=== Hapus Pengguna ===")
    username = input("Masukkan username pengguna yang ingin dihapus: ")
    akun = load_akun()
    new_akun = [user for user in akun if not (user['username'] == username and user['peran'] == 'user')]
    if len(new_akun) < len(akun):
        simpan_akun(new_akun)
        print("\033[92mPengguna berhasil dihapus.")
    else:
        print("\033[91mPengguna tidak ditemukan atau bukan pengguna.")


# Menu admin
def menu_admin(pengguna):
    while True:
        print("\nMenu Admin:")
        print(rainbow_text("1. Tambah Pertanyaan"))
        print(rainbow_text("2. Lihat Pertanyaan"))
        print(rainbow_text("3. Ubah Pertanyaan"))
        print(rainbow_text("4. Lihat Feedback"))
        print(rainbow_text("5. Lihat Rekap Skor Pengguna"))
        print(rainbow_text("6. Verifikasi Admin Baru"))
        print(rainbow_text("7. Lihat Pengguna"))
        print(rainbow_text("8. Ubah Informasi Pengguna"))
        print(rainbow_text("9. Hapus Pengguna"))
        print(rainbow_text("10. Logout"))
        pilihan_admin = input(rainbow_text("Pilihan: "))
        
        if pilihan_admin == '1':
            tambah_pertanyaan()
        elif pilihan_admin == '2':
            lihat_pertanyaan()
        elif pilihan_admin == '3':
            ubah_pertanyaan()
        elif pilihan_admin == '4':
            lihat_feedback()
        elif pilihan_admin == '5':
            lihat_rekap_skor_pengguna()
        elif pilihan_admin == '6':
            verifikasi_admin_baru()
        elif pilihan_admin == '7':
            lihat_pengguna()
        elif pilihan_admin == '8':
            ubah_pengguna()
        elif pilihan_admin == '9':
            hapus_pengguna()
        elif pilihan_admin == '10':
            print(rainbow_text("\033[92mLogout berhasil."))
            break
        else:
            print(rainbow_text("\033[91mPilihan tidak valid."))

# Menu pengguna
def menu_pengguna(pengguna):
    while True:
        print("\nMenu Pengguna:")
        print(rainbow_text("1. Jalankan Kuis"))
        print(rainbow_text("2. Beri Feedback"))
        print(rainbow_text("3. Lihat Riwayat Kuis"))
        print(rainbow_text("4. Logout"))
        pilihan_pengguna = input(rainbow_text("Pilihan: "))
        
        if pilihan_pengguna == '1':
            kuis_pengguna(pengguna['username'])
        elif pilihan_pengguna == '2':
            beri_feedback()
        elif pilihan_pengguna == '3':
            lihat_riwayat_kuis(pengguna['username'])
        elif pilihan_pengguna == '4':
            print(rainbow_text("\033[92mLogout berhasil."))
            break
        else:
            print(rainbow_text("\033[91mPilihan tidak valid."))

if __name__ == "__main__":
    main()