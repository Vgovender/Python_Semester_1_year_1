import random


def read_file(file_name):
    file = open(file_name,'r')
    f = file.readlines()
    file.close()
    return f


def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = words[random_index]
    return word


def select_random_letter_from(word):
    random_index = random.randint(0, len(word) - 2)
    letter = word[random_index]
    print('Guess the word: ' + word[:random_index] + "_" + word[random_index+1:])
    return letter, random_index

def get_user_input():
    return input('Guess the missing letter: ')
    

def show_answer(answer, selected_word, missing_letter_index):
    if selected_word[missing_letter_index] == answer:
        print("The word was: " + selected_word)
        print("Well done! You are awesome!")
    else:
        print("The word was: " + selected_word)
        print("Wrong! Do better next time.")

    """
    TODO Step 1 - Show better results messages
    """
    pass


# TODO: Step 2
def ask_file_name():
    file_name = input("Words file? [leave empty to use short_words.txt] :")
    if file_name == "":
        file_name = "short_words.txt"
    while file_name == False:
        print("You entered an incorrect file name. Please try again")
        file_name = input("Words file? [leave empty to use short_words.txt] :")
    
    """
    TODO Step 2 - Update to prompt user for filename to use for words
    """
    return file_name


def run_game(file_name):
    """
    You can leave this code as is, and only implemented above where the code comments prompt you.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    missing_letter, letter_index = select_random_letter_from(word)
    answer = get_user_input()
    show_answer(answer, word, letter_index)

if __name__ == "__main__":
    words_file = ask_file_name()
    run_game(words_file)