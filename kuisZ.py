import math
import numpy as np
import matplotlib.pyplot as plt
g = -9.8
xo = 490
dt = 0.1 
vo = 0
N=5-1

KWaktu=[]
KDataAnalitik=[]
KDataNumerik=[]
#========== WAKTU TOTAL ====================
T = math.sqrt(-2*xo/g)
#========== 
n=(T/dt)+1 #ini nih kuncinya KACAWWW
print('banyak titik = ',n)



t=[0.1,0.2,0.3,0.4] #ini tuh kalau misalkan detiknya cuma segini kalau misal otomatis tergantung banyak titik si waktunya ngikutin delta

z=0

#print(len(t))
#=========== ANALITIK ERA ====================
print('ANALITIK')
plt.figure()
i=0
while(i<=n):
    dti=dt*(i+1)
    KWaktu.append(dti)
    if(i==0):
        x = (0.5*(g*((dti)**2)))+xo
    else:
     
        x = (0.5*(g*((dti)**2)))+xo
    KDataAnalitik.append(x)
    print(round(x,2))
    i=i+1

#=========== NUMERIK ERA =====================
print('NUMERIK')
ib = 0
while (ib<=n):
    if (ib==0):
        v = g*(dt)+vo
    else:
        v = g*((ib+1)*dt)+v
    x = v*dt+xo
    KDataNumerik.append(x)
    ib = ib+1
    print(round(x,2))

plt.plot(KWaktu,KDataAnalitik,'r')
plt.plot(KWaktu,KDataNumerik,'b')
plt.show()