class MyComInfo():
    def __init__(self, arg = "Python Acadmy"):
        self.name = arg

    def DisplayName(self):
        print(self.name)

    def SettingName(self, namearg):
        self.name = namearg #멤버변수에 namearg 값을 대입해서 멤버변수 내용을 수정

com1 = MyComInfo("AI Academy")
com1.DisplayName()  # AI Academy

com2 = MyComInfo()
com2.DisplayName()

com2.SettingName("Agent Academy")
com2.DisplayName() # Agent Academy