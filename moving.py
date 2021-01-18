def maphere (a,b,c,d) :
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
            ableMove = 1
            break
        else :
            print ('잘못된 방향입니다.')
            direction = input('어디로 이동합니까?'+addText)


maphere ('0','1','0','0')
maphere ('1','1','0','0')
maphere ('1','1','1','0')
