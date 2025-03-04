from pathlib import Path
## text file

path = Path('my_list.txt')
contents = path.read_text()
print(contents)

new_path = Path("new_file.txt")
new_path = "Today was a day that was being a day."
new_path += "\n\tevery good day is gift\n\twelcome to new world"
new_path += "\nronny\nethan\npierre\nmarvelous"
new_path += "\n ethan is best research\n pierre is good in code\n marvelous is good in code"

path.write_text(new_path)



