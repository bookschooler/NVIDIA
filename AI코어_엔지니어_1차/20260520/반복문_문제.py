
# 첫 알파벳 기준으로 시작되는 단어 모음
wordlist = [ 'car', 'apple', 'cattle', 'bar', 'book', 'air', 'cat' , 'korea', 'kick' ]

worddict = {}
# for 반복문 활용해서 구현
for word in wordlist:
    letter = word[0]
    if letter in worddict:
        worddict[ letter ].append(word)
    else:
        worddict[letter] = [word]

print(worddict) # { 'a':['apple','air'], 'b':['bar','book'], 'c':['car','cattle','cat']}
