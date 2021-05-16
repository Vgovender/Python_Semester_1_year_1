#TIP: use random.randint to get a random word from the list
import random


def read_file(file_name):
    file_n = open(file_name,"r")
    all_words = file_n.readlines()
    """
    TODO: Step 1 - open file and read lines as words
    """
    return all_words

def select_random_word(words):
    r_word = random.randint(0,len(words)-1)
    word = words[r_word]
    r_letter = random.randint(0,len(word)-2)
    word1 = word[:r_letter]+'_'+word[r_letter+1:]
    print("Guess the word:",word1)
    """
    TODO: Step 2 - select random word from list of file
    """
    return word

def get_user_input():
    usr = input("Guess the missing letter: ")
    """
    TODO: Step 3 - get user input for answer
    """
    return usr

def run_game(file_name):
    """
    This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print('The word was: '+word)

if __name__ == "__main__":
    run_game('short_words.txt')

