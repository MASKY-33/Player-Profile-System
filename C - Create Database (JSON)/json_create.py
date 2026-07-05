# 1. Import JSON
import json


# 2. Create the database
players_profile = {"name" : "MASKY", "score" : 500}


# 3. Open JSON-file in the disk-mode
with open("profile.json", "w") as file:


    # 4. Push the database directly inside the hard-disk
    json.dump(players_profile, file)


print("JSON-dabatase successfully created!")