def check_parentheses_pairs(parentheses):
    list_ps = list(parentheses)
    return True if list_ps.count('(') == list_ps.count(')') else False

def test_check_parentheses_pairs():
    assert check_parentheses_pairs('(())(') == False
    assert check_parentheses_pairs('((((') == False
    assert check_parentheses_pairs(')))(') == False
    assert check_parentheses_pairs('()()()') == True
    assert check_parentheses_pairs('((()))') == True
    assert check_parentheses_pairs('(())()') == True


'''
괄호식 검증하기
• 언제나 말씀드리는데요. 문제 풀기보다 더 중요한 게 문제 이해하기에요. 문제를 제대로 이해하지 못하면 필시 잘못된 코드를 내놓게 되어 있어요. 옳은 괄호는 여는 괄호와 닫는 괄호의 개수가 맞는 게 절대 다가 아니에요. 문제를 다시 이해해주세요. 이 문제는 좀 유명하고 중요하거든요? 본인을 위해서 꼭 다시 풀어보세요.
• 그리고 .count 메소드는 리스트뿐 아니라 str에도 있습니다. 왜 그런지 알고 싶으시면 좀더 공부해야 합니다. 그래서 굳이 리스트화 하지 않으셔도 돼요.
'''