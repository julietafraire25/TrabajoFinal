from random import randint

def quiniela ():
       quiniela=int(input("Quiere apostar un numero de 2,3 o 4 digitos? "))
       if quiniela ==2:
              apuesta = int(input("Ingrse un número de 2 cifras: "))
              print("El número ingresado es: ",apuesta)
       
       elif quiniela==3:
              apuesta = int(input("Ingrse un número de 3 cifras: "))
              print("El número ingresado es: ",apuesta)
       elif quiniela==4:
              apuesta = int(input("Ingrse un número de 4 cifras: "))
              print("El número ingresado es: ",apuesta)
       else:
              print("Error en número")
def cliente ():
       DNI=int(input("Ingrese su DNI: "))
       Fecha=input("Ingrese la fecha: ")
       Hora=input("Ingrese la hora: ")
       Nro_ticket=int(input("Ingrese el número de comprobante: "))
       cifra_apostada=float(input("Ingrese la cifra apostada: "))
       print ("\n---TICKET COMPROBANTE---")
       print("*Quiniela 'El pela'*")
       print("La fecha es: ",Fecha)
       print("La hora es: ",Hora)
       print("El número de comprobante es: ",Nro_ticket)
       print("Su DNI es: ",DNI)
       print("La apuesta es de: $ ",cifra_apostada)
       print ("-----------------------")
def quini_6 ():
       quini_6=int(input("Quiere realizar una apuesta de 6 números entre 00 y 45 ó al azar? "))
       if quini_6 ==1:
              apuesta=[]
              for i in range (6):
                     apuesta1 = int(input("Ingrese un número de 6 cifras del 00 al 45 inclusive: "))
                     if 0<=apuesta1<=45:
                            apuesta.append(apuesta1)
                     else:
                            print("El número debe estar entre 00 y 45")
              print("El número apostado es: ",apuesta)
                     
       if quini_6 ==2:
              apuesta_azar = [randint(0,45) for i in range (6)]
              print("El número ingresado es: ",apuesta_azar)

print("***********************")
print("*Quiniela 'El pela'*")
print("***********************")

menu={"1":"Quiniela",
       "2":"Quini 6",
       "3":"Comprobar apuesta",
       "4":"Arqueo de caja",
       "5":"Salir"}
print("------------------")
print("Opciones")
print("------------------")

for opcion, descipcion in menu.items():
    print(f'*{opcion} - {descipcion}', end="\n")

opcion=int(input("Elija una opción: "))

if opcion ==1:
       opcion1=quiniela(),cliente()
if opcion ==2:
       for opcion2, descipcion in menu.items():
              opcion2=quini_6(),cliente()
       

      
    

    




