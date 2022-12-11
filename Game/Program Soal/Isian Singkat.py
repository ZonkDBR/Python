from Class import Pertanyaan
Soal = [
    "Warna apel adalah...\n",
    "Warna pisang adalah...\n",
    "Warna anggur adalah...\n",
    "Warna semangka adalah...\n",
    "Warna jeruk adalah...\n"
]
Pertanyaannya = [
    Pertanyaan(Soal[0], "merah"),
    Pertanyaan(Soal[1], "kuning"),
    Pertanyaan(Soal[2], "ungu"),
    Pertanyaan(Soal[3], "hijau"),
    Pertanyaan(Soal[4], "orange")
]
def Tes(Pertanyaanya):
    score = 0
    for Pertanyaan in Pertanyaanya:
        jawabannya = input(Pertanyaan.teks)
        if jawabannya.lower() == Pertanyaan.jawaban :
            score += 1
    else:
        print("Kamu benar " + str(score) + "/" + str(len(Pertanyaanya)))
