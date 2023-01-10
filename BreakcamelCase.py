def solution(s):
    s_up = s.upper() #받은 문장 모두 대문자로
    result =''

    for i in range(len(s)): #문장수만큼 반복

        if s_up[i] == s[i]: #원래 문장이 대문장일시 공백추가
            result +=' '
        result += s[i]
    return result