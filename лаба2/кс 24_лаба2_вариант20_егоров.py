a=[]
h =10# шаг изменения темпиратуры
b=[64.44,65.4, 66.74,68.36,70.22,72.24,74.32,76.51,78.74,80.86]# точки из опыта
n=5# количество уранений
m=10# количество опытов
def perevod(z):
    return round(z,2)

def create(z):
    for i in range(z):
        a.append([])



def schet(t):
    a[0].append(  64.496+0.0659625*t +0.224306*10**(-2)*t**2-0.105729*10**(-4)*t**3)
    a[1].append(64.496+0.066027*t +0.2241304*10**(-2)*t**2-0.10560396*10**(-4)*t**3)
    a[2].append(64.4724+8.1564207*10**(-2)*t+2.3034122*10**(-4)*pow(t,2.8) -2.6492852*10**(-5)*pow(t,3.3)+2.4826037*10**(-8)*pow(t,4.5))
    a[3].append(64.18+0.1348*t+5.31*10**(-4)*t**2)
    a[4].append(63.608+0.133*t+7.22*10**(-4)*t**2)

create(n)
for i in range(m):
    schet(0+i*(h))

for i in range(n):
    print (list(map(perevod,a[i])),end='\n\n')

for i in range(n):
    r=0
    for j in range(m):
        r=+ (a[i][j]-b[j])**2
    print(perevod(r),end='\n\n')
