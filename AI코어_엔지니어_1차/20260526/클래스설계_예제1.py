
class MyDataControl():  # 클래스 정의
    def __init__(self,*arg):
        #print("객체 생성 완료!!")
        #print(arg)
        # 멤버변수 등록하고 초기화
        self.m_arg = arg   # m_arg 라는 멤버변수가 ( 50,... 90) 이라는 튜플객체를 참조

    def SumofData(self):
        # 합을 계산하는 로직은 여기서...
        #print(self.m_arg)
        total = 0
        for x in self.m_arg:
            total += x
        print('total : ', total)  # 50,60,70,80,90 의 합을 출력

# 객체생성 ==> 객체가 생성될때  "객체 생성 완료!!" 를 출력
value = MyDataControl(50,60,70,80,90)  # 객체를 메모리에 생성했으면 변수로 참조해야함.
value.SumofData() # 50,60,70,80,90 의 합을 출력



