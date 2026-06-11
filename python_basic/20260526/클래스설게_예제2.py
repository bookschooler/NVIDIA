class PersonInfo():
    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
        self.city = args[2]
    def Display(self):
        print(f"이름: {self.name}, 나이: {self.age}, 지역: {self.city}")

per1 = PersonInfo("Hong", 30, "Seoul")
per2 = PersonInfo("Kim", 50, "Daejeon")
per3 = PersonInfo("Park", 40, "Busan")

perlist = [per1 , per2 , per3]
for item in perlist:
    item.Display()    # "이름: Hong, 나이: 30, 지역: Seoul"
    print('='*40)


