import gamemap #지도 정의
import movement #이동 함수
import checkenemy #몹 탐색
import time #딜레이

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

print (color.BOLD + '오로라력 2021년, 어느날.' +color.END)
time.sleep (1)
print ('현자 장영진은 옐로나이프 성으로부터 강한 악의 기운을 느꼈다.')
time.sleep (2)
print ('장영진: 결국, 이렇게 되는 것인가?.')
time.sleep (2)
print ('그는 서둘러 용사 벨로가를 부른다.')
time.sleep (2)
print ('벨로가: 부르셨습니까?')
time.sleep (2)
print ('장영진: 오오, 자네 왔는가.')
time.sleep (1.4)
print ('장영진: 예연이 실현되려는 모양이야.')
time.sleep (1.4)
print ('장영진: 마왕의 출현에 대한 예언이...')
time.sleep (1.4)
print ('벨로가: 그렇다면?')
time.sleep (1)
print ('장영진: 이 검과 방패를 들고 떠나게. 가서 꼭 마왕을 물리치게나.')
time.sleep (1.4)
print ('용사 벨로가는 서현검을 장비했다.')
time.sleep (1.4)
print ('용사 벨로가는 서정방패를 장비했다.')
time.sleep (1.4)
print ('장영진: 옐로나이프 성으로 떠나게. 가서 꼭 세상을 구해주게나.')
time.sleep (1.4)

print ('용사 벨로가는 옐로나이프 성으로 향한다.')
time.sleep (1.4)


movement.moveAble(1)

