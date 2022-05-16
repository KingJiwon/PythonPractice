# print(5)
# print(-10)
# print(3.14)
# print(1000)
# print(5+3)
# print(2*8)
# print(3*(3+1))
# print('풍선')
# print("나비")
# print("ㅋ"*9)
# print(5>10)
# print(5<10)
# print(True)
# print(False)
# print(not True)
# print(not (5>10))
#####변수#####
# name = "연탄"
# animal = "강아지"
# age = 4
# hobby = "산책"
# is_adult = age >= 3

# print("우리집 "+ animal +"의 이름은 "+ name +"이에요")
# print(name,"이는 "+ str(age) + "살이며, "+ hobby +"을 아주 좋아해요")
# print(""+ name +"이는 어른일까요?" +str(is_adult))

#####주석#####
# '''
# 여러문장
# 주석처리
# '''

#####Quiz#####
# station = "사당"
# station1 = "신도림"
# station2 = "인천공항"

# print(station, "행 열차가 들어오고 있습니다.")
# print(station1 + "행 열차가 들어오고 있습니다.")
# print(station2, "행 열차가 들어오고 있습니다.")

#####연산#####
# print(1+1)
# print(3-2)
# print(2**3)
# print(5%3)
# print(10//3)

# print(10>3)
# print(4>=7)
# print(10<3)
# print(3==3)
# print(4==2)
# print(1 != 3)
# print(not(1!=3)) #False

# print((3>0) and (3<5))
# print((3>0)&(3<5))
# print((3>0)or(3>5))
# print((3>0|(3>5))) #or과 같음
# print(5>4<3)

#####수식#####
# print(2 + 3 * 4)
# print((2 + 3) * 4)
# number = 2 + 3 * 4
# print(number)
# number = number +2
# print(number)
# number += 2
# print(number)
# number *= 2
# print(number)
# number %= 2
# print(number)

#####숫자 처리 함수#####
# print(abs(-5)) # 5
# print(pow(4,2)) # 4^2
# print(max(5,12)) # 12
# print(min(5,12)) # 5
# print(round(3.14)) # 3
# from math import *
# print(floor(4.99)) #내림
# print(ceil(3.14)) #올림
# print(sqrt(16)) # 제곱근 4

#####랜덤함수#####
# from random import *
# print(random()) #0.0 ~ 1.0 미만의 임의의 값 생성
# print(random()*10) ##0.0 ~ 10.0 미만의 임의의 값 생성
# print(int(random()*10))
# print(int(random()*10 + 1))
# print(int(random() * 45 + 1))
# print(randrange(1,46)) #1~45 이하의 임의의 값 생성
# print(randint(1, 45)) #1~45 이하의 임의의 값 생성 (두값 모두 포함)

#####퀴즈2#####
# from random import *
# date = randint(4, 28)
# print("오프라인 스터디 모임 날짜는 매월 " + str(date) + " 일로 선정되었습니다.")

#####문자열#####
# sentence = '나는 소년입니다'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence3)

##### 슬라이싱 #####
# jumin = "980708-1234567"
# print("성별 : " + jumin[7])
# print("년도 : " + jumin[0:2])
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])
# print("생년월일 : " + jumin[:6]) #처음부터 6직전까지
# print("뒤 7자리 : " + jumin[7:]) #7번부터 끝까지
# print("뒤 7자리 : " + jumin[-7 :]) #맨뒤에서 7번째부터 끝까지

##### 문자열 처리 함수 #####
# python = "Python is Amazing"
# print(python.lower()) #소문자로 변환
# print(python.upper) #대문자로 변환
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "Java"))
# index = python.index("n") #index 찾기 , 없으면 오류
# print(index)
# index = python.index("n", index + 1) # 2번쨰 n 찾기
# print(index)
# print(python.find("n"))
# print(python.find("Java")) # java없음 -1
# print(python.count("n")) # 몇번 나왔는지

##### 문자열 포멧 #####
# print("나는 %d살입니다." % 20) #정수
# print("나는 %s을 좋아해요" %"파이썬") #문자열
# print("Apple은 %c로 시작해요" % "A") #문자
# # %s <<범용 가능
# print("나는 %s색과 %s색을 좋아해요" % ("파랑","빨강")) # 여러 문자열 

# print("나는 {}살입니다.".format(20)) # {}와 .format을 이용한 포멧
# print("나는 {}색과 {}색을 좋아해요".format("파랑", "빨강"))
# print("나는 {1}색과 {3}색을 좋아해요".format("파랑", "빨강", "노랑", "초록"))
# print( "나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color = "빨강"))

