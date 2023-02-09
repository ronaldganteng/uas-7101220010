# Input
gaji = int(input("Masukkan gaji: "))
hutang = int(input("Masukkan hutang: "))

# Proses
keuangan = gaji - hutang
biaya_sehari_hari = keuangan * 70 / 100
tabungan = keuangan * 20 / 100
infak = keuangan - biaya_sehari_hari - tabungan

# Output
print("Biaya sehari-hari:", biaya_sehari_hari)
print("Tabungan:", tabungan)
print("Infak:", infak)