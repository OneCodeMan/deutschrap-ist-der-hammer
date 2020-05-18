# raw_character_text,spoken_words

import pandas as pd
import json

class Line:
    def __init__(self, character, spoken_words):
        self.character = character
        self.spoken_words = spoken_words 
    
    def __str__(self):
        return_str = f'{self.character}: {self.spoken_words}'
        return return_str
    
    def __repr__(self):
        return_str = f'{self.character}: {self.spoken_words}'
        return return_str

CSV_FILE_NAME = 'simpsons_dataset.csv' 
JSON_FILE_NAME = 'simpsons.json'

simpsons_lines = pd.read_csv(CSV_FILE_NAME)

characters = simpsons_lines.raw_character_text.to_list()
dialogue_lines = simpsons_lines.spoken_words.to_list()

number_of_lines = len(simpsons_lines)
lines = []

for i in range(number_of_lines):
    line = Line(characters[i], dialogue_lines[i])
    lines.append(line)

lines_dict = [ob.__dict__ for ob in lines]
json_string = json.dumps(lines_dict, indent=4)

with open(JSON_FILE_NAME, "w") as outfile: 
    outfile.write(json_string)