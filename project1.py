# 처음 파이썬 파일을 실행 시키면, 한식, 중식,
# 일식 중 한 가지를 고르라는 내용이 나옵니다.
# 그 중에서 한 가지를 고르면 식당 이름을 하나 임의로 추천해 줍니다.
#
import random

food = input("한식, 중식, 일식 중 한가지를 고르시오   ")

list_a = ["김밥천국", "한식뷔페", "계절밥상", "스님식당"]
list_b = ["대성각", "교동짬뽕", "탕수육맛집", "사천짜장"]
list_c = ["스시식당", "회식당", "우동식당", "라면식당"]

if food == "한식":
    print(random.choice(list_a))
else:
    if food == "중식":
        print(random.choice(list_b))
    else:
        if food == "일식":
            print(random.choice(list_c))

#미션 클리어
