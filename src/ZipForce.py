import os
import time
import colorama
import pyzipper

# Mengatur warna teks menggunakan modul colorama
h = colorama.Fore.LIGHTGREEN_EX
b = colorama.Fore.LIGHTBLUE_EX
m = colorama.Fore.LIGHTRED_EX
c = colorama.Fore.LIGHTCYAN_EX
p = colorama.Fore.LIGHTWHITE_EX
k = colorama.Fore.LIGHTYELLOW_EX
r = colorama.Style.RESET_ALL

os.system("clear")

print(f"""{b}
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 Program   : ZipForce
 Deskripsi : Ekstrak file zip menggunakan wordlist
 Pembuat   : Rofi
 Github    : github.com/rofidoang03/zipforce
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##@@@
{r}""")

# Meminta nama file zip dari pengguna
while True:
        file_zip = input(f"{k}[?] {p}Nama file zip: ")
        if not os.path.exists(file_zip):
                print(f"{m}[x] {p}File {file_zip} tidak ditemukan.{r}")
        else:
                print(f"{h}[+] {p}File zip {file_zip} ditemukan.{r}")
                break

# Meminta nama file wordlist dari pengguna
while True:
        file_wordlist = input(f"{k}[?] {p}Nama file wordlist: ")
        if not os.path.exists(file_wordlist):
                print(f"{m}[-] {p}File {file_wordlist} tidak ditemukan.{r}")
        else:
                print(f"{h}[+] {p}File wordlist {file_wordlist} ditemukan.{r}")
                break

# Membuka file wordlist dan mencoba setiap kata sandi untuk mengekstrak file zip
with open(file_wordlist, 'r', encoding="latin-1", errors="ignore") as wordlist:
        print("")
        time.sleep(3)
        for kata_sandi in wordlist:
                kata_sandi = kata_sandi.strip()

                # Mengekstrak file zip dengan kata sandi
                try:
                        with pyzipper.AESZipFile(file_zip) as fz:
                                fz.pwd = kata_sandi.encode('latin-1')
                                fz.extractall()
                                print(f"{h}File zip berhasil diekstrak dengan kata sandi: {kata_sandi}{r}")
                                break
                except Exception as e:
                        print(f"{m}File zip gagal diekstrak dengan kata sandi: {kata_sandi}{r}")
print("")
