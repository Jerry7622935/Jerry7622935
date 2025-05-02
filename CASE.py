dia=int(input("ingrese un numero del 1 al 7 para mostrar los dias de la semana"))
match dia:
    case 1: print("domingo")
    case 2: print("lunes")
    case 3: print("martes")
    case 4: print("miercoles")
    case 5: print("jueves")
    case 6: print("viernes")
    case 7: print("sabado")
    case _:
        print("error era un numero del 1 al 7")

        
