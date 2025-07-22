import json 

def muat_data(nama_file):
        """
    Fungsi untuk memuat data inventaris dari file JSON.
    Mengembalikan list kosong jika file tidak ada atau error.
    """
    try :
        with open(nama_file, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Peringatan: File data tidak valid. Membuat file baru.")
        return []
    
def simpan_data(nama_file, data):
    """
    Fungsi untuk menyimpan data inventaris ke file JSON.
    """
    with open(nama_file, 'w') as f:
        json.dump(data, f, indent=4)