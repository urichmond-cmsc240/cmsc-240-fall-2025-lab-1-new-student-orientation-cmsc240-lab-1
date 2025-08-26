# make files from menu.txt

import os

# remove all other files not starting with _
for filename in os.listdir():
    if not filename.startswith("_"):
        os.remove(filename)

with open("_MENU.txt") as f:
    # create a file for each menu item
    # replace " " with _ and end with .txt
    for line in f:
        filename = line.lower().strip().replace(" ", "_") + ".txt"
        with open(filename, "w") as item_file:
            item_file.write(line)
            
            # add an emoji for the closest food item
            # apparently, this does not exist yet! What a good program idea 🤔
            #item_file.write("🍔")