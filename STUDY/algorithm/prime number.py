def is_prime_number(n):
    for factor in range(2, n):
        if n % factor == 0:
            return False

    return True


def test_is_prime_number():
    assert is_prime_number(2) == True
    assert is_prime_number(41) == True
    assert is_prime_number(5) == True
    assert is_prime_number(283) == True
    assert is_prime_number(449) == True
    assert is_prime_number(4) == False
    assert is_prime_number(6) == False
    assert is_prime_number(150) == False
    assert is_prime_number(9) == False
    assert is_prime_number(12) == False
