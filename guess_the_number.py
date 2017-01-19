import random

correct = 'you guessed correctly!'
too_low = 'Too Low!!!'
too_high = 'too high'


def configure_range():
    '''Set the high and low values for the random number'''
    minimum = int(input('Enter the minimum value: '))
    maximum = int(input('Enter the maximum value: '))
    return minimum, maximum


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess(low, high):
    '''get user's guess'''
    x = 0
    valid = False
    while not valid:
        try:
            x = int(input('Guess the secret number?'))
        except ValueError:
            print('Invalid!')
            continue
        if low <= x <= high:
            valid = True
        else:
            print('Value out of range!')
    return x


def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high

def input_valid(x):
    try:
        if type(x) == int:
            return True
    except:
        return False

def main():

    game_running = True
    while game_running:  # main game loop

        guess_counter = 0

<<<<<<< HEAD
        (low, high) = configure_range()
        secret = generate_secret(low, high)

        guessing = True
        while guessing:
            guess = get_guess()
            result = check_guess(guess, secret)
            guess_counter += 1
            print(result)

            if result == correct:
                print("You got in in " + str(guess_counter))
                guessing = False

        print("DEBUG: end of game")

        replay_input_invalid = True
        while replay_input_invalid:  # input validation loop
        # TODO separate into validation function
            replay = input("Play again? [Y/N] ")
            if replay.upper() == 'Y':
                replay_input_invalid = False
                game_running = True
            elif replay.upper() == 'N':
                replay_input_invalid = False
                game_running = False
            else:
                print("Please enter Y or N.")
                replay_input_invalid = True
=======
    while True:
        guess = get_guess(low, high)
        result = check_guess(guess, secret)
        guess_counter += 1
        print(result)
>>>>>>> bc77cfa97515fdbe17079e8da18add58a25d3e28



if __name__ == '__main__':
        main()
