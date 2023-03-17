import pandas

#Read file of codes and create a dictionary
df = pandas.read_csv("nato_phonetic_alphabet.csv")
dic = {row.letter: row.code for (index, row) in df.iterrows()}

#Convert user input to list and translate each letter into code
user_input = input("Enter any word: ").upper()
input_list = list(user_input)
list_of_words = [dic[letter] for letter in input_list]
print(list_of_words)
