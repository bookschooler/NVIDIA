# 파이썬은 객체지향언어(OOP)
# 파이썬은 기본적으로 다양한 클래스를 제공 (int, float, str etc)
from xml.sax import parseString

# 클래스를 바탕으로 객체를 생성하고 생성된 객체를 변수로 참조해서 동작하는 언어
# ==> 파이썬 프로그램 기본 동작

data1 = int(50)   # 클래스를 바탕으로 객체를 생성하는 문법 => 클래스명()
# data 변수는 50이라는 정수 객체를 참조하는 역할
# data = 50
# 동적 타이핑언어: 타이핑하는 순간 자료형 결정
print(data1, type(data1), id(data1))
data2 = "python"
print(data2, type(data2), id(data2))

# 파이썬의 변수는 어떤 객체의 ID든 저장이 가능하고 참조가 가능함!
# 특정 객체의 id를 저장해서 특정개체의 참조하는 역할이 파이썬 변수의 역할

# Bool 타입 => True , False를 저장하 수 있는 타입을 제공
data3 = True
print(data3, type(data3), id(data3))

class MyClass():
    def __init__(self, arg):
        self.mdata = arg

# 객체 생성
mydata = MyClass(80)
print(mydata.mdata, type(mydata.mdata), id(mydata.mdata))
