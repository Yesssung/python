def define_str():
    """
    함수 정의 연습
    :return:
    """
    # 문자열의 정의
    # 한 줄 문자열: "" or '' 둘 다 가능
    s1 = "Hello Python"         # 리터럴로 생성
    s2 = str("Hello Python")    # 문자열 타입함수로 생성
    s3 = str(3.14159)           # 다른 타입을 변환해서 생성
    print(s1, type(s1))
    print(s2, type(s2))
    print(s3, type(s3))

    print("s1은 str?", isinstance(s1, str))

    # 여러 줄 문자열: """ or '''
    s4 = """Life si too short, You need Python. 
파이썬은 데이터 처리가 중요한 시대에서 
가장 널리 사용되는 언어입니다."""
    print(s4)

    # 여러 줄 문자열은 한 줄 주석만 있는 파이썬에서
    # 여러 줄 주석을 사용하고자 할 때도 사용할 수 있다
    """여러 줄 문자열을 사용한 여러 줄 주석 메서드 정의
    바로 아래 여러 줄 주석을 추가하면 문서화 할 때 이용될 수 있고
    help명령어로 해당 메서드의 주석을 볼 수 있다."""

    # f-string : 문자열 포맷팅 방식 중 하나
    name, age = "홍길동", 28
    message = f"안녕하세요 {name} {age}세 입니다."
    print(message)

    width, height = 10, 5
    message = f"사각형의 면적은 {width * height} 입니다"
    print(message)


def string_oper():
    """
    문자열 연산
    """
    str1 = "First String"
    str2 = "Second String"
    # len(), 인덱싱 가능, 슬라이싱 가능, 포함 여부 판별
    # immutable, 치환이 불가능
    print(len(str1), len(str2))     # 길이

    # 인덱싱
    print(str1[0], str1[1], str1[2], "...", str1[9], str1[10], str1[11])
    print(str1[-12], str1[-11], str1[-10], "...", str1[-3], str1[-2], str1[-1])

    # 문자열은 immutable -> 치환 불가
    # str1[0] = "f"     # 변경 불가


    # 슬라이싱
    str1 = "First String"
    # [시작 경계 : 끝 경계 [:간격]]
    print(str1)
    print(str1[6:9])
    print(str1[-6:-3])

    print(str1[0:5])
    print(str1[:5])             # 처음부터 출력하고 싶다면 시작부분 생략 가능

    print(str1[6:len(str1)])    # 길이가 얼만지 모를때는 그냥 이런식으로 작성
    print(str1[6:])

    print(str1[::2])            # 처음부터 끝까지 간격 2
    print(str1[::-1])           # 간격 값이 음수면 역방향

def transform_methods():
    """
    대소문자 변환 관련 연습
    """
    s = "I like Python"

    print("UPPER: ", s.upper())                 # 모두 대문자로
    print("LOWER: ", s.lower())                 # 모두 소문자로
    print("CAPITALIZE: ", s.capitalize())       # 첫 글자만 대문자로
    print("TITLE: ", s.title())                 # 각 단어의 첫 글자만 대문자로 변환

    print("SWAPCASE: ", s.title().swapcase())   # 대 <-> 소

    # 불변 자료 -> 원본은 바뀌지 않음
    print("원본: ", s)

def search_methods():
    """
    문자열 검색 관련 예제
    """
    s = "I Like Python, I Like Java Also"
    print("COUNT: ", s.count("Like"))                # 문자열 내부의 Like 갯수

    # Like를 찾아봅시다 : find
    index = s.find("Like")                           # 문자열 내부의 첫 번째 Like
    print("1st Find: ", index)
    index = s.find("Like", 6)            # Index 6부터 검색
    print("2nd Find: ", index)
    index = s.find("Like", 21)           # Index 21부터 검색
    print("3rd Find: ", index)                       # 찾을 검색어가 없으면 -1

    # Like를 찾아봅시다 : index
    print("1st Index: ", s.index("Like"))
    print("2nd Index: ", s.index("Like",6))
    # print("3rd Index: ", s.index("Like", 21))      # 찾을 수 없기 때문에 에러 발생

    # 방법1. 예외처리
    # 방법2. 먼저 검색어 포함 여부를 확인 후 검색
    if "Like" in s[21:]:                             # 포함여부
        print("3rd Index: ", s.index("Like", 21))
    else:
        print("21번 인덱스 이후에는 Like 없음")

    # 역방향 검색 : find
    print("RFIND: ", s.rfind("Like"))               # 17
    print("RFIND: ", s.rfind("Like",0,17))

    # 문자열이 특정 문자열로 시작되는가?
    url = "http://www.naver.com"
    surl = "https://www.google.com"
    ftp = "ftp://ftp.naver.com"

    print("STARTSWITH:", url.startswith("http://"))
    print("STARTSWITH:", surl.startswith("https://"))
    print("STARTSWITH:", ftp.startswith(("http://", "https://")))       # 검색 대상이 여러개일때는 튜플형식으로 쓴다

    # 문자열이 특정 문자열로 끝나는가?
    print("ENDSWITH:", url.endswith("naver.com"))
    print("ENDSWITH:", surl.endswith("naver.com"))

    # startswith, endswith에서 검색 범위를 제한
    print("STARTSWITH:", ftp.startswith("ftp.", 6, len(ftp)))

