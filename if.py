# 비교 연산자(if)
#비교 연산의 결과는 뮤조건 True or False 로 나옴

# ==        *같으면* True, *다르면* False
# !=        *다르면 True, *같으면* False
# <
# >
# <=
# >=

# print(5 != 2)
# print(5 < 2)


#========================================================================================#


# 조건식의 종류

# [가장 일반적인 형식]
# if(조건식):
#     if의 조건식이 True일 경우 실행할 코드

# elif(조건식):
#     elif의 조건식이 True일 경우 실행할 코드

# else:
#     위의 모든 조건식이 False일 경우 실행할 코드


# ----------[if만 사용한 경우]-----------

# if(조건식):
#     if의 조건식이 True일 경우 실행할 코드


# ---------[if랑 elif만 사용한 경우]----------
# if(조건식):
#     if의 조건식이 True일 경우 실행할 코드

# ---------[if랑 elif만 사용한 경우]----------

# if(조건식):
#     if의 조건식이 True일 경우 실행할 코드
# else:
#     위의 모든 조건식이 False일 경우 실행할 코드


# 위 형식들의 조건식이 있으면

# if는 무조건 1개,

# elif는 0개 ~ 무한대,

# else 는 0개 or 1개를 사용하여 조건문을 구성할수 있음

# @@@조건문은 조건문 안에 중첩하여 사용할수 있다@@@




#========================================================================================#




# score는 숫자로 입력받기
# 100 ~ 90    : A
# 89 ~ 70     : B
# 69 ~ 60     : C
# 59 ~        : D

# score = int(input())

# if(100 >= score >= 90):
#     print("A")
# elif(89 >= score >+ 70):
#     print('B')
# elif(69 >= score >= 60):
#     print('C')
# elif(59 >= score >= 60):
#     print('D')

# else:
#     print("제발 입력하다 점수 사이 0 과 100.")


# print('끝나다')



#========================================================================================#



# age = int(input())

# print('나이가 12세이상만 볼수있는 영화입니다요')

# if(age < 12):
#     print('꼬맹이는 나가새요^^')
# elif(age >= 12):
#     print('즐겁게 보고 나오세요~중간에 화장실 가시면 벌금 56700원 있으시구요 팝콘 11900원인데 하나 들고가시겠어요?으료수는 9800원입니다')




#========================================================================================#



# print('enter any number')
# number = int(input())

# if(number % 2 == 0):
#     print('zzack-su')
# elif(number % 2 != 0):
#     print('hol-su')



#========================================================================================#

# not         : True면 False, False 면 True로 결과를 뒤집음
# and         : 양옆이 전부 True면 True, 하나라도 False면 True
# or          : 양옆이 전부 False 면 False, 하나라도 True면 True
# 실행 순서는 not, and, or 순서로 실행됨

# a = 10
# b = 5
# if((a == 10) and ( b== 5)):
#     print('a=10,b=5')

# if((a==10) or (a==5)):
#     print('a와b 둘중 한개 이상은 10 입니다')

# if(not(a == 5)):
#     print('a = 5가 아님')


#========================================================================================#


# print('두 개의 숫자를 입력해주새요')
# number_1 = int(input())
# number_2 = int(input())

# int(number_1)
# int(number_2)

# print("어떤 계산을 실행할까요?")
# print("[  1. 곱하기   2. 나누기  3. 더하기  4. 빼기  ]")
# math = int(input())

# if math == 1:
#     # print(number_1 * number_2)
#     print( "곱하기를 선택하셨습니다",number_1,"*",number_2, "=", number_1 * number_2)
# elif math == 2:
#     # print(number_1 / number_2)
#     print( "나누기를 선택하셨습니다",number_1,"/",number_2,"=",number_1 // number_2)
# elif math == 3:
#     # print(number_1 + number_2)
#     print( "더하기를 선택하셨습니다",number_1,"+",number_2,"=",number_1 + number_2)
# elif math == 4:
#     # print(number_1 - number_2)
#     print( "빼기를 선택하셨습니다",number_1,"-",number_2,"=",number_1 / number_2)
# else:
#     print("다시 시도해주세요")