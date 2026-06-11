from audioop import avg

scorelist = [ ["Kor"], ["Eng"], ["Math"] ]
print(scorelist)

# 문제 : input함수를 이용해서 각 과목에 점수를 입력받아 저장하기.
# 결과물은 print(scorelist)     # [ ["Kor", 90], ["Eng", 80] --- ] 이런식으로 나오도록 만들어주기
# 학생의 총점과 평균을 계산해서 출력

# input을 차례대로 받아가지고 그걸 scorelist에 순서대로 추가함 (리스트니깐 append 쓰면 될 것 같음)
# input을 scorelist의 순서대로 받기 ? => socrelist[i]

score = []
score.append(int(input(f'점수: ')))    # input함수는 무조건 문자열 객체로 생성함.
score.append(int(input(f'점수: ')))    # input함수는 무조건 문자열 객체로 생성함.
score.append(int(input(f'점수: ')))    # input함수는 무조건 문자열 객체로 생성함.

print(score)

for i in range(len(scorelist)):
    scorelist[i].append(score[i])
    print(scorelist)

total = sum(score)
average = total/len(score)
print(total, average)

# 강사님 ver
#
# kor = int ( input("국어 점수를 입력해주세요: "))
# scorelist[0].append(kor)
#
# eng = int ( input("영어 점수를 입력해주세요: "))
# scorelist[1].append(eng)
#
# math = int ( input("수학 점수를 입력해주세요: "))
# scorelist[2].append(math)


