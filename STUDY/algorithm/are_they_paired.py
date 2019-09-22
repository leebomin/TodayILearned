def check_parentheses_pairs(ps):
    for_count = []
    open_ps = '({['
    close_ps = ')}]'

    for p in list(ps):
        if p in open_ps:
            print(p in open_ps)
            for_count.append(p)
        else:
            if len(for_count) == 0:
                return False
            else:
                last_open_p = for_count.pop()
                if last_open_p != open_ps[close_ps.index(p)]:
                    return False

    return len(for_count) == 0


def test_check_parentheses_pairs():
    assert check_parentheses_pairs('()') == True
    assert check_parentheses_pairs('{}') == True
    assert check_parentheses_pairs('(({})[()])') == True
    assert check_parentheses_pairs('{({}[()])}') == True
    assert check_parentheses_pairs('(') == False
    assert check_parentheses_pairs(')') == False
    assert check_parentheses_pairs('()())') == False
    assert check_parentheses_pairs('{') == False
    assert check_parentheses_pairs('{}}') == False
