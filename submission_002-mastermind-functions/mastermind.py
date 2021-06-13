import random
#this is a comment
#FUCK
correct_digits_and_position = 0
correct = False
turns = 0
# TODO: Decompose into functions
def generate_code():
    '''generate the random code'''
    code = [0,0,0,0]
    for i in range(4):
        value = random.randint(1,8) # 8 possible digits
        while value in code:
            value = random.randint(1,8)  # 8 possible digits
        code[i] = value
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')
    return code

def get_user_input():
    while True:
        user_input = input('Input 4 digit code: ')
        if len(user_input) == 4:
            return user_input
        else:
            print('Please enter exactly 4 digits.')
            continue


def check_input_wrong(code):
    '''checks user input and checks if it is incorrect'''
    global correct_digits_and_position
    global turns
    global correct
    while not correct and turns < 12 :
        correct_digits_and_position = 0
        correct_digits_only = 0
        answer = get_user_input()
        for i in range(len(code)):
            if str(code[i]) == answer[i]:
                correct_digits_and_position += 1
            elif int(answer[i]) in code:
                correct_digits_only += 1
        print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
        print('Number of correct digits not in correct place: '+str(correct_digits_only))
        turns += 1
        check_input_correct(code)
        if correct_digits_and_position == 4:
            break
        continue

def check_input_correct(code):
    '''checks user input and checks if it matches random code'''
    global correct_digits_and_position
    global turns
    if correct_digits_and_position == 4:
        correct = True
        print('Congratulations! You are a codebreaker!')
        print('The code was: '+str(code))
    else:
        print('Turns left: '+str(12 - turns))


def run_game():
    code = generate_code()
    check_input_wrong(code)


if __name__ == "__main__":

    run_game()
