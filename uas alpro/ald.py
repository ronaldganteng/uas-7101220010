# Input
kehadiran = float(input("Masukkan nilai kehadiran (0-100): "))
tugas = float(input("Masukkan nilai tugas (0-100): "))
uts = float(input("Masukkan nilai UTS (0-100): "))
uas = float(input("Masukkan nilai UAS (0-100): "))

# Proses
na = 0.1 * kehadiran + 0.2 * tugas + 0.3 * uts + 0.4 * uas
if na >= 85:
    grade = "A"
elif na >= 70:
    grade = "B"
elif na >= 55:
    grade = "C"
elif na >= 40:
    grade = "D"
else:
    grade = "E"

# Output
print("Nilai akhir:", na)
print("Grade:", grade)
80