#
# class MyCalList():
#     def __init__(self, arg1, arg2):
#         self.marg1 = arg1
#         self.marg2 = arg2
#
#     def Sumoflist(self):
#         print(self.marg1, self.marg2)
#         set1 = set(self.marg1)
#         set2 = set(self.marg2)
#         print( set1 - set2 )
#         # for idx, item in enumerate(self.marg1):
#         #     print(idx, item , self.marg2[idx])
#         #     listdata.append(  item + self.marg2[idx] )
#         # print( listdata )
#
#
# data = MyCalList( [5,6,7,9], [8,9,5,10] )
#                   #    [ 13, 15, 12, 19 ]
# data.Sumoflist()  #    [6,7] OR [7,6]
# #print(result) # [ 13, 15, 12, 19 ]

class StudentScore():
    def __init__(self , name, *arg):
        #print(name, arg)
        self.name = name   # 전달인자를 멤버변수화
        self.scoredata = arg

    def TotalData(self):
        total = 0
        for x in self.scoredata:
            total += x
        return total

    def scoredisplay(self):
        print(self.name, self.TotalData() ,  self.TotalData() / len(self.scoredata) )


Studentlist =[
    StudentScore("Hong", 80, 60, 70, 90),
    StudentScore("Kim", 90, 70, 80, 85),
    StudentScore("Park", 88, 66, 77, 99),
    StudentScore("Lee", 92, 72, 82, 82),

]

print("이름", "총점" , "평균" )
for student in Studentlist:
    student.scoredisplay()

# # 이름  총점  평균
# # Hong  368   92.5
# # Kim   360   90.5
# # park  350   91.5
# # Lee   340   93.5