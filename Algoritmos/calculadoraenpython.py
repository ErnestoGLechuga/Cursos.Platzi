# Crear una calculadora con operaciones basicas

#Esta calculara esta encendida para las operaciones que el usuario necesite
#Le pedimos al usuario que nos entregue los 2 numeros
n1 = int(input("Introduce tu primer número: ") )
n2 = int(input("Introduce tu segundo número: ") )

opcion = 0

#Creamos un ciclo "While" para mantener la calculadora activa mientras quiera el usuario
while True:

    #creamos nuestro menu de opciones
    print("""
    Dime, ¿qué quieres hacer?
    
    1) Sumar los dos números
    2) Restar los dos números
    3) Multiplicar los dos números
    4) Cambiar los números elegidos
    5) Apagar calculadora
    """)
    opcion = int(input("Elige una opción: ") )     

#creamos las operaciones a llevar a cabo de acuerdo a la seleccion del usuario
    if opcion == 1:
        print(" ")
        print("RESULTADO: La suma de",n1,"+",n2,"es igual a",n1+n2)
    elif opcion == 2:
        print(" ")
        print("RESULTADO: La resta de",n1,"-",n2,"es igual a",n1-n2)
    elif opcion == 3:
        print(" ")
        print("RESULTADO: El producto de",n1,"*",n2,"es igual a",n1*n2)
    elif opcion == 4:
        n1 = float(input("Introduce tu primer número: ") )
        n2 = float(input("Introduce tu segundo número: ") )
    elif opcion == 5:
        break
    else:
        print("Opción incorrecta")