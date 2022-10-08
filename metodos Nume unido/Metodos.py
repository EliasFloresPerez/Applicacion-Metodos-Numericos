from ast import Lambda
from asyncio.proactor_events import _ProactorSocketTransport
import math
import matplotlib.pyplot as plt
import numpy as np
from sympy import *

def Formula(formula, x):
    
    y = eval(formula)

    return y

def FormulaDoble(formula,x,y):
    z = eval(formula)
    return z


def Graficar(titulo,formula,a=-100, b= 100,cantidad = 100):

    x = np.linspace(a,b,cantidad)
    
    y =  [Formula(formula,i)for i in x]

    plt.plot(x,y,color = 'g')

    
    #Decoracion
    plt.title(titulo)
    #plt.legend(formula)
    plt.grid()
    plt.xlabel('Eje de las x',color = 'b')
    plt.ylabel('Eje de las y',color = 'b')
    plt.show()

def Metodo_Grafico(formula,a=-100, b= 100,cantidad = 100):
    x = np.linspace(a,b,cantidad)
    y =  [Formula(formula,i)for i in x]

    return x,y

def metodo_biseccion(f,a,b,e):
    
    x_x1,x_re,y_re = [],[],[]

    while(b-a >= e):
        r = (a+b)/2

        try: 
            x_x1.append(abs(r - x_re[-1])) 
        except : 
            x_x1.append(abs(r - a))

        x_re.append(r)
        y_re.append(abs(Formula(f,r)))
        
        

        if abs(Formula(f,r))<= e:
            return x_x1,x_re,y_re
        else:
            if Formula(f,a) *  Formula(f,r)>0:
                a = r
            else:
                b = r


    return x_x1,x_re,y_re

def Metodo_Newton(f,X0,e):
    x =  Symbol('x')
    g =  diff(eval(f),x)
    
    tabla = []
    tramo = abs(2*e)
    xi = X0
    
    while (tramo>=e):

        xnuevo = xi - Formula(f,xi)/Formula(str(g),xi)
        tramo  = abs(xnuevo-xi)
        tabla.append([xi,Formula(f,xi),tramo])
        xi = xnuevo
        

    return tabla

def Dibujar_Lineas(tabla):

    #Separar tabla
    x = []
    y = []

    for i in reversed(tabla):
        x.append(i[0])
        y.append(i[1])
    
    
    new_x = []
    for i in x:
        new_x.append(i)
        new_x.append(i)

    new_y = []
    for i in y:
        new_y.append(i)
        new_y.append(0)

    print(new_x,new_y)
    plt.plot(new_x,new_y,color = 'red',marker="o")

def Graficar_Euler(titulo,formula,x,y):

    
    plt.plot(x,y,color = 'g')

    
    #Decoracion
    plt.title(titulo)
    #plt.legend(formula)
    plt.grid()
    plt.xlabel('Eje de las x',color = 'b')
    plt.ylabel('Eje de las y',color = 'b')
    plt.show()

def Metodo_Euler(T,X0,F,n):
        
    t=np.linspace(T[0],T[1],n+1)

    h=float(T[1]-T[0])/n

    X1=np.array(X0)
    X2=np.array([X1])
    
    
    for i in range(n):

        X1=X1+h*np.array(FormulaDoble(F,t[i],X1))
        X2=np.append(X2,[X1],axis=0)

    return t,X2

def Metodo_Taylor(form,x0,grado):

    x  = Symbol('x') 
    n  = grado + 1  
    k = 0 
    polinomio = 0
    
    Lista = []
    while (k < n):
        Lista.append([k])
        
        
        derivada   = diff(eval(form),x,k)
        Lista[k].append(derivada)
        derivadax0 = derivada.subs(x,x0)
        Lista[k].append(round(derivadax0,4))
        divisor   = np.math.factorial(k)
        terminok  = (derivadax0/divisor)*(x-x0)**k

        Lista[k].append(terminok)
        polinomio = polinomio + terminok
        
        k = k + 1

    
    return polinomio,Lista

def graficar_Taylor(Form,Form_Aprox,x0):
    Form_Aprox =  str(Form_Aprox)
    x = np.linspace(-10,10,100)
    

    y =  [Formula(Form,i)for i in x]
    yk =  [Formula(Form_Aprox,i)for i in x]

    plt.plot(x,y,color = 'y',label =Form,linewidth=1.5)
    plt.plot(x,yk,color = 'r',label ='Form aprox',linewidth=1)
    plt.plot(x0,Formula(Form_Aprox,x0) ,marker='o',color='g', label ='x0')
    
 
    print("Formula aprox : ",Form_Aprox)

    plt.xlim(min(x) , max(x) )
    plt.ylim(min(yk) , max(yk) )

    #Decoracion
    plt.title("Metodo de taylor\n Formula: {0}".format(Form_Aprox))
    
    #plt.legend(formula)
    plt.grid()
    plt.xlabel('Eje de las x',color = 'b')
    plt.ylabel('Eje de las y',color = 'b')
    plt.legend(loc='upper left')
    plt.show()