# age = 20
# color = "빨강"
# print(f"나는 {age}살이며, {color}색을 좋아해요") # python3.6이상에서 가능

##### 탈출 문자 #####
# print("백문이 불여일견 \n백견이 불여일타") # \n : 줄바꿈
# print('저는 "지원"입니다')
# print("저는 \"지원\"입니다.")

# print("C:\\Users\\Jiwon\\Desktop\\Python workspace") # \\ : 문장내에서 \쓰기
# print("Red Apple\rPine") # \r: 맨 앞으로 이동
# print("Redd\bApple") # \b : 한 글자 삭제
# print("Red\tApple") # \t : 탭

##### 퀴즈3 #####
#비밀번호 만들기 프로그램
# url = "http//youtube.com"
# pwd = url.replace("http//","")
# pwd = pwd[:pwd.index(".")] #pwd 문자열중 처음부터 .이전까지만 자름
# pwd1 = pwd[:3]
# pwd2 = len(pwd)
# pwd3 = pwd.count("e")
# pwd4 = "!"
# password = pwd1 + str(pwd2) + str(pwd3) + pwd4
# print("{0}의 비밀번호는 {1}입니다.".format(url, password))

##### 리스트 #####
# subway = [10, 20, 30]
# print(subway)
# subway = ["유재석", "조세호", "박명수"]
# print(subway)
# print(subway.index("조세호"))
# subway.append("하하") #인덱스 추가
# print(subway)
# subway.insert(1, "정형돈") # 인덱스에 끼워넣기
# print(subway)
# print(subway.pop()) # 인덱스 뒤에서부터 빼기
# print(subway)
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석")) # 동일한 인덱스 count
# num_list = [5,2,4,3,1]
# num_list.sort() # 정렬
# print(num_list)
# num_list.reverse()
# print(num_list) # reverse시키기
# num_list.clear() # list안의 모든 내용 삭제
# print(num_list)
# num_list = [5,2,4,3,1]
# mix_list = ["조세호", 20, True]
# print(mix_list)
# num_list.extend(mix_list) #list 합치기
# print(num_list)

##### Dictionary #####
# cabinet = {3: "유재석", 100 : "김태호"}
# print(cabinet[3]) #key값 대입
# print(cabinet[100])
# print(cabinet.get(3))
# print(cabinet[5]) #값이 없는경우 오류 프로그램 종료
# print(cabinet.get(5)) # 값이 없는경우 none 후 다음으로넘어감
# print(cabinet.get(5, "사용가능"))
# print("hi")
# print(3 in cabinet) # True 값의 유무 확인
# print(5 in cabinet) # False
# cabinet = {"A-3" : "유재석", "B-100" : "김태호"} 
# print(cabinet["A-3"])
# print(cabinet["B-100"])
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호" # 값 추가 및 update
# print(cabinet)
# del cabinet["A-3"] #값 지우기
# print(cabinet)
# print(cabinet.keys()) # key 출력
# print(cabinet.values()) # value 출력
# print(cabinet.items()) #key, value 출력
# cabinet.clear()
# print(cabinet)

##### tuple #####
# 변경 x 속도가 list보다 빠름
# menu = ("돈까스","치즈까스")
# print(menu[0])
# print(menu[1])
# menu.add("생선까스") # err 추가, 변경 불가능
# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)
# name, age, hobby = ("김종국", 20, "코딩")
# print(name, age, hobby)

##### set #####
# 중복 x, 순서없음
# my_set = {1,2,3,3,3}
# print(my_set)
# java = {"유재석","김태호","양세형"}
# python = set(["유재석","박명수"])
# print(java & python) # 교집합 출력
# print(java.intersection(python))# 교집합 출력
# print(java | python)
# print(java.union(python)) # 합집합 출력
# print(java - python)
# print(java.difference(python)) #차집합 출력
# python.add("김태호")
# print(python) # 추가
# java.remove("김태호")
# print(java) # 값 뺴기

##### 자료구조 변경 #####
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))
# menu = list(menu)
# print(menu,type(menu))
# menu = tuple(menu)
# print(menu,type(menu))
# menu = set(menu)
# print(menu,type(menu))

##### 퀴즈4 #####
# from random import *
# reple = range(1,21)
# reple = list(reple)
# winners = sample(reple,4)
# print("--- 당첨자 발표 ---")
# print("치킨 당첨자 : {}".format(winners[0]))
# print("커피 당첨자 : {}".format(winners[1:3]))
# print("--- 축하합니다 ---")

##### if #####
# weather = input("오늘 날씨는 어때요? ")
# if weather == "비" or weather =="눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요.")
# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp and temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요")

