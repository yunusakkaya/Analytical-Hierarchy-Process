import numpy as np

n=int(input("kaç etken var?:"))
y=0
dt=0

tablo=np.array([[0]*n]*n,dtype=float)
tablo=tablo.reshape(n,n)
print("oluşturduğunuz tablo:\n",tablo)

for i in range(0,n):
    for j in range(0,n):
        if tablo[i,j]==0:
            if i==j:
                tablo[i,j]=1
            else:
                tablo[i,j]=float(input("değer:"))
                tablo[j,i]=float(1/tablo[i,j])
                if tablo[i,j]>9 or tablo[i,j]<0:
                    print("olmaz öyle şey")
                    tablo[i,j]=float(input("tekrar:"))
                    tablo[j,i]=float(1/tablo[i,j])
            
                
print("değer tablosu:\n",tablo)

a=tablo.sum(0)
print("toplam:",a)

tablo2=tablo/a
print("ağırlık tablosu:\n",tablo2)

tablo3=tablo2

w=tablo3.sum(1)
print(w)
k=w/n
print("ağırlık değerleri:\n",k)

ı=int(input("kaç seçenek var?:"))
gt=[0]*ı

for l in range (1,n+1):
        
    tablo10=np.array([[0]*ı]*ı, dtype=float)
    tablo10=tablo10.reshape(ı,ı)
    
    for i in range(0,ı):
        for j in range(0,ı):
            if tablo10[i,j]==0:
                if i==j:
                    tablo10[i,j]=1
                else:
                    tablo10[i,j]=float(input("değer:"))
                    tablo10[j,i]=float(1/tablo10[i,j])
                    if tablo10[i,j]>9 or tablo10[i,j]<0:
                        print("olmaaz")
                        tablo10[i,j]=float(input("tekrar:"))
                        tablo10[j,i]=float(1/tablo10[i,j])
                    
    print("oluşturduğunuz tablo:\n",tablo10)
                
    a=tablo10.sum(0)
    print("toplam tablosu:",a)
     
    tablo11=tablo10/a
    print("ağırlık tablosu:\n",tablo11)
     
    tablo12=tablo11.sum(1)
    print("ağırlık değerleri:\n",tablo12/(tablo12.size))
    ad=tablo12/(tablo12.size)
     
    for h in range (0,ı):
             
            A=float(ad[h])*float(k[l-1])
            gt[h]=gt[h]+A
        
             
     
print("uygunluk değerleri:", gt)
print("{}. seçenek uygundur".format(gt.index(max(gt))+1)) 