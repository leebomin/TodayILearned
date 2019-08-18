## Fjll this file third

# 판다스 라이브러리를 가져온다
import pandas as pd

# scores 파일에서 class_total 함수를 불러온다
from scores import class_total


# main에서 사용할 함수를 정의한다
def main():
    # 데이터 셋
    class_scores = [
        {'Name': 'Jane', 'Korean': 100, 'English': 100, 'Math': 100},
        {'Name': 'Brown', 'Korean': 10, 'English': 20, 'Math': 30}
    ]

    # total이라는 이름을 데이터로 한 행을 추가한다
    total = {'Name': '<Total>'}

    # iteration을 돌면서 total이라는 딕셔너리 안에 'subject 이름' : 'subject 값의 총합' 으로 매칭되는 키와 값을 저장한다.
    for subject in ['Korean', 'English', 'Math']:
        total[subject] = class_total(class_scores, subject)

        # class_scores와 total을 결합하여 판다스 데이터프레임으로 결과를 표시한다
        table = pd.DataFrame(class_scores + [total],
                             columns=['Name', 'Korean', 'English', 'Math'])
        print(table)


main()
