import json
from collections import ChainMap

file_name = 'lines-by-season.json'
final_file = 'characters-most-dialogue-per-season.json'
all_seasons = [str(x) for x in range(1,19)] # ['1', ... , '18']

with open(file_name, "r") as read_file:
    data = json.load(read_file)

for season in data:
    max_dialogue = max(season, key=lambda y: y.grades).student_id

    
            

