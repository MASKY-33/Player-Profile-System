import json

with open("profile.json", "r") as file:

    loaded_data = json.load(file)

    del loaded_data["score"]

with open("profile.json", "w") as file:

    json.dump(loaded_data, file)

print(f"Data deleted successfully!")