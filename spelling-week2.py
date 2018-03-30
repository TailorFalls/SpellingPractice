print ("Hello Drew")

# store the word
spelling_word = "sulk"
# store the definition
definition = "To be angry or upset about something and to refuse to discuss it with other people"

word1 = {}
word1["spelling_word"] = spelling_word
word1["definition"] = definition

word2 = {}
word2["spelling_word"] = "excitement"
word2["definition"] = "A feeling of eager enthusiasm and interest : the state of being excited"

word3 = {}
word3["spelling_word"] = "inscription"
word3["definition"] = "Words that are written on or cut into a surface." 

word4 = {}
word4["spelling_word"] = "occasion"
word4["definition"] = "A special event or time."

word5 = {}
word5["spelling_word"] = "familiar"
word5["definition"] = "Frequently seen, heard, or experienced"

word6 = {}
word6["spelling_word"] = "criticize"
word6["definition"] = "To express disapproval of (someone or something) : to talk about the problems or faults of (someone or something)"

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

def try_word(spelling_word, prompt):
  guess = get_user_guess(spelling_word["definition"], prompt)
  correct = check(spelling_word["spelling_word"], guess)
  if not correct:
    response = input("Press Y to try again: ")
    if response == "Y":
      try_word(spelling_word, prompt)

try_word(word1, prompt_1)
try_word(word2, prompt_1)
try_word(word3, prompt_1)
try_word(word4, prompt_1)
try_word(word5, prompt_1)
try_word(word6, prompt_1)
