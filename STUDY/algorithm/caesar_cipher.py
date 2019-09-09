def make_caesar_cipher(word):
    password = ''
    z = ord('z')
    chars = list(word)
    pw_codes = [ord(char) + 3 for char in chars]

    for code in pw_codes:
        if int(code) <= int(z):
            password += chr(code)
        else:
            password += chr(int(code) - int(z))
    return password


def test_make_caesar_cipher():
    assert make_caesar_cipher('word') == 'zrug'