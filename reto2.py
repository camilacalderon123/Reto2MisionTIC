print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
nombreDeUsuario = int(input("Ingrese su usuario: "))

menu = [" 1.Cambiar contraseña"," 2.Ingresar coordenadas actuales", " 3.Ubicar zona wifi más cercana", " 4.Guardar archivo con ubicación más cercana", " 5.Actualizar registros de zonas wifi desde archivo",
         " 6.Elegir opción de menú favorita", " 7.Cerrar sesión"]

#Función la cual contiene el resto de opciones del menú y se hace el llamado a la función de favoritos
def menuAdaptativo():
  intentos = 0

  while(intentos <= 2):
    print(menu[0])
    print(menu[1])
    print(menu[2])
    print(menu[3])
    print(menu[4])
    print(menu[5])
    print(menu[6])
    opcion = int(input("Elija una opción: "))
    aux = opcion
    opcion -=1
    if(opcion == 0):
      opcion += 1
      print(f"Usted ha elegido la opción {opcion}")
      break
    elif(opcion == 1):
      opcion += 1
      print(f"Usted ha elegido la opción {opcion}")
      break
    elif(opcion == 2):
      opcion += 1
      print(f"Usted ha elegido la opción {opcion}")
      break
    elif(opcion == 3):
      opcion += 1
      print(f"Usted ha elegido la opción {opcion}")
      break
    elif(opcion == 4):
      opcion += 1
      print(f"Usted ha elegido la opción {opcion}")
      break
    elif(opcion == 5):
      favoritos()
    elif(opcion == 6):
        print("Hasta pronto")
        break
    elif(aux > 7):
      intentos += 1
      if(intentos ==3):
        print("Error")

#Función para que se pueda elegir la opción favorita de la persona
def favoritos():
  favorita = int(input("Seleccione opción favorita: "))
  if(favorita <=4 and favorita != 6 and favorita != 7):
    respuesta = int(input("Para confirmar por favor responda:\n¿Cuánto son tres medias moscas y mosca y media?: "))
    if(respuesta == 3):
      respuesta2 =int(input("Para confirmar por favor responda:\n¿Qué cosa será aquella que mirada del derecho y mirada del revés siempre un número es?:"))
      if(respuesta2 == 6):
        aux = favorita - 1
        quitando = menu.pop(aux)
        menu.insert(0,quitando)
      else:
        print("Error")       
    else:
        print("Error")
  else:
    print("Error")
    exit()


#Funcion para iniciar sesión por parte del usuario
def inicioDeSesion(): 
  if(nombreDeUsuario == 51636):
   contrasena = int(input("Ingrese su contraseña: "))
   if(contrasena == 63615):
     numero1 = nombreDeUsuario % 1000
     numero2 = int(6/(6 % 5+1))
     suma = int(input("Ingrese la suma de " + str(numero1) + " + " + str(numero2) + " = "))   
     if(suma == 639):   
       menuAdaptativo()      
     else:
       print("Error")
   else:
      print("Error")
  else:
   print("Error")


inicioDeSesion()


