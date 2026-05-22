

#문제1)
def AlphaFindFunc(strdata):
    # chrdata = '#'  # 한문자 영문 소문자  범위에 속하냐?
    # print( chrdata >= 'a' and chrdata <= 'z' )
    # print( chrdata >= 'A' and chrdata <= 'Z')
    listdata = []
    for s in strdata:
        #'a' <= chrdata <= 'z' or 'A' <= chrdata <= 'Z'
        if s >= 'a' and s <= 'z':
            listdata.append(s)   # 영문 소문자 저장
        elif s >= 'A' and s <= 'Z':
            listdata.append(s)   # 영문 대문자 저장
    print(listdata)
    return "".join(listdata)


strdata = "# Ai % 3 pro&*graM"
result = AlphaFindFunc(strdata) # 함수호출
print('result : ', result) # AiprograM ==> 영문대소문자만 추출 출력

###############################################################

# 문제2)
def WordCountFunc(arglist):
    #print(arglist)
    worddict = {}
    for word in arglist:
        #print(word)
        if word in worddict:
            worddict[word] += 1  # value 를 1씩 증가시키겠다
        else:
            worddict[word] = 1  # 키 와 value를 새로 추가하는 구문

    #print(worddict)
    return worddict


listdata = [ 'python', 'ai', 'study', 'good', 'ai', 'python', 'ai']
result = WordCountFunc(listdata)
print('result : ', result) # { 'python':2, 'ai':3, 'study':1, 'good':1 }


# 문제3)
def InforCombine(arg1, arg2):
    # dictdata = {}
    # for idx, item in enumerate(arg1):
    #     print(item, arg2[idx])
    #     dictdata[item] = arg2[idx]
    dictdata = { item : arg2[idx] for idx, item in enumerate(arg1) }
    print(dictdata)
    return dictdata

key_list = ["name", "age", "address"]
value_list = ["Hong", 50, "seoul"]

result = InforCombine(key_list, value_list)
print('result : ', result) # {'name':"Hong", "age":50, "address":"seoul"}

import os
os.system("pause")