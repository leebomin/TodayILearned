# direction : 구구단을 출력합니다.

# TODO 0 step

def test_mutiply():
    assert multiply(2, 1) == '2*1=2' #fail
    assert multiply(2, 2) == '2*2=4' #fail
    assert multiply(2, 3) == '2*3=6' #fail

# E       NameError: name 'multiply' is not defined

# TODO 1st step

def multiply():
    pass

def test_mutiply():
    assert multiply(2, 1) == '2*1=2' #fail
    assert multiply(2, 2) == '2*2=4' #fail
    assert multiply(2, 3) == '2*3=6' #fail

# E       TypeError: multiply() takes 0 positional arguments but 2 were given

# TODO 2nd step

# def multiply(x, y):
#     return f'{x}*{y}={x*y}'
#
# def test_mutiply():
#     assert multiply(2, 1) == '2*1=2' #pass
#     assert multiply(2, 2) == '2*2=4' #pass
#     assert multiply(2, 3) == '2*3=6' #pass

# TODO 3rd step

# def multiply(x, y):
#     return f'{x}*{y}={x*y}'
#
# def test_mutiply():
#     assert multiply_table[0] == '2*1=2' #fail
#     assert multiply_table[1] == '2*2=4' #fail
#     assert multiply_table[2] == '2*3=6' #fail

# E       NameError: name 'multiply_table' is not defined

# TODO 4th step

# def multiply(x, y):
#     return f'{x}*{y}={x*y}'
#
# def multiply_table():
#     pass
#
# def test_mutiply():
#     assert multiply_table[0] == '2*1=2' #fail
#     assert multiply_table[1] == '2*2=4' #fail
#     assert multiply_table[2] == '2*3=6' #fail

# E       TypeError: 'function' object is not subscriptable

# TODO 5th step

# def multiply(x, y):
#     return f'{x}*{y}={x*y}'
#
# def multiply_table():
#     return ['2*1=2']
#
# def test_mutiply():
#     assert multiply_table()[0] == '2*1=2' #pass
#     assert multiply_table()[1] == '2*2=4' #fail
#     assert multiply_table()[2] == '2*3=6' #fail

# E       TypeError: 'function' object is not subscriptable


# TODO 6th step

# def multiply(x, y):
#     return f'{x}*{y}={x*y}'
#
# def multiply_table():
#     table = []
#     return table.append(multiply(2,1))
#
# def test_mutiply():
#     assert multiply_table()[0] == '2*1=2' #fail
#     assert multiply_table()[1] == '2*2=4' #fail
#     assert multiply_table()[2] == '2*3=6' #fail


# TODO 7th step
def multiply(x, y):
    return f'{x}*{y}={x*y}'

def multiply_table():
    table = []
    for i in range(2,9+1):
        for j in range(1, 9+1) :
            table.append(multiply(i, j))
        return table

def test_mutiply():
    assert multiply_table()[0] == '2*1=2' #pass
    assert multiply_table()[1] == '2*2=4' #pass
    assert multiply_table()[2] == '2*3=6' #pass




# f string

# def gugu(n):
#     gugu_text = ''
#     for i in range(1, 10) :
#         gugu_text += f'{n}*{i}={n*i} '
#     return gugu_text.strip()
#
# def test_gugu():
#     assert gugu(2) == '2*1=2 2*2=4 2*3=6 2*4=8 2*5=10 2*6=12 2*7=14 2*8=16 2*9=18' #pass
#     assert gugu(3) == '3*1=3 3*2=6 3*3=9 3*4=12 3*5=15 3*6=18 3*7=21 3*8=24 3*9=27' #pass
#     assert gugu(4) == '4*1=4 4*2=8 4*3=12 4*4=16 4*5=20 4*6=24 4*7=28 4*8=32 4*9=36' #pass