#concatenación 

#a = "renzo"

#b = "blas"

#juntar = a + b 

#print(juntar)

#type(juntar)

#operación con variable y texto

#x = 14

#y = 12

#suma= x + y

#print(x + y)

#print(x, "hola", suma, "-", y)

#print(x+ "hola"+ suma+ "-"+ y)

#línea 25 va a saltar error po rque antes de imprimir números hay que 
#transformar variables

#print(str(x), "hola", str(suma), "-", str(y))
#o tambien 

#z = "hola"

#r = "-"

#print(str(x), z, str(suma), r, str(y))

a = 23

print("a = 23  -->", a)

a = a + 1

print("a=a+1 -->", a)

a+=1

print("a+=1 -->", a)

a*=2

print("a*=2 -->", a)

a/=2

print("a/=2 -->", a)

for x in [1,7,9]:
    if x == 1 :
        print("echo")
    elif x == 7:
        print("buen camino")
    else:
        print("no hay valor en 9")  

#otro ejemplo 
from math import *
T = "formula para hallar area del rectangulo"
print(T)
a=input("ingrese el numero: ")
b=input("ingrese el numero: ")

_1=input("presione 1 y luego enter : ")
_y=[1,9]
if int(_1)==_y[0]:
    s=int(a)*int(b)
    print(s)
else :
    print("error de syntax")




