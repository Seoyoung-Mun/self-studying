user_input = input("나이를 입력하세요")
age = int(user_input)
if 1<=age<=7:
    print("유아")
elif 8<=age<=13:
    print("초등학생")
elif 14<=age<=16:
    print("중학생")
elif 17<=age<=19:
    print("고등학생")
elif 20<=age:
    print("성인")
