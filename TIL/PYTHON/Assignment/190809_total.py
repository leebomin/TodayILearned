scores = [80, 100, 70, 90, 40]


# 우리는 결과값을 알고 있다. 함수의 스펙, 기대되는 값을 이미 알고 있는 상태에서 코드로 변환하는 작업이다.

# 1. 테스트 케이스를 가장 먼저 작성한다. 뭐가 들어갔을 때 뭐가 나오는지 알고 있으니까. 테스트 케이스 작성부터 시작.
# 2. 테스트 함수를 작성.
# 3. 실제 작성해야하는 함수 작성.
# 4. 가장 간단한 레벨에서부터 테스트 케이스들을 해결해나간다.
# 에러 메세지를 보고 한단계 한단계씩!

# TODO) 0st stage

# def test_total():
#     assert total([20]) == 20 # pass
#     assert total([20, 30]) == 50 #fail
#     assert total([20, 40, 50]) == 110 #fail

# TODO) 1st stage
# def total():
#     pass
#
# def test_total():
#     assert total([20]) == 20 # pass
#     assert total([20, 30]) == 50 #fail
#     assert total([20, 40, 50]) == 110 #fail

# TODO) 2nd stage
# def total(test_scores):
#     return 20
#
# def test_total():
#     assert total([20]) == 20 # pass
#     assert total([20, 30]) == 50 #fail
#     assert total([20, 40, 50]) == 110 #fail

# TODO) 3rd stage
# def total(test_scores):
#     result = 20
#     return result
#
# def test_total():
#     assert total([20]) == 20 # pass
#     assert total([20, 30]) == 50 #fail
#     assert total([20, 40, 50]) == 110 #fail

# TODO) 4rd stage
def total(test_scores):
    result = 0
    for item in test_scores:
        result += item
    return result

def test_total():
    assert total([20]) == 20 # pass
    assert total([20, 30]) == 50 #pass
    assert total([20, 40, 50]) == 110 #pass
    assert total([20, 50, 40, 80, 100, 30]) == 20 + 50 + 40 + 80 + 100 + 30
    assert total([20, 50, 40, 80, 100, 30]) == total([20, 50, 40, 80, 100]) +30
    assert total(scores) == sum(scores) #pass