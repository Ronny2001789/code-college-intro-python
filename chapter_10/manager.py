from pathlib import Path
import json

numbers =  [1,2,3,4,5,]

json_Path = Path("number.json") 
content = json.dumps(numbers)

json_Path.write_text(content)

content = json_Path.read_text()
