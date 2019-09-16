def get_second_largest(ranks):
    ranks = list(set(ranks))
    if len(ranks) == 1:
        return 'equality'
    else:
        max_rank = max(ranks)
        ranks.remove(max_rank)
        return max(ranks)


def test_get_second_largest():
    assert get_second_largest([6, 5, 2, 1, 100, 3, 1, 59]) == 59
    assert get_second_largest([5, 5, 5, 5, 5]) == 'equality'


'''
두 번째 큰 값 찾기
* 되게 잘 하셨어요. 괜찮은 방법인 것 같아요. 근데 좀 더 표준적인 방법은 제가 만든 방법이거든요. 제 코드도 확인해주세요.
'''


# 성환님 코드

from math import inf
# inf : 무한대

def second_largest(arr):
    # 두 번쨰 큰 값이 없을 때 반환하는 문구 초기화.
    NO_ANSWER_MESSAGE = 'equality'

    # 두번째로 큰 값. -무한대로 초기값 셋팅. 아주아주 작은 값에서 하나씩 업데이트 해서 큰 값을 찾는 방식.
    biggest = second = -inf
    for n in arr:
        if n > biggest:
            second = biggest
            biggest = n
        elif second < n < biggest:
            second = n

    # 기본적인 아이디어는 biggest 값이 나오면 biggest에 값을 넣고 second에 원래 biggest 였던 값을 할당해주는 식으로 가는건데.
    # 이게 대체 어떻게 가능한가 봤더니 위 for문 안에 들어있는 if 문 안에는 n == ?? 이런 조건식이 없다.
    # 즉. biggest보다 크거나 biggest보다 작거나.
    # 둘 중 하나면 위에 for문에서 분기를 타지만 n값이 계속 biggest 값과 같다면 분기를 타지 않는다.
    # n이 계속 같은 값이 나올 경우에는 biggest 값만 하나로 계속 나와서 second 값이 -무한대로 초기화 된 상태에서 움직이지 않는 것.

    if second == -inf:
        return NO_ANSWER_MESSAGE
    else:
        return second
