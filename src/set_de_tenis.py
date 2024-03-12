def evaluar(num_victorias_a, num_victorias_b):
    # TODO: Coloca aquí el código del ejercicio 1: Set de tenis
    resultado = ""
    if num_victorias_a > num_victorias_b:
        mayor=num_victorias_a
        menor=num_victorias_b
        ganador = "A"
    else:
        mayor=num_victorias_b
        menor= num_victorias_a
        ganador ="B"

    if (mayor == 6) and (mayor-menor==2): #Alguien ya ganó con 2 victorias encima y hasta 6
        respuesta = "Ganó " + ganador
    elif (mayor == 7 and (menor == 6 or menor == 5) ):#Ganó alguien por ultimo juego empate 6-6, o por empate 5-5
        respuesta="Ganó " + ganador 
    elif (mayor<7 and mayor-menor!=2): #Condiciones por las que aun no termina
        respuesta="Aún no termina"
    else: #Todo lo demás es inválido
        respuesta = "Inválido"
    return (respuesta)

if __name__ == '__main__':
    print("Los juegos ganaddor por A:", end="")
    num_victorias_a = int(input())
    print("Los juegos ganaddor por B:", end="")
    num_victorias_b = int(input())

    respuesta = evaluar(num_victorias_a, num_victorias_b)
    print(respuesta)
