import json
from collections import ChainMap

file_name = 'lines-by-season.json'
all_seasons = [str(x) for x in range(1,19)] 

with open(file_name, "r") as read_file:
    data = json.load(read_file)

total_season_activity = []
for season in all_seasons:
    max_lines = 0
    max_words = 0
    for character in data[season]:
        if character['number_of_lines'] > max_lines:
            has_most_lines = character
            max_lines = character['number_of_lines']
        if character['number_of_words_spoken'] > max_words:
            has_most_words = character
            max_words = character['number_of_words_spoken']
    total_season_activity.append({season: {'character_with_most_lines': has_most_lines, 'character_with_most_words': has_most_words}})
 

json_data_string = json.dumps(total_season_activity, indent=4)
final_file = 'who-speaks-most-per-season.json'

with open(final_file, "w") as outfile: 
    outfile.write(json_data_string)