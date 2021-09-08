# Write your code here
import random

# print("""H A N G M A N
# The game will be available soon.""")

# answer = random.choice(['python', 'java', 'kotlin', 'javascript'])
# # letters = answer[0:3]
# # hidden_letters = ("-" * (len(answer) - 3))
# # hidden_word = letters + hidden_letters
# #
# # first_word = input(f'Guess the word {hidden_word}: ')
# #
# # if first_word == answer:
# #     print('You survived!')
# # else:
# #     print('You lost!')
import sys

list_of_words = ['python', 'java', 'kotlin', 'javascript']
chosen_word = random.choice(list_of_words)
hidden_word = list(len(chosen_word) * '-')
lives = 8
letters_used = []
counter = 0

print("""H A N G M A N""")


while counter < 1:
    menu = input('Type "play" to play the game, "exit" to quit: ')
    if menu == 'quit':
        quit()
    elif menu == 'play':
        counter += 1

while lives > 0:
    print()
    answer = ''.join(hidden_word)
    print(answer)
    if answer == chosen_word:
        print('You guessed the word!')
        print('You survived!')
        break
    i = input('Input a letter: ')

    if len(i) >= 2:
        print("You should input a single letter")
    elif i.islower() is not True:
        print("Please enter a lowercase English letter")
    elif i.isalpha() is not True:
        print("Please enter a lowercase English letter")
    elif i in letters_used:
        print("You've already guessed this letter")
    elif i not in chosen_word:
        lives -= 1
        print('That letter doesn\'t appear in the word')


    if lives == 0:
        print('You lost!')
    letters_used.append(i)

    for num in range(0, len(chosen_word)):
        if i in chosen_word[num]:
            hidden_word[num] = i




# print("""Thanks for playing!
# We'll see how well you did in the next stage""")
