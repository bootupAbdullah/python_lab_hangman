import random

listOfWords = [{"Superman"}, {"Pegasus"}, {"Danger Zone"}, {"Highway"}, {"Exclamation"}]



# for words in listOfWords:
#     for word in words:
#         print(word)


# for word in listOfWords[0]:
#     print(word)



def word_choice():
      num = random.randint(0,4)
      for word in listOfWords[num]:
        return word

# print(word_choice())

def game():
    print('Welcome to hangman')
    while True:
        prompt = input("""
Press '1' to play. Press any other key to quit.\n
""")
        if prompt != "1":
            break

        if prompt == "1":
            first_word = word_choice()
            print(f"You have three turns to guess the word. Your word has {len(first_word)} letters.")
            guess_1 = input("")
            if guess_1 in first_word:
                print("You have guessed correctly. Please guess again.")
                print(f"Letter guessed correctly: {guess_1}")

        
game()