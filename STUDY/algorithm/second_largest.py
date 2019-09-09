def get_second_largest(ranks):
    if len(set(ranks)) == 1:
        return 'equality'
    else:
        max_rank = max(ranks)
        ranks.remove(max_rank)
        return max(ranks)


def test_get_second_largest():
    assert get_second_largest([6, 5, 2, 1, 100, 3, 1, 59]) == 59
    assert get_second_largest([5, 5, 5, 5, 5]) == 'equality'
