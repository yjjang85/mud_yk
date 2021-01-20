f = open('savedata.txt','r')
line = f.readline()
f.close()
userdata = line.strip('\n').split(',')
