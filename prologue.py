import time #딜레이
import settings as st #세팅

   
def firstgame (x) :
    if x == '1':
        print ('\n\n\n오로라력 2021년, 어느날.\n')
        time.sleep (1)
        print (st.yj+'은 옐로나이프 성으로부터 강한 악의 기운을 느꼈다.\n')
        time.sleep (2)
        print (st.yj+': 결국, 이렇게 되는 것인가?.\n')
        time.sleep (2)
        print ('그는 서둘러 '+st.me+'를 부른다.\n')
        time.sleep (2)
        print (st.me+': 부르셨습니까?\n')
        time.sleep (2)
        print (st.yj+': 오오, 자네 왔는가.\n')
        time.sleep (2)
        print (st.yj+': 예언이 실현되려는 모양이야.\n')
        time.sleep (2)
        print (st.yj+': 마왕의 출현에 대한 예언이...\n')
        time.sleep (2)
        print (st.me+': 그렇다면?\n')
        time.sleep (1.5)
        print (st.yj+': 이 검과 방패를 들고 떠나게. 가서 꼭 마왕을 물리치게나.\n')
        time.sleep (2)
        print ('\n * '+st.me+'는 [목검]을 장비했다.(공격력 +3)\n')
        time.sleep (2)
        print ('\n * '+st.me+'는 [목방패]를 장비했다.(방어력 +3)\n\n')
        time.sleep (2)
        print (st.yj+': 옐로나이프 성으로 떠나게. 가서 꼭 세상을 구해주게나.\n')
        time.sleep (2)
        print (st.me+': 네, 꼭 세상을 구해보이겠습니다.\n')
        time.sleep (2)
        print (st.me+'는 옐로나이프 성으로 향한다.\n')
        time.sleep (2)
    elif x == '2' :
        print ('\n * 프롤로그를 스킵하셨습니다.\n')
        time.sleep(1)
    else :
        print ('잘못 입력되었습니다.')
        x = input('프롤로그를 보시겠습니까? 1.본다 2.안 본다\n')
        firstgame(x)
