import json

print ("Hello Drew")

filename = "week8.json"

with open(filename) as infile:
	spelling_words = json.load(infile)

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
    if response.upper() == "Y":
      try_word(spelling_word, definition, prompt)

for word in spelling_words.keys():
  # print("My key is: " + word)
  # print("My definition is: " + spelling_words[word])
  try_word(word, spelling_words[word], prompt_1)
  # try_word(word, prompt_1)
