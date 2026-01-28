# Hay que definir las variables (lo hacemos mientras vamos necesitando)
# Hay una "PALABRA DEL DIA"
# La palabra ingresada solo puede tener 5 letras ---> inf len(palabra) == 5 (entra al juego)
# si es igual a 5 debe enviar un mensaje de eroor y que vuelva a intentar ----> print("vuelva a intentar")
# tenemos 6 oportundidades de ganar ---> for oportunidades in range(6) (entra al juego)
# necesitamos comparar cada caracter de la palabra con cada caracter del wordle, tambien debemos considerar la posición que esta
# POdemos transformar el string a lista para guardar la posicieon de cada caracter de la letra, como vamos a usar varias veces podemos hacer una función 
#def cambiar_a_lista(cadena)
#    cadena_vector = [0,1,2,3,4] #definimos las variables locales
#    i = 0 #indicador de posición
#    for letra_cadena in cadena:
#        cadena_vector[i]=letra_cadena
#        i=i+1
#    return cadena_vector # return devuelve el valor de una variable al programa principal
    #si exite la letra y esta en la posición correcta debe avisar 
    #si la letra esta en la palabra entonces la letra esta correcta y la posición cirrecta
    #si no existe la letra entonces
print("Bienvenidos a WORDLE by leonshy")
wordle = "MUNDO"
oportunidades = 0 # va a contar la cantdad de palabras ingresadasa correctamente 
while oportunidades < 6: #tenemos 6 oportunidades
    print("-----------------------------------------")
    print(f"Oportunidad #{oportunidades+1}")
    palabra = input("ingrese una palabra en mayuscula")
#   primero vamos a verificar si es que la palabra ingresada tiene 5 letras
    if len(palabra) == 5: #En caso que coincida entramos al juego 
        aciertos = 0 #asignamos un contador que si llega a 5 es porque se gano el juego
        m = 0 #indicador de posición de palabra
        for letra_palabra in palabra :
            caracter = False
            posicion = False
            #print(letra_palabra,m)
            n = 0 #indicador de posición en wordle
            for letra_wordle in wordle :
                #print(letra_wordle,n)
                if letra_palabra == letra_wordle:
                    caracter = True
                    #print("coicide la letra")
                    if m == n:
                        posicion = True
                        #print ("coicide posición") 
                n = n+1
            if caracter == False:
                print(letra_palabra,"     NOOO - No existe el caracter")
            elif caracter == True and posicion == False:
                print(letra_palabra,"     CASI - El caracter existe, pero no esta en la posicieon correcta")
            else:
                print(letra_palabra,"     SIII - El caracter existe, y esta en la posición correcta")
                aciertos = aciertos+1    
            m = m+1
        print(f"tenés {aciertos} aciertos")
        if aciertos == 5:
            print("...:::¡¡¡FELICIDADES GANASTE!!!:::... ")
            break        
        oportunidades = oportunidades + 1
        if oportunidades > 5:
            print("PERDISTE, mejor suerte la proxima")
            break
    else:
        print("la palabra que ingresaste no es valida debe ser de 5 caracteres") 
print("GRACIAS POR JUGAR")  