import prologue #프롤로그
import movement #이동
import time #딜레이
import saveload #저장

lv = 1
att = 5
arm = 5
plc = 1

def starting () :
    print ('\n * 어디서든 "0" 을 입력하면 메뉴로 이동합니다.\n')
    time.sleep(1)
    print ('[현재 상태]\n')
    time.sleep(0.5)
    print ('레벨:',lv,'/ 공격력:',att,'/ 방어력:',arm,'/ 위치:',plc)
    time.sleep(1)
    movement.moveAble(plc)


if saveload.userdata != '':
    saved = input ('지난 게임을 불러오시겠습니까? 1.예 2.아니오\n')
    if saved != '1':
        x = input('프롤로그를 보시겠습니까? 1.본다 2.안 본다\n')
        prologue.firstgame(x)
        starting ()
    else :
        lv = int(saveload.userdata[0])
        att = int(saveload.userdata[1])
        arm = int(saveload.userdata[2])
        plc = int(saveload.userdata[3])
        starting ()
