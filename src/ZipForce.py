#!/usr/bin/env python3
# Nama Program............: ZipForce
# Deskripsi Program.......: Ekstraksi pada file zip yang terlindungi oleh kata sandi dengan menggunakan wordlist.
# Pembuat Program.........: Rofi
# Github..................: https://github.com/rofidoang03/ZipForce
#
# MIT License
#
# Copyright (c) 2024 rofidoang03 
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
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

while True:
        file_zip = input(f"{k}[?] {p}Nama file zip: ")
        if os.path.exists(file_zip):
                if file_zip.endswith('.zip'):
                        print(f"{h}[+] {p}File zip {file_zip} ditemukan.{r}")
                        break
                else:
                        print(f"{m}[-] {p}File {file_zip} bukan file zip.{r}")
        else:
                print(f"{m}[-] {p}File {file_zip} tidak ditemukan.{r}")

while True:
        file_wordlist = input(f"{k}[?] {p}Nama file wordlist: ")
        if os.path.exists(file_wordlist):
                print(f"{h}[+] {p}File wordlist {file_wordlist} ditemukan.{r}")
                break
        else:
                print(f"{m}[-] {p}File {file_wordlist} tidak ditemukan.{r}")

folder_keluaran = os.path.expanduser("~/ZipForce/Hasil Ekstraksi")

if not os.path.exists(folder_keluaran):
        os.makedirs(folder_keluaran)

nama_file_dasar = os.path.splitext(file_zip)[0]

folder_keluaran = os.path.join(folder_keluaran, nama_file_dasar)

if not os.path.exists(folder_keluaran):
        os.makedirs(folder_keluaran)

with open(file_wordlist, 'r', encoding="latin-1", errors="ignore") as wordlist:
        print(f"\n{b}[*] {p}Mulai ekstraksi. Saat dimulai tekan [CTRL+C] untuk berhenti.{r}\n")
        time.sleep(3)
        for kata_sandi in wordlist:
                kata_sandi = kata_sandi.strip()
                try:
                        with pyzipper.AESZipFile(file_zip) as fz:
                                fz.pwd = kata_sandi.encode('latin-1')
                                fz.extractall(path=nama_folder_yang_diekstrak)
                                print(f"{h}[+] {p}File zip berhasil diekstrak dengan kata sandi: {h}{kata_sandi}{r}")
                                break
                except Exception as e:
                        print(f"{m}[-] {p}File zip gagal diekstrak dengan kata sandi: {m}{kata_sandi}{r}")
