

class PersonInfo():
    def __init__(self, name, age, local):
        self.name = name  # 멤버변수 화 ==> 멤버변수 등록과 동시 초기화
        self.age = age
        self.local = local

    def Display(self):
        print(f"이름 : {self.name}, 나이 : {self.age}, 지역 : {self.local}")

per1 = PersonInfo("Hong", 30, "Seoul")
per2 = PersonInfo("Kim", 50, "Deajun")
per3 = PersonInfo("Park", 40, "Pusan")

perlist = [per1, per2, per3]
for item in perlist:
    item.Display()   #"이름 : Hong, 나이 : 30, 지역 : Seoul"
    print('='*30)

