import json

with open("profile.json", "r") as file:

    loaded_data = json.load(file)

print(f"Welcome back, {loaded_data['name']}! Your score is {loaded_data['score']}")