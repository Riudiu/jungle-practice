
a = 7
b = 2

a+b   # 9 
a-b   # 5
a*b   # 14
a/b   # 3.5
a//b  # 3 (몫)
a%b   # 1 (나머지)
a**b  # 49 (거듭제곱)

a+3*b # 13 (여러 연산을 한 줄에 할 경우 사칙연산의 순서를 따른다.)

# 자바스크립트와 다르게 증감연산자(i++, i-- 등)는 없다.


y = 1
z = "a"
c = a
print(y, z, c) # 1 "a" 1

# d = x          # x라는 변수가 정의되지 않았기 때문에 에러메시지가 나온다.
d = "x"


a_list = []
a_list.append(1)     # 리스트에 값을 넣는다
a_list.append([2,3]) # 리스트에 [2,3]이라는 리스트를 다시 넣는다

a_list         # [1,[2,3]]
len(a_list)    # 2 리스트의 길이
a_list[0]      # 1
a_list[1]      # [2,3]
a_list[1][0]   # 2

a = [3, 3, 1]
b = [5, 2]

a + b  # [3, 3, 1, 5, 2]
a * 2  # [3, 3, 1, 3, 3, 1]


txt = '서울시-마포구-망원동'
result = txt.replace('-', '>')  # '서울시>마포구>망원동'


a = 4 > 2  # True
not a      # False    NOT 연산자로 참을 거짓으로, 거짓을 참으로 바꿔준다.

b = 2!=2   # False

a and b    # False    AND 연산자로 모두 참이어야 참을 반환한다.
a or b     # True     OR 연산자로 둘 중 하나만 참이면 참이다.


# 함수
# 참고: 자바스크립트에서는
# function f(x) {
#    return 2*x+3
# }

# 파이썬에서는
def f(x):
    return 2*x+3   # 중괄호 대신에 들여쓰기로 각 블록의 범위를 표시한다.

f(2)  # 7

def sum_all(a,b,c):
    return a+b+c


# 조건문
def is_adult(age):
    if age > 20:
        print('성인입니다') 
    elif age >= 13:
        print('청소년이에요')  # else if는 elif로 줄여쓴다.
    else:
        print('어린이네요!')

is_adult(30)           # 성인입니다


#반복문
fruits = ['사과','배','감','귤']

for fruit in fruits:
    print(fruit)

# 사과
# 배
# 감
# 귤

fruits = ['사과','배','감','귤']

for i in range(len(fruits)):  # i 가 0, 1, 2, 3일 때 
    fruit = fruits[i]	
    print(fruit)

# 사과
# 배
# 감
# 귤
    