##### for #####
# for waiting_no in range(1, 6):
#     print("대기번호 : {0}".format(waiting_no))
# starbucks = ["아이언맨","토르","아이엠 그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

##### while #####
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비되었습니다. {1} 번 남았어요".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분 되었습니다.")
# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비되었습니다. 호출 {1} 회".format(customer,index))
#     index += 1
# customer = "토르"
# person = "Unknown"
# while person != customer :
#     print("{0}, 커피가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")

##### continue 와 break #####
# absent = [2,5] #결석
# no_book = [7]
# for student in range(1,11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))

#### 한 줄 for #####
# 출석번호 1,2,3,4 앞에 100을 붙임
# student = [1,2,3,4,5]
# student = [i+100 for i in student]
# print(student)
# #학생 이름을 길이로 변환
# student = ['Iron man', "Thor", "I am groot"]
# student = [len(i) for i in student]
# print(student)
# #학생 이름을 대문자로 변환
# student = ['Iron man', "Thor", "I am groot"]
# student = [i.upper() for i in student]
# print(student)

##### 퀴즈5 #####
from random import *

from pip import main
# cnt = 0
# for i in range(1,51):
#     time = randrange(5,51)
#     if 5 <= time <= 15:
#         print("[O] {0}번째 손님 (소요시간 :{1}분)".format(i,time))
#         cnt += 1
#     else :
#         print("[] {0}번째 손님 (소요시간 :{1}분)".format(i,time))
# print("총 탑승 승객 : {0} 분".format(cnt))

##### 함수 #####
# def open_account(): # 함수 선언
#     print("새로운 계좌가 생성되었습니다.")
# def deposit(balance, money): # 입금
#     print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
#     return balance + money #리턴
# def withdraw(blance, money): # 출금
#     if balance >= money: 
#         print( "출금이 완료되었습니다. 잔액은{0}원입니다.".format(balance - money))
#         return balance - money 
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
#         return balance
# def withdraw_night(balance, money): #저녁에 출금 ,수수료
#     commission = 100 # 수수료 100원
#     return commission, balance - money - commission #2개의 값 반환
# balance = 0
# balance = deposit(balance, 1000) 
# commission, balance = withdraw_night(balance, 500)
# print("수수료 {0} 원이며, 잔액은 {1}원 입니다.".format(commission, balance))

##### 기본값 #####
# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))
# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")
# 같은 학년 같은 반 같은 수업?
# def profile(name, age = 17, main_lang = "파이썬"): # 기본값 setting
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))
# profile("유재석")
# profile("김태호")

##### 키워드값 #####
# def profile(name, age, main_lang):
#     print(name, age, main_lang)
# profile(name = "유재석", main_lang = "파이썬", age=20)
# profile(main_lang= "자바", age = 25, name = "김태호")

##### 가변인자 #####
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}/t나이 : {1}\t".format(name, age),end = " ") # end사용 줄바꿈x
#     print(lang1,lang2,lang3,lang4,lang5)
# def profile(name, age, *language):
#     print("이름 : {0}/t나이 : {1}\t".format(name, age),end = " ") # end사용 줄바꿈x
#     for lang in language:
#         print(lang, end = " ")
#     print()
# profile("유재석",20,"Python","Java","C","C++","C#","JavaScript")
# profile("김태호",25,"Kotlin","Swift")

##### 지역변수와 전역변수 #####
# gun = 10

# def checkpoint(soldiers):
#     global gun #전역 공간에 있는 gun 사용
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 {0} ".format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 {0} ".format(gun))
#     return gun
# print("전체 총 : {0}".format(gun))
# #checkpoint(2)
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))

##### 퀴즈6 #####

# def std_weight(height, gender):
#     if gender == "남자" :
#         return height * height * 22
#     else:
#         return height * height * 21
# height = 1.75
# gender = "남자"
# weight = round(std_weight(height, gender),2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(int(height*100), gender, weight))

##### 표준 입출력 #####
# print("Python","Java",sep = ",", end = "?")
# print("무엇이 더 재밌을까요?")
# import sys 
# print("Python","Java",file = sys.stdout)
# print("Python","Java",file = sys.stderr)
# scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
# for subject,score in scores.items():
#     print(subject.ljust(6), str(score).rjust(4), sep = ":") # 6칸확보 왼쪽정렬. 4칸확보 오른쪽정렬
# for num in range(1,21):
#     print("대기번호 : " + str(num).zfill(3)) # 001, 002 등으로 변환
# answer = input("아무 값이나 입력하세요 : ") # 항상 문자열 형태로 저장됨.
# print(type(answer)) # 타입확인
# print("입력하신 값은 " + answer + "입니다.")