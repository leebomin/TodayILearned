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
