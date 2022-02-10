import screen
screen.clear()

def operaciones(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a/b        
    screen.locate(5,4)
    print(a, "+", b, "=", suma)
    screen.locate(6,4)
    print(a,"-",b,"=", resta)
    screen.locate(7,4)      
    print(a, "*", b, "=", multiplicacion)      
    screen.locate(8,4)
    print(a,"/",b, "=", division)            


def pideNumero():
    screen.locate(1,1)
    a = int(input("escribe un numero: "))
    screen.clear()
    screen.locate(1,1)
    b = int(input("escribe otro numero: "))
    screen.clear()
    while a != 0 and b != 0:
        screen.clear()
        operaciones(a,b)
        screen.locate(1,1)
        a = int(input("escribe un numero: "))
        screen.clear
        screen.locate(1,1)
        b = int(input("escribe otro numero: "))
       
pideNumero()

    

