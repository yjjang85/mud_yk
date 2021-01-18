def mobCheck (x) :
    print ('적이 있는지 확인합니다. 적 출현확률:', x, '%')
    monster = random.randint (0,100)
    if monster <= x:
        print ('적이 나타났습니다.')
        print ('적 출현 확률이 초기화됩니다.')
        #적 출현 확률 초기화
    else :
        print ('적이 없습니다.')
        print ('적 출현 확률이 증가합니다.')
        #적 출현 확률 +5
