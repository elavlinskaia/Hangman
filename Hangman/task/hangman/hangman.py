import random


num_of_win = 0
num_of_lost = 0
is_game = True
print("H A N G M A N")

while is_game:
    game_mode = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    if game_mode == "play":
        num_of_attempts = 8
        print("")
        word_list = ["python", "java", "swift", "javascript"]
        word = random.choice(word_list)
        current_word = len(word) * "-"
        current_list = [n for n in current_word]
        entered_letters = []
        print(current_word)

        while num_of_attempts > 0:
            input_letter = input("Input a letter: ")
            if len(input_letter) != 1:
                print("Please, input a single letter.")
            elif not input_letter.islower() or not input_letter.isalpha():
                print("Please, enter a lowercase letter from the English alphabet.")
            elif input_letter in entered_letters:
                print("You've already guessed this letter.")
            elif input_letter in word:
                for ind in range(len(word)):
                    if word[ind] == input_letter:
                        current_list[ind] = input_letter
                current_word = "".join(current_list)
                entered_letters.append(input_letter)
            else:
                print("That letter doesn't appear in the word.")
                num_of_attempts -= 1
                entered_letters.append(input_letter)

            if num_of_attempts > 0:
                if current_word == word:
                    print()
                    print("You guessed the word " + word + "!")
                    print("You survived!")
                    num_of_win += 1
                    break
                else:
                    print()
                    print(current_word)
            else:
                print()
                print("You lost!")
                num_of_lost += 1

    elif game_mode == "results":
        print("You won: " + str(num_of_win) + " times")
        print("You lost: " + str(num_of_lost) + " times")

    elif game_mode == "exit":
        is_game = False
        exit()
