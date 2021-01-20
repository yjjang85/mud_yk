import settings as st
import random

def fight (x) :
    if x < 10 :
        n= random.randint(1,3)
        name = st.enemy[n][0]
        print (name)
