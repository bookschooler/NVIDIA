class MyCalList():
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    # def Sumoflist(self):
    #     result = []
    #     for i in range(len(self.list1)):
    #         result.append(self.list1[i] + self.list2[i])
    #     print(result)
    def Minuslist(self):
        result = []
        for item in self.list1:
            if item not in self.list2:
                result.append(item)
        print(result)

data = MyCalList( [5,6,7,9], [8,9,5,10] )

# data.Sumoflist()  # [13, 15, 17]
data.Minuslist()

#===========================================================================

class StudentScore():
    def __init__(self, name, *scores):
        self.name = name
        list = []
        self.scores = list.append(scores)
        print(list)
    def scoredisplay(self):
        total = sum(self.scores)
        avg = total / len(self.scores)
        print(f'이름: {self.name}, 총점:{total}, 평균:{avg}')

Studentlist = [
    StudentScore("Hong", 80, 60, 70, 90),
    StudentScore("Kim", 90, 70, 80, 85),
    StudentScore("Park", 88, 66, 77, 99),
    StudentScore("Lee", 92, 72, 82, 82),
]

print("이름", "총점", "평균")
for student in Studentlist:
    student.scoredisplay()

