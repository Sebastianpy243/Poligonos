#Juan Sebastian Fernandez Buitrago --- Grupo 43 

import turtle
from time import sleep

ancho = 300
alto = 300

def inicializa_ventana(y:int=0, size:int=10, color:str = '#33cc8c', shape: str = 'turtle') -> object:
    #creación de la ventana
    ventana = turtle.Screen()
    ventana.setup(900, 900)
    ventana.screensize(ancho, alto)
    #creacion de la tortuga iniciando desde abajo de la pantalla
    tortuga = turtle.Turtle()
    tortuga.shape(shape)
    tortuga.pencolor(color)
    tortuga.pensize(size)
    tortuga.penup()
    tortuga.setx(0)
    tortuga.sety(y)
    tortuga.pendown()
    return(tortuga, ventana)

def poligreg(ancho: int, alto: int, ventana: object, tortuga: object) -> None:
    #Función que dibuja el poligono regular
    n = int(input('Ingrese la cantidad de lados del poligono: '))
    for i in range(n):
        sleep(0.5)
        alto += 100
        ancho += 50
        ventana.screensize(ancho, alto)
        tortuga.forward(100)
        tortuga.left(360/n)
    sleep(3)

def espiral(ancho: int, alto: int, ventana: object, tortuga: object)->None:
    #Funcion que dibuja el espiral
    a = int(input('Ingrese el número de espiras: '))
    n = int(input('Ingrese la cantidad de lados del poligono: '))
    avanza = 10
    for i in range(a*2):
        alto += 100
        ancho += 50
        ventana.screensize(ancho, alto)
        tortuga.forward(avanza)
        tortuga.left(360/n)
        tortuga.forward(avanza)
        tortuga.left(360/n)
        avanza += 10
    sleep(3)

def espiral_especial(tortuga: object)->None:
    n = int(input('Ingrese numero de lados del poligono espiral: '))
    for i in range(0,250,5):
        for j in range(n):
            tortuga.forward(i)
            tortuga.left(360/n)
        tortuga.left(10)
    sleep(3)

def menu()-> None:
    #Menú inicial
    while True:
        mensaje = '''\nEl siguiente programa dibuja poligonos regulares y espirales
        
                    Ingrese la opción que prefiera
                    
                    1. Dibujar Poligono Regular
                    2. Dibujar Espiral
                    3. Dibujar Espirar Especial
                    4. Cerrar'''.title()
        opcion = int(input(mensaje+'\n->'))
        if opcion == 1:
            tortuga, ventana = inicializa_ventana(-300, 10)
            poligreg(ancho, alto, ventana, tortuga)
            ventana.reset()
            ventana.clear()
            continue
        if opcion == 2:
            tortuga,ventana = inicializa_ventana(0, 2)
            espiral(ancho, alto, ventana, tortuga)
            ventana.reset()
            ventana.clear()
            continue
        if opcion == 3:
            tortuga,ventana = inicializa_ventana(0,2,'black', 'classic')
            espiral_especial(tortuga)
            ventana.reset()
            ventana.clear()
            continue
        elif opcion == 4:
            print('\n\n\tfin de la ejecución..\n'.upper())
            break
        else:
            print('\n\tERROR:::Debe ingresar una opción del menú')
            sleep(1)

menu()



