

class MyComInfo():
    def __init__(self, arg = "Python Academy"):  # arg = "Python Academy" / 디폴트파라미터
        self.name = arg

    def DisplayName(self):
        print(self.name)

    def SettingName(self, namearg):
        #print(self.name) # Python Academy
        self.name = namearg  # 멤버변수에 namearg 을 대입해서 멤버변수 내용을 수정

com1 = MyComInfo("AI Academy")
com1.DisplayName()  # AI Academy

# com2 = MyComInfo()
# com2.DisplayName() # Python Academy
#
# com2.SettingName("Agent Academy")
# com2.DisplayName() # Agent Academy