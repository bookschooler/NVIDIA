import pandas as pd
pets = [
    {"name":"구름", "수학":50 , "국어":90},
    {"name":"초코", "수학":30 ,"국어":90},
    {"name":"아지", "수학":100 ,"국어":90},
    {"name":"호랑이","수학":90 ,"국어":90}
]
mydf = pd.DataFrame(pets)
print(mydf)
# total = 0
# for item in pets:
#     print(item['name'], item['age'])
