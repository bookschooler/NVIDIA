import re

string_exam = '파이썬, library 활용한 Text Preprocessing!!'

# library, Text, Preprocessing 인 한문자열로 출력

result = re.findall(r'[a-zA-Z]+', string_exam)

print(','.join(result))


