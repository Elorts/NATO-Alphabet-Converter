import pandas

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

#easy methood
#data_frame = pandas.read_csv("nato_phonetic_alphabet.csv", header=None, index_col=0, squeeze=True)

df = pandas.read_csv("nato_phonetic_alphabet.csv")
dic = df.to_dict()
print(dic)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# user_input = input("Enter any word: ").upper()
# input_list = list(user_input)
# list_of_words = [dic[letter] for letter in input_list]
# print(list_of_words)

