# 사용자로부터 값을 입력받기!!
# input 은 입력받은 값을 "문자열"로 저장!!!!!!!!!!!!!1
# 한 줄에 결괏값 출력하기
# input 은 뭐.. 예시 없어도 되겠져..

# 파일로 읽고 쓰기 -> 파일을 통한 입출력
# 파일객체 = open(파일이름, 파일 열기모드)
# r=read, w=write, a=add -> w모드로 열 경우 기존에 데이터는 다 날라간다..조심..

# f = open("new file.txt", "w")
# f.close()

f=open("new file.txt", "w")
for i in range(1,11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()