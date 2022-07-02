#id = input("아이디를 입력 해 주세요")
#pw = input("비밀번호를 입력 해 주세요")

#f = open("/Users/MARY/Desktop/Folder/information.txt","b")


#if f == (id and pw) :
#    print("성공")
#else :
#    print("실패")

#f.close()
#다 틀림..ㅠㅠ

f = open("/Users/MARY/Desktop/Folder/information.txt","r")

infor = f.readlines() #리스트 단위(readlines)로 읽어서 저장

id = input("아이디를 입력하세요.")
pw = input("비밀번호를 입력하세요.")

flag = False 

for i in range(len(infor)): #텍스트 파일 내 끝날 때까지 반복
    information = infor[i].split()
    #infor를 information에 저장. 이때 리스트를 인수 하나하나 쪼개서 저장.
    #따라서 information도 리스트가 되고, information[0], information[1]에 하나씩 들어간다.
    if information[0] == id and information[1] == pw :
        flag = True
        break
    else:
        flag = False

if flag :
    print("로그인 성공")
else:
    print("로그인 실패")

