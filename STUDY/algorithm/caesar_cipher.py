def make_caesar_cipher(word):
    password = ''
    z = ord('z')
    chars = list(word)
    pw_codes = [ord(char) + 3 for char in chars]

    for code in pw_codes:
        if int(code) <= int(z):
            password += chr(code)
            # password + chr(code)만 하고 왜 맞는데 답이 틀리다고 나오지 계속 고민함. +=와 +는 다릅니다.
        else:
            password += chr(int(code) - int(z))
    return password


def test_make_caesar_cipher():
    assert make_caesar_cipher('word') == 'zrug'