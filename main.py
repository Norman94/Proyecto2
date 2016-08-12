

#Metodo para encontrar primo
def es_primo(numero):
    contador = 0
    verificar = False
    #Verificamos
    for i in range(1, numero + 1):
        if (numero % i) == 0:
            contador = contador + 1
        if contador >= 3:
            verificar = True
            break

    if contador == 2 or verificar == False:
        print ("el numero es primo")
    else:
        print ("el numero no es primo")





def main():
        try:
                numUsuario = int(input("Digite un numero:"))
                if(numUsuario<=0):
                    print("Debe de digitar un numero entero")
                elif(numUsuario==1):
                    print ("El numero es impar y primo a la vez")
                elif((numUsuario%2)==0):
                    print("par")
                else:
                    print("Impar")
                es_primo(numUsuario)

        except:
                print("Debe de digitar un numero entero")


main()