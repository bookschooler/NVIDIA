# 객체지향언어(OOP, Object Oriented Programming)
# 클래스를 기반으로 객체르 생성해서 프로그램이 동작하는 프로그램

# 클래스 ==> 정보를 담는 역할의 멤버변수, 멤버변수를 접근해서 관리는 멤버함수(메서드)
# 클래스 ==> 멤버변수 + 멤버함수(메서드)로 하나의 큰 자료형(타입)을 설계함
# 객체를 생성할 때 특정 클래스를 바탕으로 객체를 생성

# 기본 제공 클래스 ==> int(), float(), Bool(), str(), list(), tuple()
# ==> dict(), set()

# 사용자가 직접 정의 클래스 ==> 사용자 정의 클래스
# 클래스 정의 키워드 ==> class

class MyCls():  # 클래스 정의
    def __init__(self): # 멤버변수를 등록하고 초기화해주는 특수한 역할의 메소드(생성자역할)
    # print("__init__() 호출 됨!!")        # 멤버 변수
    local_val = 50  # 해당함수에서만 동작하는 지역등록 변수
    self.m_val = 100    # 객체의 멤버변수를 등록하고 초기화

    def Infodisplay(self):     # self는 해당 메소드를 어떤 객체가 호출했는지 객체의 정보가 자동으로 남는다
        print('self.m_val :', self.m_val)

# MyCls 클래스를 바탕으로 객체를 생성해야지만 프로그램이 동작
# 객체생성문법 ==> 클래스명()
data = MyCls()  # 객체가 생성되는 시점에서 자동으로 호출되는 특수한 메서드(생성자역할의 함수)
# print(data.m_val)   # 외부 접근
data.Infodisplay()

# mystr = "python"
# print(mystr.replace())
#
# mystrdata = "programming"
# print(mystrdata.replace())

# MyCls 클래스를 바탕으로 객체를 생성해야지만 프로그램이 동작
# 객체생성문법 ==> 클래스명()
data = MyCls(60) # 객체가 생성되는 시점에서 자동으로 호출되는 특수한 메서드(생성지역의 함수)
data.Infodisplay()

temp_data = MyCls("python programming")
temp_data.Infodisplay()