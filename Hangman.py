# Designed by Ferdinand
# Created on the 1st of October 2021 and finished on the 1st of November 2021

import time
import random 
from random import randint
from time import sleep

def random_word_generator():
    with open('sowpods.txt', 'r') as word_bank:
        word = word_bank.read().splitlines()  # this will read every line of the file and seperate each word into its own list element. without it 'word' would just be a big string
        word_selector = randint(1, len(word))   
        random_word = word[word_selector] 
    return random_word

def word_index(arr, x):
    for i in range(len(arr)):
        if arr[i] == x and i not in index_list:
            return i
    return -492006  

time.sleep(2)
print("")
print("Welcome to Hangman")
print("")
time.sleep(3)
print("You will get 6 lives") 
time.sleep(2)

print("")
print("                 +---+")
print("                 |   |")
print("                     |")
print("                     |")
print("                     |")
print("                     |")
print("              =========")
print("")

time.sleep(1)
print("however you will need to enter the correct letter multiple times to meet all the occurences")
print("")
print("")
time.sleep(4)

while True: 
    try:
        random_word_confirmed = random_word_generator() 
        guessing_answer = "_" * len(random_word_confirmed)  # will output a string with the number of underscores as letters in the word

        random_word_confirmed = list(random_word_confirmed)
        already_guessed = []

        print("The word has been chosen...")
        time.sleep(1)
        print(guessing_answer + "   this is a " + str(len(random_word_confirmed)) + " letter word")

        guessing_answer = list(guessing_answer)

        print("")

        time.sleep(1)
        user_guess = str(input("guess a letter: "))
        user_guess = user_guess.upper()

        t1 = time.time()

        index_list = []   # this list will make the program check more than one index by filtering the ones stored here which will have already been used

        current_lives = 6

        while True:  

            if user_guess in already_guessed:
                user_guess = ''  # so that on the next loop it will go to the else statement
                print("you've already guessed that letter ")  
                current_lives = current_lives - 1 
                if current_lives == 5:
                    print("")
                    print("                 +---+")
                    print("                 |   |")
                    print("                 O   |")
                    print("lives = "+ str(current_lives) +"            |")
                    print("                     |")
                    print("                     |")
                    print("              =========")
                    print("")
                elif current_lives == 4:
                    print("")
                    print("                 +---+")
                    print("                 |   |")
                    print("                 O   |")
                    print("lives = "+ str(current_lives) +"        |   |")
                    print("                     |")
                    print("                     |")
                    print("              =========") 
                    print("")
                elif current_lives == 3:
                    print("")
                    print("                 +---+")
                    print("                 |   |")
                    print("                 O   |")
                    print("lives = "+ str(current_lives) +"       /|   |")
                    print("                     |")
                    print("                     |")
                    print("              =========") 
                    print("")
                elif current_lives == 2:
                    print("")
                    print("                 +---+")
                    print("                 |   |")
                    print("                 O   |")
                    print("lives = "+ str(current_lives) +"       /|\  |")
                    print("                     |")
                    print("                     |")
                    print("              =========") 
                    print("")
                elif current_lives == 1:
                    print("")
                    print("                 +---+")
                    print("                 |   |")
                    print("                 O   |")
                    print("lives = "+ str(current_lives) +"       /|\  |")
                    print("                /    |")
                    print("                     |")
                    print("              =========") 
                    print("")
                elif current_lives == 0:
                    print("")
                    print("                 +---+")
                    print("                 |   |")
                    print("                 O   |")
                    print("lives = "+ str(current_lives) +"       /|\  |")
                    print("                / \  |")
                    print("                     |")
                    print("              =========")
                    print("")
                    time.sleep(2)
                    print("")
                    print("Game Over! ")
                    time.sleep(1) 
                    print("the word was: " + ''.join(random_word_confirmed)) 
                    print("")
                    print("")
                    time.sleep(3)
                    print("launching next game...")
                    time.sleep(1)
                    print("")
                    print("")
                    break              

            elif user_guess in random_word_confirmed and user_guess not in already_guessed:
                checking_index = word_index(random_word_confirmed,user_guess) 
                if checking_index == -492006:
                    print("there is no more of that letter left in the word")
                    user_guess = ''   # so that on the next loop it will go to the else statement 
                if checking_index != -492006:  # i need this here because if not then the if statement above will not have any significance as the program would still try and assign that negative number to an index when it is not an index
                    guessing_answer[checking_index] = user_guess
                    index_list.append(checking_index)
                    user_guess = ''   # so that on the next loop it will go to the else statement

            else:
                print(''.join(guessing_answer))
                if user_guess is not '' and user_guess not in random_word_confirmed: 
                    already_guessed.append(user_guess)
                    print("thats incorrect..")
                    current_lives = current_lives - 1 
                    if current_lives == 5:
                        print("")
                        print("                 +---+")
                        print("                 |   |")
                        print("                 O   |")
                        print("lives = "+ str(current_lives) +"            |")
                        print("                     |")
                        print("                     |")
                        print("              =========")
                        print("")
                    elif current_lives == 4:
                        print("")
                        print("                 +---+")
                        print("                 |   |")
                        print("                 O   |")
                        print("lives = "+ str(current_lives) +"        |   |")
                        print("                     |")
                        print("                     |")
                        print("              =========") 
                        print("")
                    elif current_lives == 3:
                        print("")
                        print("                 +---+")
                        print("                 |   |")
                        print("                 O   |")
                        print("lives = "+ str(current_lives) +"       /|   |")
                        print("                     |")
                        print("                     |")
                        print("              =========") 
                        print("")
                    elif current_lives == 2:
                        print("")
                        print("                 +---+")
                        print("                 |   |")
                        print("                 O   |")
                        print("lives = "+ str(current_lives) +"       /|\  |")
                        print("                     |")
                        print("                     |")
                        print("              =========") 
                        print("")
                    elif current_lives == 1:
                        print("")
                        print("                 +---+")
                        print("                 |   |")
                        print("                 O   |")
                        print("lives = "+ str(current_lives) +"       /|\  |")
                        print("                /    |")
                        print("                     |")
                        print("              =========") 
                        print("")
                    elif current_lives == 0:
                        print("")
                        print("                 +---+")
                        print("                 |   |")
                        print("                 O   |")
                        print("lives = "+ str(current_lives) +"       /|\  |")
                        print("                / \  |")
                        print("                     |")
                        print("              =========")
                        print("")
                        time.sleep(2)
                        print("")
                        print("Game Over! ")
                        time.sleep(1) 
                        print("the word was: " + ''.join(random_word_confirmed)) 
                        print("")
                        print("")
                        time.sleep(3)
                        print("launching next game...")
                        time.sleep(1)
                        print("")
                        print("")
                        break              


                time.sleep(1)
                user_guess = str(input("guess a letter: "))
                user_guess = user_guess.upper()

            if '_' not in guessing_answer:
                t2 = time.time() 
                print("")
                time.sleep(1)
                print("Congrats you've won!")
                print("the word was: " + ''.join(random_word_confirmed)) 
                time.sleep(1)
                t3 = t2 - t1 
                print("time taken = " + str(t3) + " in seconds")
                print("")
                print("")
                time.sleep(3)
                print("launching next game...")
                print("")
                print("")
                break

    except:
        print("")
        print("an error has occured")
        print("")


# Designed by Ferdinand
