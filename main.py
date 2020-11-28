import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# code = data["code"].tolist()
# letter = data["letter"].tolist()
# nato_alpha = {letter[i]: code[i] for i in range(len(letter))}

# same thing as above but shorter
nato_alpha = {row.letter: row.code for (index, row) in data.iterrows()}

user_input = input("Enter a word:\n> ").upper()
code_list = [nato_alpha[letter] for letter in user_input]
print(code_list)




