import json
from collections import ChainMap

file_name = 'south-park.json'
all_seasons = [str(x) for x in range(1,19)] 

with open(file_name, "r") as read_file:
    data = json.load(read_file)

def get_conversations(key_phrase, characters, context_amount, final_file):
    final_arr = []

    for line in range(len(data)):
        current_line = data[line]['line'].lower()
        current_character = data[line]['character']
        if key_phrase in current_line and current_character in characters:
            context_lines = [{'character': data[item]['character'], 'line': data[item]['line']} for item in range(line - context_amount, line + context_amount)]
            final_arr.append(context_lines)

    final_data = {'count': len(final_arr), 'compilation': final_arr}
    json_string = json.dumps(final_data, indent=4)

    with open(final_file, "w") as outfile: 
        outfile.write(json_string)

get_conversations('learned something today', ['Kyle', 'Stan'], 3, 'learned-something.json')
get_conversations('screw you guys, i\'m goin', ['Cartman'], 3, 'screw-you-guys-im-going-home.json')
get_conversations('m\'kay', ['Mr. Mackey'], 3, 'm-kay.json')