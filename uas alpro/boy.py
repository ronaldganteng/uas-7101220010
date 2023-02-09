# Program untuk menghitung nilai akhir dan grade mata kuliah Algoritma dan Pemrograman

# Mendefinisikan variabel-variabel yang diperlukan
kehadiran = float(input("Masukkan nilai kehadiran (0-100): "))
tugas = float(input("Masukkan nilai tugas (0-100): "))
uts = float(input("Masukkan nilai UTS (0-100): "))
uas = float(input("Masukkan nilai UAS (0-100): "))

# Menghitung nilai akhir
na = (kehadiran * 0.1) + (tugas * 0.2) + (uts * 0.3) + (uas * 0.4)

# Menentukan grade
if na >= 85:
    grade = 'A'
elif na >= 70:
    grade = 'B'
elif na >= 55:
    grade = 'C'
elif na >= 40:
    grade = 'D'
else:
    grade = 'E'

# Menampilkan hasil
print("Nilai Akhir:", na)
print("Grade:", grade)
