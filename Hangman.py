import words

def play_again():
    while True:
        choice = input("\nPlay again? y/n: ")

        if choice == 'y' or choice == 'Y':
            play_hangman(words.get_word())
        elif choice == 'n' or choice == 'N':
            break
        elif choice != 'y' or choice != 'Y' or choice != 'n' or choice != 'N':
            continue
        # if user enters a wrong choice, then tries to enter either n or N,
        # the program will continue to ask if they want to play agian, even
        # though the user entered a valid choice...

def play_hangman(word):
    wrong = 0 # keeps track of incorrect letters p2 has guessed
    stages = ["",
              "__________          ",
              "|                   ",
              "|          |        ",
              "|          0        ",
              "|         /|\       ",
              "|         / \       ",
              "|                   "
              ]
    rletters = list(word) # keeps track of letters left to guess as a list of chars
    board = ["_"] * len(word) # creates dashes according to the length of a word
    win = False
    print("---WELCOME TO HANGMAN---")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        char = char.lower()

        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
            
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))

        if "_" not in board:
            print("You win! The word was: \"{}\"".format(word))
            win = True
            break
        
    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose! The word was: {}".format(word))

    play_again()

play_hangman(words.get_word())










