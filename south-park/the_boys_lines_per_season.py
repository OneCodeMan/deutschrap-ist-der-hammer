## IN PROGRESS

import json
from collections import ChainMap

file_name = 'lines-by-season.json'
all_seasons = [str(x) for x in range(1,19)] 

with open(file_name, "r") as read_file:
    data = json.load(read_file)

all_the_boys = []
total_season_activity = []
the_boys = ['Cartman', 'Stan', 'Kyle', 'Kenny']
for season in all_seasons:
    for character in data[season]:
        for boy in the_boys:
            if boy in character:
                total_season_activity.append({season: character})
        all_the_boys.append(total_season_activity)

new_data = data = dict(ChainMap(*all_the_boys))
json_data_string = json.dumps(new_data, indent=4)
final_file = 'the-boys-lines-by-season.json'

with open(final_file, "w") as outfile: 
    outfile.write(json_data_string)