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

    guess_counter = 0

    (low, high) = configure_range()
    secret = generate_secret(low, high)

    while True:
        guess = get_guess(low, high)
        result = check_guess(guess, secret)
        guess_counter += 1
        print(result)

        if result == correct:
            print("You got in in " + str(guess_counter))
            break


if __name__ == '__main__':
    main()
