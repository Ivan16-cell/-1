# TODO решите задачу
#def task() -> float:
#    ...


#print(task())


import json



import json


def task() -> float:
    with open("input.json", "r") as f:
        data = json.load(f)

    total_sum = 0
    for item in data:
        total_sum += item["score"] * item["weight"]

    return round(total_sum, 3)


print(task())

# TODO Сериализовать в файл с отступами равными 4
# TODO импортировать необходимые молули