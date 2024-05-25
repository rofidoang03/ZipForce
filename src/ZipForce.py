#!/usr/bin/env python3
# Nama Program............: ZipForce
# Deskripsi Program.......: Ekstraksi pada file zip yang terlindungi oleh kata sandi dengan menggunakan wordlist.
# Pembuat Program.........: Rofi
# Github..................: https://github.com/rofidoang03/ZipForce

import os
import sys
import time
import hashlib

# Jika terjadi error saat menginstal modul
# Gunakan perintah ini:
# 1. python3 -m venv modul
# 2. source modul/bin/activate
# 3. pip3 install <modul>
#
# Misalnya: pip3 install colorama 

try:
        # Modul colorama digunakan untuk menambahkan warna 
        # dan gaya ke teks di terminal.
        import colorama
except ImportError:
        print("Error: Modul colorama belum diinstal. Mohon instal dengan menjalankan perintah 'pip3 install colorama'.")
        sys.exit(1)
try:
        # Modul pyzipper digunakan  untuk mengompresi 
        # dan mengekstrak file dan data menggunakan format ZIP.
        import pyzipper
except ImportError:
        print("Error: Modul pyzipper belum diinstal. Mohon instal dengan menjalankan perintah 'pip3 install pyzipper'.")
        sys.exit(1)

# Variabel untuk mengatur warna output teks menggunakan modul colorama.
h = colorama.Fore.LIGHTGREEN_EX  # Hijau terang 
b = colorama.Fore.LIGHTBLUE_EX   # Biru terang 
m = colorama.Fore.LIGHTRED_EX    # Merah terang 
c = colorama.Fore.LIGHTCYAN_EX   # Cyan terang 
p = colorama.Fore.LIGHTWHITE_EX  # Putih terang 
k = colorama.Fore.LIGHTYELLOW_EX # Kuning terang 
r = colorama.Style.RESET_ALL     # Reset 

def banner():
        print(f"""
{b}Ekstrak file zip yang dilindungi kata sandi menggunakan wordlist{r}
{k}Dibuat oleh {p}: Rofi{r}
{k}Github {p}: https://github.com/rofidoang03/ZipForce/{r}
""")

def ekstrak_file_zip(file_zip, file_log, folder, file_wordlist):
        # Membuka file wordlist dengan encoding latin-1.
        with open(file_wordlist, 'r', encoding="latin-1", errors="ignore") as wordlist:
                print(f"\n{b}[*] {p}Mulai ekstraksi. Saat dimulai tekan [CTRL+C] untuk berhenti.{r}\n")
                time.sleep(3)
                # Membaca setiap kata sandi dari file wordlist.
                for kata_sandi in wordlist:
                        kata_sandi = kata_sandi.strip()
                        try:
                                # Membuka file zip dengan pyzipper dan mencoba kata sandi.
                                with pyzipper.AESZipFile(file_zip) as fz:
                                        list_file = fz.namelist()
                                        fz.pwd = kata_sandi.encode('latin-1')
                                        fz.extractall(path = folder)
                                        with open(file_log, 'a') as log:
                                                log.write(f"{kata_sandi}:{file_zip}:{kata_sandi}\n")
                                        print(f"{h}[+] {p}File zip berhasil diekstrak dengan kata sandi: '{h}{kata_sandi}{p}'{r}")
                                        print(f"{h}[+] {p}Isi file zip yang berhasil diekstrak:{r}")
                                        for file in list_file:
                                                print(f"    {h}[+] {p}{file}{r}")
                                        print(f"{h}[+] {p}Isi file zip yang berhasil diekstrak disimpan di folder '{h}Hasil Ekstraksi'{p}.{r}")
                                        print(f"{h}[+] {p}Kata sandi yang berhasil ditemukan disimpan di file Log: '{h}ZipForce.log{p}'.{r}")
                                        break
                        except Exception as e:
                                print(f"{m}[-] {p}File zip gagal diekstrak dengan kata sandi: '{m}{kata_sandi}{p}'{r}")

if __name__ == "__main__":       

        # File untuk menyimpan Log ZipForce.
        file_log = "ZipForce.log"

        # Membuat file 'ZipForce.log' jika belum ada.
        if not os.path.exists(file_log):
                with open(file_log, 'w') as f:
                        f.write("[ZipForcre Log]\n")                       

        # Folder untuk menyimpan hasil ekstraksi file zip.
        folder = "Hasil Ekstraksi"

        # Membuat folder 'Hasil Ekstraksi' jika belum ada.
        if not os.path.exists(folder):
                os.makedirs(folder)
 
        banner()
        
        # Memasukkan nama file zip.
        while True:
                file_zip = input(f"{c}[»] {p} Masukkan jalur file zip : ")
                if os.path.exists(file_zip):
                        if file_zip.endswith('.zip'):
                                print(f"{h}[+] {p}File zip {file_zip} ditemukan.{r}")
                                break
                        else:
                                print(f"{m}[-] {p}File {file_zip} bukan file zip.{r}")
                else:
                        print(f"{m}[-] {p}File {file_zip} tidak ditemukan.{r}")

        # Memasukkan nama file wordlist.
        while True:
                file_wordlist = input(f"{c}[»] {p}Masukkan jalur file wordlist: ")
                if os.path.exists(file_wordlist):
                        print(f"{h}[+] {p}File wordlist {file_wordlist} ditemukan.{r}")
                        break
                else:
                        print(f"{m}[-] {p}File {file_wordlist} tidak ditemukan.{r}")

        
        # Menjalankan fungsi ekstrak_file_zip dengan parameter 'file_zip, folder, file_wordlist'.
        ekstrak_file_zip(file_zip, file_log, folder, file_wordlist)
