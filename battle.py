import settings as st
import time
#temp에서 내 스탯 불러오기
import random

damage = 0

def dmg (a,b,c,d) : #공레벨, 방레벨, 공공격, 방방어
    l = random.randint (0,100)
    luck = l * (a-b)
    global damage
    if (a>b) :
        if luck > 80 :
            print (st.me,'는 회심의 일격을 가했다!\n')
            damage = ((c-d)*2)*10*0.8
            
        else :
            print (st.me,'가 검을 휘둘렀다.\n')
            damage = (c-d)*10*0.8
    else :
        if luck > 80 :
            print (st.me,'는 회심의 일격을 가했다!\n')
            damage = ((c-d)*2)*10*0.8
            
        else :
            print (st.me,'가 검을 휘둘렀다.\n')
            damage = (c-d)*10*0.8
            
def fight (x) :
    name = st.enemy[x][0]
    intro = st.enemy[x][1]
    attack = st.enemy[x][2]
    monslv = st.enemy[x][3]
    monsatt = st.enemy[x][4]
    monsarm = st.enemy[x][5]
    monshp = st.enemy[x][6]
    monsexp = st.enemy[x][7]
    print ('\n'+intro+'\n')
    time.sleep(1)
    print ('전투다!')
    time.sleep(1)
    while monshp > 0 :
        action = input ('1.공격한다. 2.도망친다.\n\n')
        if action == '1':
            time.sleep(0.5)
            dmg(2,1,5,3)
            monshp = monshp - damage
            if monshp < 0 :
                monshp = 0
            print (name,'은',damage,'의 데미지를 입었다. [남은 체력:',monshp,']\n')
            time.sleep(0.5)            
            if monshp > 0 :
                print (name,'이 반격한다.\n')
                time.sleep(0.5)                
                print (st.me,'은','의 데미지를 입었다.\n')
                time.sleep(0.5)
            else :
                print (name,'을 쓰러뜨렸다.\n')
                time.sleep(0.5)
                print ('경험치가',monsexp,'올랐다.\n')
                break
            
        elif action == '2':
            print (st.me,'는 도망쳤다.\n')
            time.sleep(0.5)
            break
fight(1)