def modify_replace_method():
    """
    문자열 수정, 치환 관련 메서드 연습
    """
    s = "     Alice and the Heart Queen     "
    print("STRIP:[", s.strip(), "]", sep="")            # sep -> ""공백으로 구분
    print("LSTRIP:", s.lstrip(), "]", sep="")           # 왼쪽 여백만 제거
    print("RSTRIP:", s.rstrip(), "]", sep="")           # 오른쪽 여백만 제거

    s = "---------- Alice and the Heart Queen ----------"
    print("STRIP -:[", s.strip("-"), "]", sep="")

    # Java -> Python
    s = "I Like Java"
    print("REPLACE:", s.replace("Java", "Python"))
    print("원본:", s)                 # str은 immutable -> 문자열은 변경되지 않는다. Python으로 바꿨어도 데이터 자체가 바뀐것은 아님


def align_methods():
    """
    문자열 정렬 관련 메서드
    """
    s = "Alice and the Heart Queen"
    print("CENTER:[", s.center(60), "]", sep="")
    print("CENTER:[", s.center(60,"*"), "]", sep="")
    print("LJUST:[", s.ljust(60, "*"), "]", sep="")
    print("RJUST:[", s.rjust(60, "*"), "]", sep="")

    print("ZFILL:", "1234".zfill(5))        # 다섯자리 출력공간 확보, 내용 채운 후 빈 공간에 0으로 채운다 -> 출력: 01234
    print("ZFILL:", "123456".zfill(5))      # 확보한 공간이 다섯자리지만 문자열이 그것보다 넘는다고 잘리지는 않는다. 최소 확보 5 라는 뜻


def split_join_method():
    """
    문자열 분할과 합치기 관련 메서드
    """
    s = "Ham and Cheese and Bread and Ketchup"
    print("SPLIT:", s.split())                      # 기본적으로 공백을 기준으로 단어 분리 해줌 -> 리스트

    ingr = s.split(" and ")                         # " and "를 기준으로 분리
    print("SPRIT:", ingr)
    print("JOIN:", ", ".join(ingr))                 # ingr리스트를 , 중심으로 합침

    print(s.split(" and ", 2))          # 앞에서 2개만 분리
    print(s.rsplit(" and ", 2))         # 뒤에서 2개만 분리

    # 줄 단위 구분 : split("\n") 과 동일               # \ : 개행문자 무시(끝이 아니라는 표시)
    lines = """\
    Java Programming
    Python Programming
    HTML Coding
    """
    print("SPLIT:", lines.split())
    print("SPLIT:", lines.split("\n"))

    print("SPLITLINES:", lines.splitlines(True))    # 개행문자 유지
    print("SPLITLINES:", lines.splitlines(False))   # 개행문자를 유지하지 않는다


def check_methods():
    """
    문자열 데이터(str)의 형태를 판별 -> True or False 형태로 출력
    """
    print("1234".isdigit())                         # 1234라는 문자열이 숫자 형태인가?
    print("abcd".isalpha())                         # 아니면 알파벳 형태인가?
    print("Python3".isalnum())                      # 아니면 숫자 + 알파벳 형태인가?
    print("Python 3".isalnum())                     # 위랑 같지만 공백 있없 차이 -> 공백이 있기때문에 false출력
    print(" \r\n\t".isspace())                      # 공백문자 형태인가? -> 스페이스, 개행문자, 탭 등 (3개는 공백문자 o)
    print("".isspace())

    print("PYTHON".isupper())
    print("python".islower())
    print("Python Programming".istitle())


def string_format():
    """
    문자열 포맷팅 연습
    """
    # c 스타일 문자열 포맷
    # %s, %c, %d, %f, %d, %o, %%
    fmt = "%d개의 %s 중에서 %d개를 먹었다."
    print(fmt % (10, "사과", 3))

    print("현재 이자율은 %f%% 입니다." % 3.4)
    print("현재 이자율은 %.2f%% 입니다." %3.4)

    # named formatting -> 이 경우 순서는 상관 없다. 이름만 맞으면 ok
    fmt = "%(total)d개의 %(fruit)s 중에서 %(eat)d개를 먹었다."
    print(fmt %{"total":10, "fruit": "사과", "eat": 3})
    print(fmt % {"fruit": "사과", "eat": 3, "total":10})

    # format 메서드
    fmt = "{}개의 {} 중에서 {}개를 먹었다."
    print(fmt.format(10, "사과", 3))
    print("{0}개의 {1} 중에서 {2}개를 먹었다.".format(10, "사과", 3))

    # placeholder의 named parameter를 이용
    fmt = "{total}개의 {fruit} 중에서 {eat}개를 먹었다."
    print(fmt.format(eat=3, total=10, fruit="사과"))

    # dict 작성된 데이터가 있을 경우 : format_map      -> 기존 fmt데이터에 이름 맞춰서 출력됨
    data = {"total": 10, "eat": 3, "fruit": "사과"}
    print(fmt.format_map(data))

    # f-string
    # 포맷팅 문자열 앞에 f를 붙여주면 f-string이 되는겨
    # {} 내부에 데이터, 변수명, 표현식 -> 해당 결과 바인딩 시켜서 최종 출력물 생성
    total, fruit, eat = 10, "사과", 3
    print(f"{total}개의 {fruit} 중에서 {eat}개를 먹었다")

    # placeholder 내부에 연산식 활용 가능
    total, fruit, eat = 10, "apple", 3
    print(f"{total}개의 {fruit.upper()} 중에서 {eat}개를 먹어서 {total - eat}개가 남았다")

if __name__ == "__main__":
    # define_str()
    # string_oper()
    # transform_methods()
    # search_methods()
    # modify_replace_method()
    # align_methods()
    # split_join_method()
    # check_methods()
    string_format()