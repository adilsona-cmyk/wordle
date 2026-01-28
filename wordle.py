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