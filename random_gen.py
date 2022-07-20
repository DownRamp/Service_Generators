import random
import json

results = []
# read in choice groups with choices
with open('json/selection.json') as f:
    data = json.load(f)

    # {choices:[choice1, choice 2]} etc.
    for i in data.choices:
        # pick selections and send back to user
        results.append(random.choice(i))
        
print(results)
