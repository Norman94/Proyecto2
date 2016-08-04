





try:
        numUsuario = int(input("Digite un numero:"))
        if(numUsuario<=0):
            print("Debe de digitar un numero entero")



        if(numUsuario==1):
            print ("El numero es inpar y primo a la vez")
        elif((numUsuario%2)==0):
            print("par")
        else:
            print("Primo")
except:
        print("Debe de digitar un numero entero")


