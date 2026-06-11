# dict_a['name'] = "구름"
# print(dict_a)

import pandas as pd
pets = [
    {"name": "구름", "age": 5},
    {"name": "초코", "age": 3},
    {"name": "아지", "age": 1},
    {"name": "호랑이", "age": 1}
]

for a in pets:
    print(a['name'], str(a['age'])+'살')

for i in pets:
    name  = pet["name"]
    age = pet['age']
    print(f'{name} {age}살')
    # print(f'{name} {age}살')

result = [f"{pet['name']} {pet['age']}살" for pet in pets]
print(result)

# mydf = pd.DataFrame(pets)
# print(mydf)


