
def main():
    edad = int(input("Ingresa tu edad: "))
    
    #Aquí empieza tu programa...

    if edad >= 18:
        identificacion = input("¿Tienes identificación oficial? (s/n): ")
        if identificacion == "s" :
            print('Trámite de licencia concedido')
        elif identificacion == "n":
            print('No cumples requisitos')
        else:
            print('Respuesta incorrecta')

    elif edad < 18:
        print('No cumples requisitos')
    
    
if __name__ == '__main__':
    main()

   