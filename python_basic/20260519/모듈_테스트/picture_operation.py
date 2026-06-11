def picture_func():     # 함수 정의
    print("사진 동작 완료!")

# 함수가 동작하려면 함수가 호출되어야함 ==> function call이라고 함

# 현재 파일이 실행 모듈일 경우 내부 특수 변수 __name__ 은 __main__을 갖음!!
# 해당 파일이 import 되는 모듈일 경우 __name__ 은 __모듈명(파일명)__ 을 갖음!

if __name__ == '__main__':
    print("__name__:", __name__)
    picture_func()  # 이게 함수 호출하는거임
