
class MyCalData():
    def __init__(self,arg):
        #print(arg)
        self.listdata = arg  # 멤버변수화

    def Avgdisplay(self):
        print(self.listdata)
        total = 0
        for item in self.listdata:
            total += item[1]
        print("평균 : {0:0.3f}".format( total / len(self.listdata) ) )


data = MyCalData( [ ("kim",100), ("Park",90), ("Hong",70) ] )
data.Avgdisplay()  #  (100 + 90 + 70) / 3 에 대한 평균을 출력