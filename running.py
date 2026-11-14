
entrenamientos = []



while True:

    try:
        tiempo_enminutos = float(input("Tiempo de carrera en minutos: "))
        distancia_km = float(input("Distancia de carrera: "))

    except ValueError:
        print("Error: introduce un número.")
        continue

    if tiempo_enminutos <= 0 or distancia_km <= 0:
        print("Escribe un valor mayor que 0!")
        continue

    tiempo_ensegundos = tiempo_enminutos * 60

    ritmo_segundos = round(tiempo_ensegundos / distancia_km)

    ritmo_medio_minutos = ritmo_segundos//60
    segundos_restantes = ritmo_segundos % 60
    tiempo_medio = (f'{ritmo_medio_minutos}:{segundos_restantes:02d}')


    entrenamiento = {
        "Tiempo" : tiempo_enminutos,
        "Distancia" : distancia_km,
        "Ritmo" : tiempo_medio,
    }

    entrenamientos.append(entrenamiento)

    respuesta = input("Quieres registrar otro entrenamiento? (si/no): ").strip().lower()
    

    if respuesta.lower() == "no":
        break


for numero, entrenamiento in enumerate(entrenamientos, start =1):
    print(f'Entrenamiento {numero}')
    print(f'Tiempo: {entrenamiento["Tiempo"]} minutos')
    print(f'Distancia: {entrenamiento["Distancia"]} km')
    print(f'Ritmo: {entrenamiento["Ritmo"]} min/km')
    print()

#ESTADISTICAS

print(f'Entrenamientos realizados: ')