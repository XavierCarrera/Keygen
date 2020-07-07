import random


def keygen():
    mayus = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    minus = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    symb = ["!", "#", "$", "%", "&", "/"]
    num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    character = mayus + minus + symb + num

    keyword = []

    for i in range(15):
        character_random = random.choice(character)
        keyword.append(character_random)

    keyword = "".join(keyword)
    return keyword

def run(): 
    keyword = keygen()
    print("Your new password is: " + keyword)

if __name__ == '__main__':
    run()