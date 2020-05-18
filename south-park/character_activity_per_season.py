import json
from collections import ChainMap

file_name = 'south-park.json'
final_file = 'character-activity-per-season.json'

with open(file_name, "r") as read_file:
    initial_data = json.load(read_file)

all_seasons_set_list = list(set([line['season'] for line in initial_data])) # code smell?
all_seasons_set_list.remove('Season')

all_seasons_as_int = [int(x) for x in all_seasons_set_list]
all_seasons_as_int.sort()

all_seasons = [str(x) for x in all_seasons_as_int]

lines_per_season = []

for season in all_seasons:
    season_lines = []
    print(f'Current season: {season}')
    for line in initial_data:
        if line['season'] == season:
            season_lines.append(line)
    lines_per_season.append({season: season_lines})

data = dict(ChainMap(*lines_per_season))
json_string = json.dumps(data, indent=4)

# with open(final_file, "w") as outfile: 
#     outfile.write(json_string)

## Phase 2: list of dicts that go like --> season 1: {'character': ['line', 'line']}
all_characters = list(set([line['character'] for line in initial_data])) # code smell
all_characters.sort()

all_lines_by_season = []

# mock_all_seasons = ['1', '2']
# mock_all_characters = ['Stan', 'Kyle', 'Kenny', 'Chef', 'Cartman']

for season in all_seasons:
    print(f'Current season: {season}')
    current_key_season = data[season] # data['1']
    lines_by_characters_per_season = []
    for character in all_characters:
        print(f'Current character: {character}')
        character_lines = []
        for item in current_key_season:
            if item['character'] == character:
                character_lines.append(item['line'])
        
        # num of words spoken
        all_lines_as_compiled_string = ' '.join(character_lines)
        num_of_words_spoken = len(all_lines_as_compiled_string.split())
        
        if character_lines:
            character_lines_dict = {character: character_lines, 'number_of_lines': len(character_lines), 'number_of_words_spoken': num_of_words_spoken} # {stan: ['', '']}
            print(f'character lines dict: {character_lines_dict}')
            lines_by_characters_per_season.append(character_lines_dict) # [ {stan: ['', '']}, {kenny: ['', '']}, ]
            print(f'array: {lines_by_characters_per_season}')

    all_lines_by_season.append({season: lines_by_characters_per_season})

print('fertig!')
    
lines_by_season_data = dict(ChainMap(*all_lines_by_season))
json_lines_by_season_string = json.dumps(lines_by_season_data, indent=4)
lines_by_season_file = 'lines-by-season.json'

with open(lines_by_season_file, "w") as outfile: 
    outfile.write(json_lines_by_season_string)
    
            

