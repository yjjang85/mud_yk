import random
initMob = 5

def moveAble (a,b,c,d,e) :
    aT = bT = cT = dT =''
    ableDir = []
    n = 0;
    ableMove = 0

    if a == '1' :
        aT = ' 1.앞으로 '
        ableDir.append('1')
    if b == '1' :
        bT = ' 2.좌로 '
        ableDir.append('2')
    if c =='1' :
        cT = ' 3.우로 '
        ableDir.append('3')
    if d == '1' :
        dT = ' 0.뒤로 '
        ableDir.append('0')

    addText = aT + bT + cT + dT    
    direction = input('어디로 이동합니까?'+addText)
    while ableMove == 0 :
        if direction in ableDir :
            print('이동합니다.')
            mobCheck(e)
            ableMove = 1
            break
        else :
            print ('잘못된 방향입니다.')
            direction = input('어디로 이동합니까?'+addText)


def mobCheck (x) :
    print ('적이 있는지 확인합니다. 적 출현확률:', x, '%')
    monster = random.randint (0,100)
    if monster <= x:
        print ('적이 나타났습니다.')
        print ('적 출현 확률이 초기화됩니다.')
        initMob = 5
    else :
        print ('적이 없습니다.')
        print ('적 출현 확률이 증가합니다.')
        initMob = x + 5
