## Cara menginstal ZipForce

Untuk menginstal ZipForce sangatlah mudah Anda tinggal Copy Paste perintah yang ada dibawah ini:

> Pastikan Anda sudah dalam mode super user (root).

## Perintah 

1. Memperbarui daftar paket yang tersedia dari repositori paket pada sistem Linux Anda. 

```
apt-get update -y
```

2. Menginstal dependensi yang diperlukan ZipForce 

```
apt-get install python3 -y ; apt-get install python3-pip -y ; apt-get install python3.11-venv -y
```

3. Membuat lingkungan virtual Python.

```
python3 -m venv /root/ZipForce/modules
```

4. Mengaktifkan lingkungan virtual Python.

```
source /root/ZipForce/modules/bin/activate
```

5. Menginstal semua paket Python yang diperlukan.

```
pip3 install -r /root/ZipForce/requirements.txt
```
