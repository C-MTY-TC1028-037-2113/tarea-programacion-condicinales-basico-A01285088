def main():

    lado1 = int(input("Ingresa la medida del lado 1: "))
    lado2 = int(input("Ingresa la medida del lado 2: "))
    lado3 = int(input("Ingresa la medida del lado 3: "))
    #Escribe aquí tu código...
    
    if lado1 <(lado2 + lado3) and lado2<(lado1+ lado3) and lado3<(lado1 + lado2):
        
        if lado1 == lado2 == lado3:
            print('ES UN TRIANGULO EQUILATERO')
            
        elif lado1 == lado2 or lado3 == lado2 or lado1 == lado3: 
            print('ES UN TRIANGULO ISOSCELES')

        else:
            print('ES UN TRIANGULO ESCALENO')

    else:
        print('NO ES TRIANGULO')

if __name__=='__main__':
    main()

