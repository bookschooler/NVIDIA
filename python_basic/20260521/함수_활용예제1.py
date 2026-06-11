
def EncryptFunc(msg):
    #print(msg)
    for s in msg:
        if s in EncBook:
            msg = msg.replace(s, EncBook[s])
    return msg

def DecryptFunc(encmsg):
    # EncBook 과 반대된 사전이 필요하다
    DecBook = {}
    for key in EncBook:
        DecBook[ EncBook[key] ] = key
    #print(DecBook)
    for s in encmsg:
        if s in DecBook:
            encmsg = encmsg.replace(s, DecBook[s])
    return encmsg  # 복호화된 문자열

stringdata = "I love ai python programming"
EncBook = {'l':'#', 'p':'@', 'o':'7', 'g':'$', 'I':'%', 'a':'8', 't':'*','r':'3','n':'6'}
encmsg = EncryptFunc(stringdata) # 전달된 문자열을 암호화 시켜서 반환하는 함수 호출
print(encmsg) # % #7ve 8i @y*h76 @37$38mmi6$
# 위 암호화된 문자열 다시 복원시키는 함수를 구현

decmsg = DecryptFunc(encmsg)
print(decmsg)  # I love ai python programming