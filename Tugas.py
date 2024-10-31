
# (222443015) M Dandi Al Idrus 2AEC

import random

print("**********Chatbot Customer Services BAAK Polman Bandung**********")
print("\n\nAda yang bisa dibantu?")
nama = input("Silahkan masukkan nama anda: ")
print("\nHallo", nama, "Ketik apa yang ingin anda tanya")

pertanyaan = ["jadwal", "nilai", "kehadiran", "dosen", "nim"]
jawaban = [
    "Jadwal kuliah dapat dilihat di aplikasi sistem akademik di menu jadwal",
    "Nilai kuliah dapat dilihat di aplikasi sistem akademik di menu nilai",
    "Kehadiran dapat dilihat di aplikasi sistem akademik di menu kehadiran",
    "Daftar dosen dapat dilihat di aplikasi sistem akademik di menu dosen",
    "NIM dapat dilihat di menu profil dalam aplikasi sistem akademik",
]

while True:
    pertanyaan_user = input("Pertanyaan Anda: ")

    if any(keyword in pertanyaan_user.lower() for keyword in pertanyaan):
        index = next((i for i, keyword in enumerate(pertanyaan) if keyword in pertanyaan_user.lower()), None)
        print("\nBot BAAK:", jawaban[index])
    elif pertanyaan_user.lower() == 'selesai':
        print("\nTerima kasih telah menggunakan CS BAAK")
        break
    else:
        random_index = random.randint(0, len(jawaban) - 1)
        print("\nBot BAAK: Maaf, pertanyaan Anda tidak dimengerti. Coba tanyakan yang lain.")

    lanjut = input("\nApakah ingin melanjutkan? (ya/tidak) ")
    if lanjut.lower() != "ya":
        print("\nTerima kasih telah menggunakan CS BAAK")
        break
