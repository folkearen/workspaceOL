import time

reloj = time.localtime()
hora_actual = (reloj.tm_hour, reloj.tm_min, reloj.tm_sec)
hora_de_salir = (19, 0, 0)

if hora_de_salir == hora_actual:
    print("Es hora de salir")
else:
    print(f"Faltan {hora_de_salir[0] - hora_actual[0]} horas {59 - hora_actual[1]} minutos {59 - hora_actual[2]} segundos\nPara salir del trabajo")