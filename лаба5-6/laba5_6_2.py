import os
import time
from laba5_6_3_reader import garr,xarr,yarr

def errof(str1,x,y):
 with open('myErrors.log', 'a') as f:
    f.write(gname)
    f.write(" x/(y-2)")
    f.write(' {0},{1} '.format(x,y))
    f.write(str1+"\n")
 

def rezerrof(str1,x,y):
 with open('myErrors.rez', 'a') as f:
     f.write('{:} {:} {:} \n'.format(str1,x,y))

def calc():
 with open('Calc.ini', 'a') as f:

    mem= str(Nx*24+Ny*24+Nx+Ny+3)
    f.write(mem+'\n')
    for i in range(Ny):
        f.write ( '{:< 24}'.format(yarr[i]))
        if i< Ny-1:
            f.write(",")
        else:
            f.write('\n')
    for i in range(Nx):
        f.write ( '{:< 24}'.format(xarr[i]))
        if i< Nx-1:
            f.write(",")
        else:
            f.write('\n')
 
def logf():
 with open('myProgram.log', 'a') as f:
 
    f.write("Название программы: laba5.2 "+"\n") 
    f.write("Вариант №5 "+"\n") 
    f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n")
    f.write("x/(y-2)"+"\n")
    f.write(gname+"\n")
    f.write("*"*20+"\n" )
    

def datarez(): 
 with open(rezname,'w' ) as f:
   
    for i in range(Nx):
        for j in range(Ny):
            f.write( garr[i][j])
            if j< Ny-1:
                f.write(",")
        f.write('\n')
 

def data():
 with open(gname,'w' ) as f:
 
    f.write(' {0},{1} \n'.format(Nx,Ny))
    f.write ( ' {:<24}'.format('x\y'))
    for i in range(Ny):
        y= y0+i*hy
        f.write ( '{:< 24}'.format(y))
        if i< Ny-1:
            f.write(",")
    for i in range(Nx):
        f.write("\n")
        garr.append([])
        x=x0+hx*i
        xarr.append(x)
        f.write( '{:< 24},'.format(x))
        for j in range(Ny):
            y=y0+j*hy
            yarr.append(y)
            func= g(x,y)
            garr[i].append(func)
            f.write( func)
            if j< Ny-1:
                f.write(",")
     
          
 

def g(x,y):
 try:
     rez='{:< 24}'.format(x/(y-2))
 except OverflowError:
     rez=' {:<23}'.format("null")
     errof("Over flow Error",x,y)
     rezerrof("Over flow Error",x,y)
 except ZeroDivisionError:
     rez=' {:<23}'.format("null")
     errof("Zero Division Error",x,y)
     rezerrof("Zero Division Error",x,y)  
 return rez



with open('read.txt') as fr:


    for line in fr :
        i= 1
        gname = 'G{:}.dat'.format(i)
        while(os.path.exists(gname)):
            i+=1
            gname= 'G{:}.dat'.format(i)
        i= 1
        rezname = 'G{:}.rez'.format(i)
        while(os.path.exists(rezname)):
            i+=1
            rezname= 'G{:}.rez'.format(i)
        str1=list(line.split(";"))
        x0=float (str1[0][3:])
        y0=float ( str1[1][3:])
        Nx=int (str1[2][3:])
        Ny=int (str1[3][3:])
        hx=float (str1[4][3:])
        hy=float (str1[5][3:])
        data()
        logf()
        datarez()
        calc()
