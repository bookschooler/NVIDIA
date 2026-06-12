
scorelist = [ ["Kor"] , ["Eng"] , ["Math"] ]
print(scorelist)

# 문제
# input() 함수를 이용해서 키보드로 각 과목의 점수를 입력 받아 저장
kor = int( input("국어 점수를 입력 : ") )# 문자열 객체
scorelist[0].append(kor)

eng = int( input("영어 점수를 입력 : ") )# 문자열 객체
scorelist[1].append(eng)

math = int( input("수학 점수를 입력 : ") )# 문자열 객체
scorelist[2].append(math)

print( scorelist )   # [ ["Kor",'90'] , ["Eng"], ["Math"] ]


# 학생의 총점 과 평균을 계산해서 출력
total = scorelist[0][1] + scorelist[1][1] + scorelist[2][1]
print(total)

average = total / len(scorelist)
print("average : {0:.2f}".format(average))

