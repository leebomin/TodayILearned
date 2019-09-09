def get_second_largest(n):
    if len(set(n)) == 1:
        return 'equality'
    else:
        n.remove(max(n))
        return max(n)


def test_get_second_largest():
    assert get_second_largest([6, 5, 2, 1, 100, 3, 1, 59]) == 59
    assert get_second_largest([5, 5, 5, 5, 5]) == 'equality'
