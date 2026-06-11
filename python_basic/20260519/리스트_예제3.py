listdata = [2, 5, 7, 3, 8, 6]
# 이걸 오름차순으로 정렬하고 싶음.

print(listdata.sort())  # 원 리스트 데이터를 기본적으로 오름차순으로 정렬
# 내부적으로는 정렬된 사본 객체를 생성하지 않고 직접 바꾼 거임.
# 함수의 리턴값(리턴구문)이 없을 경우 None 객체를 반환함!!
listdata.sort(reverse=True)
listdata1 = sorted(listdata)
print(listdata)
print(listdata1)

print(listdata.append(11))
