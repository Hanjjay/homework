import math #math 모듈 임포트
def is_square(n):
    if n < 0:
        return False #입력받은 수가 음수일시 false값 리턴
        
    sqrt_Value = math.sqrt(n)  #입력값의 제곱근
    
    #제곱근에 소수점이있는지 검사
    if 0 != (sqrt_Value - int(sqrt_Value)):
        return False
    else:
        return True