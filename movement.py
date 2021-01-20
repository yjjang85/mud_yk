import gamemap
import time
import checkenemy
import menu

def moveAble (x) :

    a= (gamemap.mapHere[x][0])
    b= (gamemap.mapHere[x][1])
    c= (gamemap.mapHere[x][2])
    d= (gamemap.mapHere[x][3])
    e= (gamemap.mapHere[x][4])
    f= (gamemap.mapHere[x][5])
    print ('\n\n'+e)
    print ('\n'+f+'\n\n')
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
        dT = ' 4.뒤로 '
        ableDir.append('4')

    addText = aT + bT + cT + dT
    if (x <= 2) :
        direction = input('어디로 이동합니까?'+addText+'\n')
        while ableMove == 0 :
            if (direction == '0'):
                    menu.action(x)
            elif direction in ableDir :
                if (direction == '1'):
                    goto = a
                if (direction == '2'):
                    goto = b
                if (direction == '3'):
                    goto = c
                if (direction == '4'):
                    goto = d
                nextPlace = gamemap.mapHere[goto][4]
                print ('당신은',nextPlace,'로 이동합니다.\n')
                time.sleep(1)
                checkenemy.mobCheck(goto)
                moveAble(goto)
                ableMove = 1
                break
            else :
                print ('잘못된 방향입니다.')
                direction = input('어디로 이동합니까?'+addText)
    else :
        print('더이상 갈 곳이 없습니다.')
    


