
import json
INPUT_FILE = 'input.json'

def task(su=0) -> float:
    with open("input.json", "r") as f:
        data = json.load(f)

    total_sum = 0
    for item in data:
        total_sum += item["score"] * item["weight"]

    return round(total_sum, 3)


print(task())

