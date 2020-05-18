import json
from collections import ChainMap

file_name = 'south-park.json'
final_file = 'lines-by-character.json'

with open(file_name, "r") as read_file:
    data = json.load(read_file)

all_characters = list(set([line['character'] for line in data])) # code smell
all_characters.sort()


lines_by_character = []
for character in all_characters:
    character_lines = []
    print(f'Current character: {character}')
    for line in data:
        if line['character'] == character:
            character_lines.append(line['line'])
    lines_by_character.append({character: character_lines})
    print(f'{character} done.')

# print(lines_by_character[0])

data = dict(ChainMap(*lines_by_character))
json_string = json.dumps(data, indent=4)

with open(final_file, "w") as outfile: 
    outfile.write(json_string)
            

