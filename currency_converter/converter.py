import requests

API_KEY = '3ba1e1f1eb9146b04178255f'
BASE_URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD'

try:
    response = requests.get(BASE_URL)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error Koneksi: {e}")
    exit()

print("Berhasil terhubung ke API!")

data = response.json()

print("Berikut adalah data yang diterima dari API:")
print(data)

rates = data.get('conversion_rates')

if not rates:
    print("Tidak ada data konversi yang ditemukan")
    exit()

# Tampilkan beberapa contoh kurs
print("\n--- Contoh Kurs terhadap USD ---")
print(f"1 USD = {rates.get('IDR')} IDR")
print(f"1 USD = {rates.get('JPY')} JPY")
print(f"1 USD = {rates.get('EUR')} EUR")


def konversi_mata_uang(jumlah, dari, ke, rates_data):
    """Fungsi untuk mengonversi mata uang dengan data kurs yang ada."""
    

    if dari not in rates_data or ke not in rates_data:
        return None, "Kode mata uang tidak valid."
        
    try:
        jumlah_dalam_usd = jumlah / rates_data[dari]
        
        hasil_akhir = jumlah_dalam_usd * rates_data[ke]
        
        return hasil_akhir, None 
    except ZeroDivisionError:
        return None, "Kurs mata uang tidak boleh nol."

# Kita coba fungsi kita
jumlah_untuk_dikonversi = 150000 # Contoh: Rp 150.000
hasil, error = konversi_mata_uang(jumlah_untuk_dikonversi, 'IDR', 'JPY', rates)

if error:
    print(f"Terjadi Error: {error}")
else:
    # ':.2f' adalah format untuk menampilkan 2 angka di belakang koma
    print(f"\n{jumlah_untuk_dikonversi} IDR adalah {hasil:.2f} JPY")