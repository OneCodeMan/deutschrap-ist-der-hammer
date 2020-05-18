import pandas as pd
import json

class Line:
    def __init__(self, season, episode, character, line):
        self.season = season
        self.episode = episode 
        self.character = character 
        self.line = line 
    
    def __str__(self):
        return_str = "{character}: {line} (season {season}, episode {episode})".format(character=self.character, line=self.line, season=self.season, episode=self.episode)
        return return_str
    
    def __repr__(self):
        return_str = "{character}: {line} (season {season}, episode {episode})".format(character=self.character, line=self.line, season=self.season, episode=self.episode)
        return return_str

CSV_FILE_NAME = 'south-park.csv' 
JSON_FILE_NAME = 'south-park.json'

sp_lines = pd.read_csv(CSV_FILE_NAME)

seasons = sp_lines.Season.to_list()
episodes = sp_lines.Episode.to_list()
characters = sp_lines.Character.to_list()
dialogue = sp_lines.Line.to_list()

number_of_lines = len(seasons)
lines = []

for i in range(number_of_lines):
    line = Line(seasons[i], episodes[i], characters[i], dialogue[i])
    lines.append(line)

lines_dict = [ob.__dict__ for ob in lines]
json_string = json.dumps(lines_dict, indent=4)

with open(JSON_FILE_NAME, "w") as outfile: 
    outfile.write(json_string)