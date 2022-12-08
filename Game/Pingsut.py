from random import choice
def play() :
    pilihan = int(input("Pilih apa?\n1. Pingsut Jepang\n2. Pingsut Jawa\n"))
    if pilihan == 1 :
        user = input("'B' untuk Batu\n'G' untuk Gunting\n'K' untuk Kertas\n").upper()
        computer = choice(["B", "G", "K"])
        print(computer)
        if user == computer :
            return "Tied!"
        if is_win(user, computer) :
            return "You Won!"
        return "You Lose!"
    if pilihan == 2 :
        user = input("'S' untuk Semut\n'M' untuk Manusia\n'G' untuk Gajah\n").upper()
        computer = choice(["S", "M", "G"])
        print(computer)
        if user == computer :
            return "Tied!"
        if is_win(user, computer) :
            return "You Won!"
        return "You Lose!"
def is_win(player, opponent) :
    if (player == "G" and opponent == "K") or (player == "K" and opponent == "B") or (player == "B" and opponent == "G") or (player == "S" and opponent == "G") or (player == "M" and opponent == "S") or (player == "G" and opponent == "M") :
        return True
print(play())