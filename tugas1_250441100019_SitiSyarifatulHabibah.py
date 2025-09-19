#Tugas Pelcod Kelas B 

nilai_tugas= 85
nilai_UTS= 75
nilai_UAS= 90

bobot_tugas = 0.30
bobot_UTS= 0.30
bobot_UAS= 0.40

nilai_akhir_tugas = nilai_tugas * bobot_tugas
nilai_akhir_UTS = nilai_UTS * bobot_UTS
nilai_akhir_UAS = nilai_UAS * bobot_UAS

total_nilai_akhir = nilai_akhir_tugas + nilai_akhir_UTS + nilai_akhir_UAS

print("--- Nilai yang diperoleh ---")
print("Nilai Tugas :", nilai_tugas)
print("Nilai UTS   :", nilai_UTS)
print("Nilai UAS   :", nilai_UAS)
print("-"*40)
print("Nilai akhir dari Tugas (30%) :", nilai_akhir_tugas)
print("Nilai akhir dari UTS (30%)   :", nilai_akhir_UTS)
print("Nilai akhir dari UAS (40%)   :", nilai_akhir_UAS)
print("="*12, "hasil akhir", "="*12)
print("Total Nilai Akhir Kamu :", total_nilai_akhir)

