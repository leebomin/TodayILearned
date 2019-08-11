scores = [80, 100, 70, 90, 40]


# TODO) 0st stage

# def test_mean():
#     assert mean([30]) == 30 #fail

# Error
# NameError: name 'mean' is not defined


# TODO) 1st stage

# def mean():
#     pass
#
# def test_mean():
#     assert mean([30]) == 30 #fail

# Error
# TypeError: mean() takes 0 positional arguments but 1 was given


# TODO) 2nd stage

# def mean(l):
#     pass
#
# def test_mean():
#     assert mean([30]) == 30 #fail

# Error
# E      assert None == 30


# TODO) 3rd stage

# def mean(l):
#     return l
#
# def test_mean():
#     assert mean([30]) == 30 #fail

# Error
# E      assert [30] == 30


# TODO) 4th stage

# def mean(l):
#     return sum(l)
#
# def test_mean():
#     assert mean([30]) == 30 #pass
#     assert mean([30, 50]) == 40 #fail

# Error
# E       assert 80 == 40


# TODO) 5th stage

def mean(l):
    return sum(l)/len(l)

def test_mean():
    assert mean([30]) == 30 #pass
    assert mean([30, 50]) == 40 #pass
    assert mean(scores) == 76 #pass