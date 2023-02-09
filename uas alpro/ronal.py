# Input
omset = int(input("Masukkan omset penjualan: "))
tpengeluaran = int(input("Masukkan total pengeluaran perusahaan: "))

# Proses
keuntungan = omset - tpengeluaran
uali = keuntungan * 20 / 100
ubudi = keuntungan * 30 / 100
ususi = keuntungan * 50 / 100

# Output
print("Keuntungan Ali:", uali)
print("Keuntungan Budi:", ubudi)
print("Keuntungan Susi:", ususi)