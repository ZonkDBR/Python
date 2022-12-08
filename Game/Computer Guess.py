import random
def v1(x) :
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' :
        guess = random.randint(low, high)
        feedback = input(f"Apakah {guess} terlalu tinggi (h), terlalu rendah (l), atau Benar(c)? ")
        if feedback == 'h' :
            high = guess - 1
        if feedback == 'l' :
            low = guess + 1
    print(f"Yay, Komputer menebak angka mu {guess} dengan benar!")
def v2(x) :
    soal = int(input("Masukkan Nomor Anda!\n"))
    jawaban = random.randint(1, x)
    print(jawaban)
    while jawaban != soal :
        if jawaban < soal :
            jawaban = random.randint(jawaban, x)
            print(jawaban)
        if jawaban > soal :
            jawaban = random.randint(1, jawaban)
            print(jawaban)
    else:
        print(f"Komputer menebak {soal} dengan benar!")
def user(x) :
    soal = random.randint(1, x)
    jawaban = int(input("Masukkan tebakan anda!\n"))

    while jawaban != soal:
        if jawaban > soal:
            print("Angka Kebesaran")
        if jawaban < soal:
            print("Angka Kekecilan")
        jawaban = int(input("Masukkan tebakan anda!\n"))
    else:
        print("Kamu menebak dengan benar!")
a = int(input("Pilih yang mana?\n1. Computer Guess v1\n2. Computer Guess v2\n3. User Guess\n"))
if a == 1 :
    b = int(input("Masukkan batas angkanya!\n"))
    v1(b)
if a == 2 :
    b = int(input("Masukkan batas angkanya!\n"))
    v2(b)
if a == 3 :
    b = int(input("Masukkan batas angkanya!\n"))
    user(b)