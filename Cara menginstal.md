## Cara menginstal ZipForce

Untuk menginstal ZipForce sangatlah mudah Anda tinggal Copy Paste perintah yang ada dibawah ini:

> Pastikan Anda sudah dalam mode super user (root).

## Perintah 

1. Memperbarui daftar paket yang tersedia dari repositori paket pada sistem Linux Anda. 

```
apt-get update -y
```

2. Menginstal dependensi yang diperlukan ZipForce.

```
apt-get install python3 -y ; apt-get install python3-pip -y ; apt-get install python3.11-venv -y ; pip3 install --upgrade pip ; apt-get install git -y
```

3. Pindah ke direktori rumah pengguna.

```
cd ~
```

4. Meng-kloning repositori ZipForce dari Github. 

```
git clone https://github.com/rofidoang03/ZipForce
```

5. Pindah ke direktori ZipForce

```
cd ZipForce
```

6. Membuat lingkungan virtual Python.

```
python3 -m venv modules
```

7. Mengaktifkan lingkungan virtual Python.

```
source modules/bin/activate
```

8. Menginstal semua paket Python yang diperlukan.

```
pip3 install -r requirements.txt
```

<p align="right"><a href="https://github.com/rofidoang03/ZipForce/blob/main/README.md">Kembali ke Halaman utama</a></p>
