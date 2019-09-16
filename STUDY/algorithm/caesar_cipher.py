def make_caesar_cipher(word):
    cipher = ''
    UNICODE_SMALL_Z = ord('z')
    chars = list(word)
    pw_codes = [ord(char) + 3 for char in chars]

    for code in pw_codes:
        if int(code) <= int(UNICODE_SMALL_Z):
            cipher += chr(code)
            # cipher + chr(code)만 하고 왜 맞는데 답이 틀리다고 나오지 계속 고민함. +=와 +는 다릅니다.
        else:
            cipher += chr(int(code) % int(UNICODE_SMALL_Z))
    return cipher


def test_make_caesar_cipher():
    assert make_caesar_cipher('word') == 'zrug'



'''
카이사르 암호 만들기
• 변수명이 이상해요. 우리는 암호를 만드는 거지 비밀번호를 만드는 게 아니거든요. 둘은 코끼리랑 바다코끼리마냥 다른거에요.
• 3번째 줄은 진짜 커피 사드리고 싶을만큼 잘하신 것 같아요. 저런 값은 그대로 쓰지 말고 상수로 담으라고 말씀드렸죠. 다만 이름이 별로에요. 일단 상수는 대문자로 하구요.(이는 다른 많은 언어 마찬가지에요 또 z 자체로는 저게 무슨 뜻인지 전혀 알 수 없어요. 상수는 의미를 구체적으로 적어주시는 게 좋아요. 가독성을 위해서요. z가 뭔지 모르니까 12번째 줄에서 이미 정수인 수에 또 정수화를 하고 계시잖아요? 가령 UNICODE_SMALL_Z 정도만 되어도 쫌 더 가독성이 좋겠어요.
• 프로그래밍을 할 때는 나머지 연산을 할 일이 정말 많습니다. 아직 써본 경험이 많이 없으신 것 같다고 느꼈거든요. 원하시는 바를 코드로 제대로 구현했는데 이 문제에 대한 기대되는 코드는 아닙니다. 제 풀이에서는 나머지 연산을 사용해 풀었거든요? 확인해주세요
'''