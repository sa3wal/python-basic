# 변수(variable)
# 변수(variable) = 값
# 위 형식으로 변수에 값을 저장
# = 기호의 뜻과 다르게 단순하게 값이 변수에 저장됨
# 변수는 아래의 규칙을 지키면 원하는 대로 가능
#   1.숫자로 시작 불가능
#   2.기호 "__"를 제외한 특수문자 불가능
#   3.띄어쓰기 불가능
#   4.예악어 불가능

# my_name = 'kim'


# ================================================================================== #


# 자료형(Data type)
# str   ->  string              문자      -> 따옴표로 이루어짐(예외x) "_",'_'
# float ->  float               실수(소수) -> 따옴표가 없고 소수점이 있으면 실수
# int   ->  Integer             정수      -> 따옴표가 없고 소수점도없으면 정수
# 일상적으로 사용하는 언어(영어, 중국어, 한국어 등)이 따옴표가 없다 -> 오류

# a = 10      # a라는 변수에 int 자료형인 10 저장
# b ='kim'    # b라는 변수에 str자료형인 'kim' 저장


# name = '파이썬'
# age = 20
# height = 178

# print(name)

# name = '파이리'
# print(name)

# name = '파이팅'
# print(name)


# ================================================================================== #

# 형 변환(casting)
# str(변수 or 값)   -> 변수 or 값을 str 자료형으로 변환
# float(변수 or 값) -> 변수 or 값을 float 자료형으로 변환
# int(변수 or 값)   -> 변수 or 값을 int 자료형으로 변환
# 단순히 연산할때만 사용하면 원본의 값은 변허지 않음
# 원본의 자료형을 변환 시키기 위해서는 변수에 값을 다시 넣어야함 { EX. a = int(a) }

# var1 = 2
# var2 = '18'
# result = var1 + int(var2)       # result 변수에 var1 변수 + int 자료형으로 변환한 var2 변수 저장
# print(result)                   
# print(type(var2))               # 변수 var2 자료형을 출력, result 변수에는 int 자료형으로 계산이되었지만 실제 변수의 자료형은 변하지않음

# var2 = int(var2)                # var2 변수에 int자료형으로 변환한 var2 변수 저장
# print(type(var2))               # 변수 var2 자료형을 출력


# ================================================================================== #


# input('str' or 변수)
# 'str' 또는 변수를 출력한 후 엔터키를 누르기 전까지 키보드 입력을 받음
# 'str' 또는 변수는 생략 가능
# 변수 = input('문자' or 변수)
# 위 형식을 주로 사용, input()만 사용했을경우 입력 값을 저장하지 못함
# input()은 무조건 str 자료형으로 값을 저장함


# var1 = 2
# var2 = input("Insert anything : ")
# print(var2)
# print(type(var2))

# var2 = int(var2)
# print(type(var2))

# sum = var1 + var2
# print(sum)


# ================================================================================== #


print('안녕하세요 이름을 입력해주세요')

name = input()

print('반가워요', name, '님.',"나이도 냉큼 입력해주세요")

age = int(input())

year = int(2024)

print(year - age ,'년에 태어나셨구나', '이제 안궁금 하니까 키나 후딱 알려줘봐요')

tall = int(input())

two_m = int(200)

print('2미터까지',two_m - tall,'cm 남았구먼요?')

