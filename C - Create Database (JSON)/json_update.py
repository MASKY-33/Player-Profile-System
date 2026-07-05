import json

with open("profile.json", "r") as file:

    loaded_data = json.load(file)

    loaded_data["score"] = 730

with open("profile.json", "w") as file:

    json.dump(loaded_data, file)

print("Data updated successfully!")