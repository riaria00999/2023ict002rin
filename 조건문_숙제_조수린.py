# -*- coding: utf-8 -*-
"""조건문 숙제 조수린

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XNgtWg9YxaPHD6I6PRdmn20NCUq17S9e
"""

#1번 문제

A,B = map(int, input().split())

if A > B:
    print(">")
elif A < B:
    print("<")
elif A == B:
    print("==")

#2번 문제
# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

score=int(input()) # 100>=score>=0

if 100>=score>=90:
  print("A")
elif 89>=score>=80:
  print("B")
elif 79>=score>=70:
  print("C")
elif 69>=score>=60:
  print("D")
else:
  print("F")

#3번 문제
# # 연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.

# # 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
# 첫째 줄에 연도가 주어진다. 연도는 1보다 크거나 같고, 4000보다 작거나 같은 자연수이다.
#(연도 % 4 == 0) and (연도 % 100 != 0 or 연도 % 400 == 0)

year=int(input())
if year%400==0: #400은 무조건 4의 배수
  print(1)
elif year%4==0 and year%100!=0:
  print(1)
else:
  print(0)



# 4번 문제
x=int(input())
y=int(input())

if x>0 and y>0:
  print(1)
elif x<0 and y>0:
  print(2)
elif x<-0 and y<0:
  print(3)
elif x<0 and y<0:
  print(4)

#  상근이가 설정한 알람 시각이 주어졌을 때, 창영이의 방법을 사용한다면, 이를 언제로 고쳐야 하는지 구하는 프로그램을 작성하시오.
# 첫째 줄에 두 정수 H와 M이 주어진다
#첫째 줄에 상근이가 창영이의 방법을 사용할 때, 설정해야 하는 알람 시간을 출력
#하루의 시작은 0:0(자정)이고, 끝은 23:59(다음날 자정 1분 전)이다. 

#1H=60M

H, M = map(int,input().split())

if M >= 45:
    M = M - 45
    print(H, M)
else:
    H = H - 1
    if H < 0:
        H = 23
    M = (M + 60) - 45
    print(H, M)

# 안풀림 오븐문제
H, M = map(int, input().split())
C = int(input()) 
total = M + C
if total < 60:
  print(H , total)

else:
    H = H + (total//60)
    M = total % 60
    if H + (total//60) >= 24:
      H = H - 24
      print(H, M)

#주사위

A,B,C = map(int, input().split())
if A == B == C:
    money = 10000+A*1000
    print(money)
elif A == B:
    money = 1000+A*100
    print(money)
elif A == C:
    money = 1000+A*100
    print(money)
elif B == C:
    money = 1000+B*100
    print(money)
else:
    money = max(A,B,C)*100
    print(money)

