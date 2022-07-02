user_input = input("나이를 입력하세요")
age = int(user_input)

if age >= 20 :
    print("성인")
    if age % 2 == 0 :
        print("나이가 짝수인 성인")
    else :
        print("나이가 홀수인 성인")
else :
    print("미성년자")
    if age % 2 == 0 :
        print("나이가 짝수인 미성년자")
    else :
        print("나이가 홀수인 미성년자")
