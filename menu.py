import settings as st
import gamemap
import movement
import time
def action (a):

    print ('\n[메뉴]')
    time.sleep(0.5)
    x = input ('\n1.이동 2.장비 3.상태 4.저장\n')
    
    if x == '1':
        movement.moveAble(a)

    if x == '2':
        print ('장비 현황')
        action(a)

    if x == '3':
        print ('현재 '+st.me+'는 01.에 위치해 있습니다.')
        action(a)

    if x == '4':
        print ('저장합니다.')
        f = open('savedata.txt','w')
        temp = '10,5,7'
        print (temp, file=f)
        f.close()
        action(a)
