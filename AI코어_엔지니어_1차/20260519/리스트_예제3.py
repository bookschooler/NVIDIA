
listdata = [2, 5, 7, 3, 8, 6]
# # 오름차순으로 정렬
# # 정렬 동작의 메서드(함수) 지원
# # 함수의 리턴값(리턴구문)이 없을 경우 None 객체를 반환함!!
# listdata.sort(reverse=True) # 원 리스트 데이터를 기본적으로 오름차순 정렬
# # reverse=True : 내림차순 정렬
# # 내부적으로 정렬된 사본 객체를 생성하지 않고 원본 데이터에  직접 반영
# print( listdata )

# 정렬 기능의 내부 함수 ( sorted )
#print(listdata)
sortedlist = sorted(listdata, reverse=True)  # 정렬된 사본 객체를 생성해서 반환
print(sortedlist)
print(listdata)
