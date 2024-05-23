import os
import colorama
import datetime
import pyzipper

# Mengatur warna teks menggunakan modul colorama
h = colorama.Fore.LIGHTGREEN_EX
b = colorama.Fore.LIGHTBLUE_EX
m = colorama.Fore.LIGHTRED_EX
c = colorama.Fore.LIGHTCYAN_EX
p = colorama.Fore.LIGHTWHITE_EX
k = colorama.Fore.LIGHTYELLOW_EX
r = colorama.Style.RESET_ALL

# Mendapatkan waktu saat ini
waktu_saat_ini = datetime.datetime.now()
format_waktu = waktu_saat_ini.strftime("%d-%m-%Y %H:%M:%S")

# Menampilkan informasi program
print("""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 Program : Ekstrak file zip menggunakan wordlist
 Pembuat : Rofi
 Github  : github.com/rofidoang03/zipforce
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##@@@
""")

# Meminta nama file zip dari pengguna
while True:
    file_zip = input(f"{c}[»] {p}Masukkan nama file zip: ")
    if not os.path.exists(file_zip):
        print(f"{m}[Error] {p}File {file_zip} tidak ditemukan.{r}")
    else:
        break

# Meminta nama file wordlist dari pengguna
while True:
    file_wordlist = input(f"{c}[»] {p}Masukkan nama file wordlist: ")
    if not os.path.exists(file_wordlist):
        print(f"{m}[Error] {p}File {file_wordlist} tidak ditemukan.{r}")
    else:
        break

# Membuka file wordlist dan mencoba setiap kata sandi untuk mengekstrak file zip
with open(file_wordlist, 'r', encoding="utf-8", errors="ignore") as wordlist:
    print(f"\n{b}[*] {p}Dimulai pada: {format_waktu}{r}\n")
    for kata_sandi in wordlist:
        kata_sandi = kata_sandi.strip()
        print(f"{p}Mencoba mengekstrak file zip dengan kata sandi: {k}{kata_sandi}{r}")

        # Mengekstrak file zip dengan kata sandi
        try:
            with pyzipper.AESZipFile(file_zip) as zf:
                zf.pwd = kata_sandi.encode('utf-8')
                zf.extractall()
            print(f"{p}File zip berhasil diekstrak dengan kata sandi: {h}{kata_sandi}{r}")
            break
        except Exception as e:
            print(f"{p}File zip gagal diekstrak dengan kata sandi: {m}{kata_sandi}{r}")
    print(f"\n{b}[*] {p}Berakhir pada: {format_waktu}{r}\n")
  
