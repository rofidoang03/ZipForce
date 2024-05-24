#!/bin/bash

function cek_root(){
        if [[ "$EUID" -ne 0 ]]; then
                echo "[x] Script ini harus dijalankan sebagai root."
                exit 1
        fi
}

function install_dependency(){
        dependency_list=(
        "python3"
        "python3-pip"
        "python3.11-venv"
        )

        for dependency in "${dependency_list[@]}"; do
                apt-get install "${dependency}"
        done
}

function install_requirements_python3(){
        python3 -m venv ~/ZipForce/modules
        source ~/ZipForce/modules/bin/activate
        pip3 install -r ~/ZipForce/requirements.txt
}

function install_Zip_Force(){
        while true; do
                read -p "Apakah Anda ingin menginstal ZipForce [Y/n] " nanya
                if [[ "${nanya}" == "y" ]] || [[ "${nanya}" == "Y" ]]; then
                        cek_root
                        # cek_koneksi_internet
                        install_dependency
                        install_requirements_python3
                        break
                else
                        echo "[x] Proses instalasi dibatalkan."
                        exit 1
                fi
        done
}

install_ZipForce
