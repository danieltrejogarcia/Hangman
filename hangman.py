import random
import os
file_path="C:/Users/Computer/Python/hangman/animals.txt"

def intro():
    print("""
 _   _    _    _   _  ____ __  __    _    _   _
| | | |  / \  | \ | |/ ___|  \/  |  / \  | \ | |
| |_| | / _ \ |  \| | |  _| |\/| | / _ \ |  \| |
|  _  |/ ___ \| |\  | |_| | |  | |/ ___ \| |\  |
|_| |_/_/   \_\_| \_|\____|_|  |_/_/   \_\_| \_|
""")
    print("welcome to hangman")

# this will display the hangman display. 
# The stage is calculated based on the difficulty chosen and number of incorrect guesses 
def show_guy(guesses_left, max_guesses):
    stages = [
        """
           _______
          |      |
          |
          |
          |
          |
        __|__
        """,
        """
           _______
          |      |
          |      O
          |
          |
          |
        __|__
        """,
        """
           _______
          |      |
          |      O
          |      |
          |
          |
        __|__
        """,
        """
           _______
          |      |
          |      O
          |     /|
          |
          |
        __|__
        """,
        """
           _______
          |      |
          |      O
          |     /|\\
          |
          |
        __|__
        """,
        """
           _______
          |      |
          |      O
          |     /|\\
          |     /
          |
        __|__
        """,
        """
           _______
          |      |
          |      O
          |     /|\\
          |     / \\
          |
        __|__
        """
    ]
    status= int((max_guesses - guesses_left) / max_guesses * (len(stages) - 1))
    return stages[status]

#processes player input makes sure input is single letter and formats it into uppercase for latter comparison
def player_guess(guess):
    while len(guess) != 1 or not guess.isalpha():
        print("please only enter one letter")
        guess = input()
    return guess.upper()
    
def update_progress(secret_word, guess, word):
    position = 0
    for letter in word:
        if guess == letter:
            secret_word[position] = letter
        position += 1
        
def set_difficulty(level):
   
    while level not in ("1","2","3"):
        level = input("please enter a number between 1 and 3\n")
    dif = int(level)   
    if dif == 1:
        return 9
    elif dif == 2:
        return 7
    elif dif == 3:
        return 5
    
# gets a random word from included animals.txt file. If file is not present defaults to 2 player mode
def get_word(file_path):
    try:
        with open(file_path, "r") as f:
            random_line = random.choice(f.readlines())
            return random_line.strip().upper()
    except FileNotFoundError:
        print("No word bank found defaulting to 2 player mode")
        print("please enter a secret word")
        return validate_word(input())

def replay(answer):
    while(answer.upper() not in ("Y", "N")):
        answer = input("please enter  Y to replay or N to quit\n")
    if answer.upper() == "Y":
        return True
    else:
        return False

def create_lists(word):
    word_list = []
    secret_word = []
    for letter in word:
        secret_word.append("_")
        word_list.append(letter)
    return word_list, secret_word

def validate_word(word):
    while(not word.isalpha()):
        print("please enter secret word using only letters")
        word = input()
    return word.upper()


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
#main game loop
def game():
    state = True
    while state:
        print("what level do you want to try? Easy(1) Normal(2) Hard(3)")
        max_guesses = set_difficulty(input())
        guesses = max_guesses
        print("How many players?")
        player_count = ""
        while player_count != "2" and player_count != "1":
            player_count = input("please enter 1 for single player and 2 for 2 player game\n")
        if player_count == "1":
            word = get_word(file_path)
        else:         
            print("enter your secret word")
            word= validate_word(input())


        word_list, secret_word = create_lists(word)

        all_guesses=""
        while guesses > 0:
            clear_screen()
            print(show_guy(guesses, max_guesses))            
            print(" ".join(secret_word))
            print(f"you have {guesses} guesses left")
            if all_guesses != "":
                print(f"you've already guessed the letters {all_guesses.upper()}")
            check = player_guess(input())
            
            if check in all_guesses:
                print("you've already guessed that")
                input()
                continue
            elif check in word:
                update_progress(secret_word, check, word_list)
                if check not in all_guesses:    
                    all_guesses += check
                if secret_word == word_list:
                    clear_screen()
                    print(show_guy(guesses, max_guesses))            
                    print("You Won!!!")
                    print("do you wish to replay?")
                    state = replay(input())  
                    break
                continue
            
            else:
                all_guesses += check
                guesses -= 1
        if guesses == 0:
            clear_screen()
            print(show_guy(guesses, max_guesses))            
            print("you lost!!!")
            print(word_list)
            print("Do you wish to replay?")
            state = replay(input())
            

def play():
    intro()
    game()    

play()


