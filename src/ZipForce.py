#!/usr/bin/env python3
# Nama Program............: ZipForce
# Deskripsi Program.......: Ekstraksi pada file zip yang terlindungi oleh kata sandi dengan menggunakan wordlist.
# Pembuat Program.........: Rofi
# Github..................: https://github.com/rofidoang03/ZipForce

import os
import sys
import time
import colorama
import pyzipper

h = colorama.Fore.LIGHTGREEN_EX
b = colorama.Fore.LIGHTBLUE_EX
m = colorama.Fore.LIGHTRED_EX
c = colorama.Fore.LIGHTCYAN_EX
p = colorama.Fore.LIGHTWHITE_EX
k = colorama.Fore.LIGHTYELLOW_EX
r = colorama.Style.RESET_ALL

def ekstrak_file_zip(file_zip, folder, file_wordlist):
        with open(file_wordlist, 'r', encoding="latin-1", errors="ignore") as wordlist:
                print(f"\n{b}[*] {p}Mulai ekstraksi. Saat dimulai tekan [CTRL+C] untuk berhenti.{r}\n")
                time.sleep(3)
                for kata_sandi in wordlist:
                        kata_sandi = kata_sandi.strip()
                        try:
                                with pyzipper.AESZipFile(file_zip) as fz:
                                        fz.pwd = kata_sandi.encode('latin-1')
                                        fz.extractall(path=folder)
                                        print(f"{h}[+] {p}File zip berhasil diekstrak dengan kata sandi: {h}{kata_sandi}{r}")
                                        break
                        except Exception as e:
                                print(f"{m}[-] {p}File zip gagal diekstrak dengan kata sandi: {m}{kata_sandi}{r}")
                else:
                        print(f"{k}[!] {p}Tidak ada kata sandi yang cocok dalam file wordlist '{file_wordlist}'.{r}")
                        sys.exit(0)
                

if __name__ == "__main__":       

        # folder untuk menyimpan file hasil ekstraksi
        folder = "~/ZipForce/Hasil Ekstraksi"

        if not os.path.exists:
                os.makedirs(folder)

        while True:
                file_zip = input(f"{k}[?] {p}Nama file zip: ")
                if os.path.exists(file_zip):
                        if file_zip.endswith('.zip'):
                                print(f"{h}[+] {p}File zip {file_zip} ditemukan.{r}")
                        else:
                                print(f"{m}[-] {p}File {file_zip} bukan file zip.{r}")
                                sys.exit(1)
                else:
                        print(f"{m}[-] {p}File {file_zip} tidak ditemukan.{r}")
                        sys.exit(1)
                        
        while True:
                file_wordlist = input(f"{k}[?] {p}Nama file wordlist: ")
                if os.path.exists(file_wordlist):
                        print(f"{h}[+] {p}File wordlist {file_wordlist} ditemukan.{r}")
                else:
                        print(f"{m}[-] {p}File {file_wordlist} tidak ditemukan.{r}")
                        sys.exit(1)

        ekstrak_file_zip(file_zip, folder, file_wordlist)
