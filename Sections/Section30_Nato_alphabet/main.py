import os
import sys
import pandas as pd

DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append('\\'.join(DIR.split('\\')[:-2]))
import pyask


# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

alpha_file = os.path.join(DIR,'nato_phonetic_alphabet.csv')
alphabet = pd.read_csv(alpha_file)
# alphabet = alphabet.to_dict(orient="records")
# print(alphabet)
# print('dict\n',alphabet.to_dict(orient="dict"))
# print('list\n',alphabet.to_dict(orient="list"))
# print('series\n',alphabet.to_dict(orient="series"))
# print('split\n',alphabet.to_dict(orient="split"))
# print('records\n',alphabet.to_dict(orient="records"))
# print('index\n',alphabet.to_dict(orient="index"))

alpha_dict= {}
for (index,row) in alphabet.iterrows():
    # print(index)
    # print(row)
    alpha_dict[row['letter']] = row['code']


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = pyask.ask_question('please provide a word:\n',str)
result = []
for i in user_input:
    # print(i)
    # print(alpha_dict[i.upper()])
    result.append(alpha_dict[i.upper()])

print('-'.join(result))


