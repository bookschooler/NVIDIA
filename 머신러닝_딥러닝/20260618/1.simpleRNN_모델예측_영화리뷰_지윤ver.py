from tensorflow.keras.models import load_model
from tensorflow.keras.datasets import imdb

(train_x, train_y), (test_x, test_y) = imdb.load_data(num_words = 5000)

from tensorflow.keras.preprocessing.sequence import pad_sequences
test_seq = pad_sequences(test_x, maxlen=100)

model = load_model('RNN_IMDB_bestmodel.keras')

test_pred = model.predict(test_seq[:5])
# print(test_pred)  
# print(test_y[:5])  

# imdb.load_data()함수활용 num_words개 만큼의 단어집합으로 리뷰 문장을
# 토큰화 진행할 경우 0(패딩), 1(문장시작), 2(untoken), 3(unused)은 특별 토큰으로 취급 및
# 추가 함으로 'this'단어는 11 + 3 ==> 14값으로 토큰화됨
# ==> IMDB 리뷰 데이터셋에서 정한 규칙임
# 실제 빈도수가 가장높은 'the' : 1 ==> 1+3 ==> 4값으로 토큰화됨

# 결론, word_to_index = imdb.get_word_index() 활용한 임의의 문장 데이터
# 토큰화 진행할 경우 +3 고려 해 진행 해야 함!! 🦀 , num_words개 단어집합 크기 고려!!
# imdb.load_data()로 토큰화 완료된 데이터로 훈련 했음으로
# 신규 데이터 예측에 있어서도 동일방법으로 토큰화 진행한 데이터로 예측 진행해야함


# word_to_index ==> {단어:정수, 단어:정수,..} , 정수 1부터 매핑
word_to_index = imdb.get_word_index() # <=== imdb 인덱스 매핑 사전 반환
# for key, value in word_to_index.items():
#     if value == 1:
#         print('key , value :',key, value) # key , value : the 1

# print(word_to_index['this']) # 11로 정수매핑 되있지만 --> 정수 토큰화된 내용은 14


# 임의의 영화 리뷰 문장 예측 
import re 

newdata_positive = "This movie completely exceeded my expectations from start to finish. The acting was outstanding and every character felt real and well developed. The story moved at a perfect pace and never felt boring even for a single moment. The music fit every scene beautifully and added so much emotion to the experience. I found myself laughing during the funny parts and feeling moved during the more serious moments. The ending tied everything together perfectly and left me with a smile on my face. I would happily watch this film again and recommend it to anyone."

newdata_negative =  "I really wanted to enjoy this movie but it turned out to be a huge disappointment. The story dragged on forever and nothing interesting happened until the very end. The acting felt flat and none of the characters were believable or worth caring about. Several scenes were so poorly written that I found myself laughing for the wrong reasons. The pacing was slow and the dialogue felt forced throughout the entire film. By the time it ended I was just relieved it was finally over. I would not recommend this movie to anyone."

# 애매한 데이터
# newdata =  "The movie started great but the ending was disappointing"
# newdata =  "Not the best film I have seen but still somewhat enjoyable"  # 99% 긍정 ==> rnn의 구조적 한계
newdata =  "The first half of this movie was genuinely impressive with strong performances and a clever story that kept me interested. However the second half completely fell apart with confusing plot twists and characters making decisions that made no sense at all. Some scenes were beautifully filmed while others felt rushed and poorly edited. The music was lovely but it could not save the weak script in the final act. I left the theater not knowing whether I liked it or not."
newnewdata = "This is not a perfect movie and it definitely has some flaws in the script but overall I still found myself enjoying the experience more than I expected going into the theater. The acting was solid even though the story was a little predictable at times. It was never amazing or unforgettable but it was also far from a disaster and I do not regret watching it."


# 숫자로 변환, 인코딩, 임베딩
def new_tokenization(arg):
    new_sentence = re.sub(r'[^0-9a-zA-Z\s]','', arg).lower()
    # 정수 인코딩
    encoded = []
    for word in new_sentence.split(' '):
        # 단어 집합 크기를 훈련데이터와 동일하게 5000으로 제한
        try:
            if word_to_index[word] <= 5000:
                encoded.append(word_to_index[word] + 3)
            else:
                # 5000 이상의 숫자는 알 수 없는 토큰으로 취급 (untoken ==> 2)
                encoded.append(2)

# 단어 집합에 알 수 없는 단어, 즉 word_to_index 사전에 word키가 없는 경우 알 수 없는 토큰(2)로 변환
        except KeyError:
            encoded.append(2)
    pad_new = pad_sequences([encoded], maxlen = 100)  # 훈련, 테스트 때와 동일하게 길이를 100으로 패딩

    # 예측
    # print(pad_new)
    score = float(model.predict(pad_new))
    # print('score:', score)
    if(score > 0.5):
        print("{:2f}% 확률로 긍정 리뷰".format(score*100))
    else:
        print("{:2f}% 확률로 부정 리뷰".format((1-score)*100))

new_tokenization(newdata_positive)
new_tokenization(newdata_negative)
new_tokenization(newdata)
new_tokenization(newnewdata)


# ====애매한 리뷰를 강하게 확신하여 판단하는 이유====
