import random


def run_game():
    digit_code = [random.randint(1,8),random.randint(1,8),random.randint(1,8),random.randint(1,8)]
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')
    count = 12   
    while True:    
        if count!= 0:
            check_correct_place = 0
            check_correct_digit = 0
            guess = input('Input 4 digit code: ')
            same = False
            if ((len(guess) != 4) or ('9' in guess) or (str(guess.isalpha) in guess)):    
                if count == 0:
                    break
                else:
                    while ((len(guess) != 4) or ('9' in guess)):
                        count -= 1
                        print('Please enter exactly 4 digits.')
                        guess = input('Input 4 digit code: ')
            for x in range(0,4):
                if int(guess[x]) == digit_code[x]:            
                    check_correct_place += 1
                elif guess[x] in str(digit_code) and int(guess[x]) != digit_code[x]:
                    check_correct_digit += 1
            if (int(guess[0]) == digit_code[0]) and (int(guess[1]) == digit_code[1]) and (int(guess[2]) == digit_code[2])and(int(guess[3]) == digit_code[3]):
                    same = True
                    print('Number of correct digits in correct place:    ',check_correct_place)
                    print('Number of correct digits not in correct place:',check_correct_digit)
                    print('Congratulations! You are a codebreaker!')
                    print('The code was:',guess)
                    break
            else:
                    same = False
            print('Number of correct digits in correct place:    ',check_correct_place)
            print('Number of correct digits not in correct place:',check_correct_digit)
            count -= 1
        else :
            break
        print('Turns left:',count)

    """
    TODO: implement Mastermind code here
    """
    pass


if __name__ == "__main__":
    run_game()
