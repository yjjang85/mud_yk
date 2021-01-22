import random
import time
import battle

def mobCheck (x) :
    time.sleep(0.5)
    print ('적이 있는지 확인합니다.')
    monster = random.randint (0,100)
    if monster <= 50:
        if x < 7 :
            n = random.randint (1,3)
            battle.fight(n)
            time.sleep(1)
    else :
        print ('적이 없습니다.\n')
        time.sleep(1)
