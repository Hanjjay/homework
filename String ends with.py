def solution(string, ending):
    
    #비교할 문장 리스트화
    string_list = list(string)
    ending_list = list(ending) 
    
    op = string_list[len(string_list)-len(ending_list):] #string 리스트의 둘의 길이를 뺀수부터 입력

    #비교후 같을시 true 출력 아닐시 false출력
    if op == ending_list:
        return True
    else:
        return False