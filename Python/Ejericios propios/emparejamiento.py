equipos = ["Equipo 1", "Equipo 2", "Equipo 3", "Equipo 4", "Equipo 5"]

for equipo_local in equipos:
    for equipo_visitante in equipos:
        if equipo_local != equipo_visitante:
            print(equipo_local + " V/S " + equipo_visitante)