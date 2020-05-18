import json
from collections import ChainMap

# import matplotlib.pyplot as plt; plt.rcdefaults()
# import numpy as np
# import matplotlib.pyplot as plt

file_name = 'lines-by-character.json'
final_file = 'mr_mackey_stats.json'
all_seasons = [str(x) for x in range(1,19)] 

with open(file_name, "r") as read_file:
    data = json.load(read_file)

mr_mackey_lines = data["Mr. Mackey"]
m_kay_lines = []
mr_mackey_stats = {'mr_mackey': {'lines': [], 'count': 0}}

for line in mr_mackey_lines:
    if 'm\'kay' in line.lower():
        m_kay_lines.append(line)
    mr_mackey_stats['mr_mackey'] = {'lines': m_kay_lines, 'count': len(m_kay_lines)}


json_mkay = json.dumps(mr_mackey_stats, indent=4)
lines_by_season_file = 'mr-mackey.json'

with open(lines_by_season_file, "w") as outfile: 
    outfile.write(json_mkay)