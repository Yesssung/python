# 백준 파이썬 오늘 날짜

# 서울의 오늘 날짜를 출력하는 프로그램을 작성하시오. (입력 없음)

# 파이썬 책 보고 타임 함수 쓴다 해서 일단 찾아봄 
import time    # 내장 함수 time 쓰기
time.strftime("%x", time.localtime(time.time())) # 이렇게 하면 04/19/25 이런 형식으로 출력

# 자바에서 출력 포맷 바꾸는거 배웠었는데 파이썬은 기억안남 데헷
# 찾아보니까 그냥 해당 포맷들 연결하면 되는거더라규
time.strftime("%Y-%m-%d", time.localtime(time.time())) 

# 근데 틀림 왜 틀렸는지 보니까 출력 형태가 '2025-04-19' 이렇게 따움표로 감싸져 있음
# print()로 출력하지 않으면 결과를 자동으로 보여주기 때문

print(time.strftime("%Y-%m-%d", time.localtime(time.time())))

# 이번엔 맞았겠지 했지만 여전히 틀림,, 왤까... 했는데 아래 힌트를 이제 봄..
# 채점 서버는 시간대(Timezone)는 UTC+0 이다.
# 다음은 채점 서버에서 KST 시간으로 2018년 3월 21일 오후 2시 7분 38초에 date 명령어를 실행시킨 결과이다.

# 서울 오늘 날짜를 출력하라더니 사용 시간대가 UTC 였다.(휴))
print(time.strftime("%Y-%m-%d", time.gmtime()))