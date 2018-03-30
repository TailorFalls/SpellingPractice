print ("Hello Drew")

# store the word
spelling_word = "sulk"
# store the definition
definition = "To be angry or upset about something and to refuse to discuss it with other people"

spelling_words = {}
spelling_words["character"] = "the mental and moral qualities distinctive to an individual"
spelling_words["dilemma"] = "a difficult situation or problem"
spelling_words["quiet"] = "making little or no noise"
spelling_words["busses"] = "a large motor vehicle that carries passengers by road"
spelling_words["social"] = "of or relating to people or society in general"
spelling_words["quotation"] = "something that a person says or writes that is used by someone else in another piece of writing or a speech"
spelling_words["enough"] = "equal to what is needed"

# def load_file(filename):
#   for thing in file:
#     word = {}
#     word[thing] = file(thing).getdefinition()

# words = {
# word["sulk"] = "to laze around and pout"
# }

prompt_1 = "Please guess the spelling: "

# check user guess
def get_user_guess(meaning, prompt):
    print (meaning)
    user_guess = input(prompt)
    return user_guess

# check if word is spelled right
def check(correct_spelling, attempt):
    if attempt == correct_spelling:
        print ("You are correct!")
        return True
    else:
        print ("You are incorrect.")
        correct_length = len(correct_spelling)
        clue = ""
        for x in range(0, correct_length):
            if correct_spelling[x] == attempt[x]:
                clue += correct_spelling[x]
            else:
                clue += correct_spelling[x]
                break
        print ("Here's a clue! Start with " + clue)
        return False

# guess = get_user_guess(word["definition"], prompt_1)
# check(word["spelling_word"], guess)

# guess = get_user_guess(word2["definition"], prompt_1)
# check(word2["spelling_word"], guess)

def try_word(spelling_word, definition, prompt):
  guess = get_user_guess(definition, prompt)
  correct = check(spelling_word, guess)
  if not correct:
    response = input("Press Y to try again: ")
    if response == "Y":
      try_word(spelling_word, definition, prompt)

for word in spelling_words.keys():
  # print("My key is: " + word)
  # print("My definition is: " + spelling_words[word])
  try_word(word, spelling_words[word], prompt_1)
  # try_word(word, prompt_1)

  
# try_word(word1, prompt_1)
# try_word(word2, prompt_1)
# try_word(word3, prompt_1)
# try_word(word4, prompt_1)
# try_word(word5, prompt_1)
# try_word(word6, prompt_1)
