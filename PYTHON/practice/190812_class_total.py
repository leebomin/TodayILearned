# 과제
#
class_scores = [
    {
        '국어': 80,
        '영어': 100,
        '수학': 50
    },
    {
        '국어': 90,
        '영어': 70,
        '수학': 40
    }
]


# TODO 0st step

def test_class_total() :
    assert class_total([{'국어': 80, '영어': 100, '수학': 50}], '국어') == 80


# TODO 1st step

def class_total():
    pass

def test_class_total() :
    assert class_total([{'국어': 80, '영어': 100, '수학': 50}], '국어') == 80 #fail


# TODO 2nd step

def class_total(set, subject):
    return set, subject

def test_class_total() :
    assert class_total([{'국어': 80, '영어': 100, '수학': 50}], '국어') == 80 #fail


# TODO 3rd step

def class_total(set, subject):
    return set[0][subject]

def test_class_total() :
    assert class_total([{'국어': 80, '영어': 100, '수학': 50}], '국어') == 80 #pass
    assert class_total(class_scores, '국어') == 80 + 90 #fail


# TODO 4th step

def class_total(set, subject):
    total = 0
    for person in set:
        total += person[subject]
    return total

def test_class_total() :
    assert class_total([{'국어': 80, '영어': 100, '수학': 50}], '국어') == 80 #pass
    assert class_total(class_scores, '국어') == 80 + 90 #pass