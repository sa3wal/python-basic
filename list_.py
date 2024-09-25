# list.py

# 변수 = ['값', 값]       => 값의 자료형은 상관X
# 위 형식으로 선언
# 리스트란 여러개의 자료형을 하나의 변수에 순서대로 모아둔것
# 모아둔 자료형의 순서는 0부터 시작한다 => 인덱스(index) 번호라고 얘기
# 리스트의 값을 가지고 올 때는 대괄호([])를 이용하여 참조

# list1 = [1,'asdf',True]
# print(list1[0])       # list1 리스트의 0번째 값을 출력
# print(list1[2])
# print(list1[3])       # list1 리스트의 3번째 값은 없으므로 애러 발새애애애앵


#========================================================================================#


# 인덱스 번호를 이용해서 해당 인덱스 번호에 있는 값을 수정할수 있다.
# 값 변경은 변수에 값을 저장하는 것처럼 진행하면 된다.
# list1 = [1,'asdf',True]
# print(list1)

# list1[1] = 'hello'  # list1의 1번째 인덱스의 값을 변경
# print(list1)


#========================================================================================#

# list1 = ['abc', 'dfg', 'hij', 123, 456]
# print(list1)
# print()

# print('Q1. list1의 1번쨰 원소를 partk로 고치시오')
# list1[1] = 'park'
# print(list1)
# print()

# print('Q2.변수 으름을 arr로 하고 아래 리스트를 대입(저장)하시오')
# arr = [4,8,12,16,20,24,28,32]
# print(arr)
# print()

# print('Q3.arr의 4번째 원소를cit로 하시오.단 맨 왼쪽의 원소가 0번째 원소.')
# arr[4] = 'cit'
# print(arr)
# print()

# print('Q4.print(list1) 와 print(arr)응 실행하시오.')
# print(list1)
# print(arr)


#========================================================================================#


# test = ['test', 1, 8, 'hi', '3.15']

# for i in test:  # 기존에 배웠던 for문에 range 자리에 리스트를 넣어서
#                 #리스트 내용을 전부 출력할수 있음
#     print(i,end=" ")

# print()


#========================================================================================#


# name = ['지훈','서준','시찬','운서']
# score = [92,96,98,100]

# avg = (score[0]+score[1]+score[2]+score[3]) / 4

# print('평균은',avg,'이고',name[3],'가 가장 점수가 높습니다')
# print(sum(score) / len(score))


#========================================================================================#


# 리스트 함수

# 리스트명.insert(인덱스 번호,추가할 값)
# insert()함수는 인덱스 번호 위치에 값을 추가, 기본 위치에 있는 값은 뒤로 밀림
# 인덱스 번호가 리스트의 범위를 벗어나는 경우 값을 리스트 제일 뒤에 추가됨

# 리스트명.append(추가할 값)
# append()함수는 리스트 제일 뒤에 값을 추가

# del(리스트명[인덱스 번호])
# del()함수는 인덱스 번호에 해당하는 값을 리스트에서 삭제
# 만약 삭제한 위치 뒤에 값이 있으면 앞이로 당겨짐
# 인덱스 번호가 범위를 벗어나면 에러 발생

# 리스트명.remove(삭제할 값)
# remove() 함수는 리스트에서 특정값을 삭제
# 만약 삭제할 값이 여러개면 제일 앞에 있는 한개의 값만 삭제
# 만약 삭제할 값이 리스트에 없으면 에러발생

# 리스트명.index(인덱스 번호를 찾을 값)
# index()함수는 특정 값의 인덱스 번호를 알려줌
# 특정값이 여러개면 가장 앞에 있는 인덱스 번호를 알려줌
# 값이 리스트에 없을경우 에러발생

# len(리스트명)
# len()함수는 리스트의 크기(길이)를 알려줘버리고르곤졸라피자가자지구펄찰육오사삼이일본메로우

# sum(리스트명)
# sum()함수는 리스트의 값을 전부 더해줌, 리스트 내부의 값이 전부숫자일 경우만 가능

# 리스트면.count(개수를 알고 싶은값)
# count()함수는 특정 값이 리스트에 맞게 있는지 알려줌
# 만약 특정값이 리스트에 몇개 있는지 알려줌
# 만약 특정값이 르스트에 없으면 0

# 리스트명.sort()
# sort함수는 르스트의 내용을 오름차순으로 정렬

# insert()와 같이 리스트 변수와 .을 같이 사용하는 함수는 리스트에서만 사용가능하고
# del(),len(),sum()의 경우는 리스트 외 다른 자료형에서도 사용가능


#========================================================================================#


# list0 = []
# print(list0)
# print()

# print("Q1. append 함수를 사용해 list0에 1,2,3,4,5,6,7,8,9를 차례로 추가하시오(반복문을 사용해도 좋다)")
# for i in range(1,10,1):     # list0 을 변수로 삼는게 아니라 i라는 딴 변수를 하나 더 만들어서 쓰는거임
#     list0.append(i)
# print(list0)
# print()

# print('Q2.insert함수를 사용해 list0의 0번쨰에 0을 추가하시오')
# list0.insert(0,0)
# print(list0)
# print()

# print('Q3.del 함수를 이용해 list0의 3번째 원소를 삭제하시오.')
# del(list0[3])
# print(list0)
# print()

# print('Q4.del 함수를 이용하여 list0의 5번째 원소를 삭제하시오')
# del(list0[5])
# print(list0)
# print()

# print('Q5.remove 함수를 이용해 list0에서 1을 삭제하시오.')
# list0.remove(1)
# print(list0)
# print()

# print('Q6.index함수를 이용해 list0에서 5가 몇번째에 위치헀는지 출력하시오')
# print(list0.index(5))
# print()

# print('Q7.index 함수를 이용해 list0에서 6이 존재하는지 확인하시오.몇번쨰에 위치했는지 출력하시오')
# try :                       #try밑에있는 코드를 실행하는데
#     print(list0.index(6))
# except :                    #만약에 그 코드가 에러며는 except 밑에있는 코드 실행함
#     print("error")
# print()

# print('Q8.len 함수를 이용해 list0의 원소의 개수를 출력하시오')
# print(len(list0))
# print()

# print('Q9.print(list0)을 해서 출력하시오')
# print(list0)


#========================================================================================#


print('점수를 입력하세요(끝낼시 0을 입력)')
scores = []
score = int(input())        # 숫자로 입력

while(score != 0):          # while은 값이 true일때 실하하는거임 if랑 같게 생각하면 안되엠
    scores.append(score)
    if score == 0:          # 변수명 햇갈리면 앙됨
        break
    score = int(input())    # score에다가 숫가값을 입력함 위 반복문은 입력된 값을 반목만 하지 값을 넣는게 아님

# print(scores)
print('평균은', sum(scores) / len(scores), '입니다')
