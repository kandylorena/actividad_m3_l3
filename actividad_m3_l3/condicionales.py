 #1. Decisión simple
edad = int(input("ingresa un numero: "))
if edad >= 18 :
    print("Eres mayor de edad")
else:
     print("Eres menor de edad")

#2. Decisión múltiple con elif
calificacion = int(input("ingresa la calificacion entre 1 y 7: "))
if calificacion == 7:
     print("Excelente")
elif calificacion == 6:
      print("Muy bien")
elif calificacion == 5:
      print("Bien")
elif calificacion == 4:
      print("Suficiente")
elif 1 <= calificacion <= 3:
    print("Insuficiente")
else:
     print("ingresa una nota valida")


#3. Condiciones anidadas
numero= int(input("Ingresa un numero entero: "))
if numero >=0:
     if numero== 0:
        print("Numero es 0")
     else:
        print("Numero es positivo")
else:
    print("Numero es negativo") 

#4. Condición de borde
numero_usuario= int(input("ingresa un numero entre 1 y 100: ")) # Solicito el numero al usuario
if numero_usuario == 1 or numero_usuario== 100: # valido con la condicional si es uno de los extremos
     print("estas en un limite permitido")
elif 1< numero_usuario <100: # valida si esta en el rango intermedio
     print("dentro del rango")
else: # si hay algun numero fuera de los solicitados
     print("fuera de rango")