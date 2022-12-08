from random_word import RandomWords
import string

def valid_word(RandomWords) :
    word = RandomWords()
    kalimat = word.get_random_word()
    return kalimat.upper()

def hangman() :
    word = valid_word(RandomWords)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()
    chance = 10
    while len(word_letters) > 0 and chance > 0 :
        print('You have', chance, 'chance left', 'and you alredy use this letter', ''.join(used_letter))
        word_list = [letter if letter in used_letter else '-' for letter in word]
        print("Current word : ", ''.join(word_list))
        user_letter = input("Guess the letter!\n").upper()
        if user_letter in alphabet - used_letter :
            used_letter.add(user_letter)
            if user_letter in word_letters :
                word_letters.remove(user_letter)
            else:
                chance = chance - 1
        elif user_letter in used_letter :
            print("You alredy use it!")
        else:
            print("Invalid Character!")
    if chance == 0 :
        print("You LOST!\n The word is : ", word)
    else:
        print("You Won", word)
hangman()