def Metodo_Trapecio(form,a,b,pasos):

    muestras = pasos + 1
    Xi = np.linspace(a,b,muestras)
    fi = Formula(form,Xi)

    #Ya son metodos de integracion
    h = (b-a)/pasos
    xi = a
    suma = Formula(form,xi)
    for i in range(0,pasos-1,1):
        xi = xi + h
        suma = suma + 2*Formula(form,xi)
    suma = suma + Formula(form,b)
    area = h*(suma/2)
    
    return area,Xi,fi

def Graficar_Trapecios(formula,a,b,tramos,Resultado):
    muestras = tramos + 1
    xi = np.linspace(a,b,muestras)
    fi = Formula(formula,xi)
    
    # Linea suave
    muestraslinea = tramos*10 + 1
    xk = np.linspace(a,b,muestraslinea)
    fk = Formula(formula,xk)

    # Graficando
    plt.plot(xk,fk, label ='f(x)')
    plt.plot(xi,fi, marker='o',color='r', label ='muestras')

    #plt.text(0.55, 0.55, 'Aproximacion : {}'.format(round(Resultado,3)), fontsize=20, color='green')
    

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Integral: Regla de Trapecios \nResultado : {}'.format(Resultado))
    plt.legend(loc='upper left')

    # Trapecios
    plt.fill_between(xi,0,fi, color='g')
    for i in range(0,muestras,1):
        plt.axvline(xi[i], color='w')

    plt.show()

def simpson_simplex(formula, a, b,pasos ):
    #Lo que retornara la funcion
    muestras = pasos + 1
    xi = np.linspace(a,b,muestras)
    fi = Formula(formula,xi)

    #calculamos h
    h = (b - a) / pasos
    
    suma = 0.0
    #hacemos un ciclo para ir sumando las areas
    for i in range(1, pasos):
        
        x = a + i * h
        
        if(i % 2 == 0):
            suma = suma + 2 * Formula(formula,x)
        
        else:
            suma = suma + 4 * Formula(formula,x)

    suma = suma + Formula(formula,a) + Formula(formula,b)
    rest = suma * (h / 3)
    
    return rest,xi,fi

def Graficar_Simpson(formula,a,b,pasos,resultado):
    muestras = pasos + 1
    xi = np.linspace(a,b,muestras)
    fi = Formula(formula,xi)
    
    # Linea suave
    muestraslinea = pasos*10 + 1
    xk = np.linspace(a,b,muestraslinea)
    fk = Formula(formula,xk)

    # Graficando
    plt.plot(xk,fk, label ='f(x)', color = 'b')
    

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Integral: Regla de Simpson \nResultado : {}'.format(resultado))
    plt.legend()

    
   
    #print(xk,fk)
    #print(len(xk),"Arreglo : ",arreglo )
    i = 0
    plt.fill_between(xk,0,fk, color='orange' ,alpha = 0.4) #, 
    
    for i in range(0,muestras,1):
        #print(i,xi[i])
        plt.axvline(xi[i], color='w')

        if i % 2 == 0:
            plt.fill_between(xk[i*10: (i+1) * 10 +1],0,fk[i*10:(i+1) * 10 + 1], color='orange')
           


    plt.show()


#Creditos a quien corresponda
def Metodo_runge_kutta(orden,Dy,t0,tn,n,y0):
    arreglo_x = []
    arreglo_y = []
    # Paso 1
    h=(tn-t0)/n
    tiwi = np.zeros(shape=(n+1,2),dtype=float)
    tiwi[0] = [t0,y0]
    ti = t0
    wi = y0
    # Paso 2
    for i in range(1,n+1,1):

        if orden==2:
            # Paso 3
            K1 = h * FormulaDoble(Dy,ti,wi)
            K2 = h * FormulaDoble(Dy,ti+h, wi + K1)
            # Paso 4
            wi = wi + (K1+K2)/2
            ti = ti + h
            tiwi[i] = [ti,wi]
        elif orden==3:
            # Paso 3
            K1 = h * FormulaDoble(Dy,ti,wi)
            K2 = h * FormulaDoble(Dy,ti+h/2, wi + K1/2)
            K3 = h * FormulaDoble(Dy,ti+h, wi + 2*K2 -K1)
            # Paso 4
            wi = wi + (1/6)*(K1+4*K2+K3)
            ti = ti + h

            tiwi[i] = [ti,wi]
        elif orden==4:
            # Paso 3
            K1 = h * FormulaDoble(Dy,ti,wi)
            K2 = h * FormulaDoble(Dy,ti+h/2, wi + K1/2)
            K3 = h * FormulaDoble(Dy,ti+h/2, wi + K2/2)
            K4 = h * FormulaDoble(Dy,ti+h, wi + K3)
            # Paso 4
            wi = wi + (1/6)*(K1+2*K2+2*K3 +K4)
            ti = ti + h

            tiwi[i] = [ti,wi]
    
    return tiwi



