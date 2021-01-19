import gamemap
import time

def moveAble (x) :

    

    a= (gamemap.mapHere[x][0])
    b= (gamemap.mapHere[x][1])
    c= (gamemap.mapHere[x][2])
    d= (gamemap.mapHere[x][3])
    f= (gamemap.mapHere[x][5])
    print ()
    print (f)
    print ()
    time.sleep(1)
    aT = bT = cT = dT =''
    ableDir = []
    ableMove = 0

    if a > 0 :
        aT = ' 1.앞으로 '
        ableDir.append('1')
    if b > 0 :
        bT = ' 2.좌로 '
        ableDir.append('2')
    if c > 0 :
        cT = ' 3.우로 '
        ableDir.append('3')
    if d > 0 :
        dT = ' 0.뒤로 '
        ableDir.append('0')

    addText = aT + bT + cT + dT
    if (x <= 2) :
        direction = input('어디로 이동합니까?'+addText)
        while ableMove == 0 :
            if direction in ableDir :
                if (direction == '1'):
                    goto = a
                if (direction == '2'):
                    goto = b
                if (direction == '3'):
                    goto = c
                if (direction == '0'):
                    goto = d
                nextPlace = gamemap.mapHere[goto][4]
                print ('당신은',nextPlace,'로 이동합니다.')
                moveAble(goto)
                ableMove = 1
                break
            else :
                print ('잘못된 방향입니다.')
                direction = input('어디로 이동합니까?'+addText)
    else :
        print('더이상 갈 곳이 없습니다.')
    


