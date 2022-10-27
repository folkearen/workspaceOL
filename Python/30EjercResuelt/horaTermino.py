hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
hora_final = (hour + (dura//60)) 
minutos_finales = ( mins + (dura % 60) ) 
if hora_final > 24:
    hora_final %= 24 
if minutos_finales >= 60:
    hora_final += minutos_finales//60
    minutos_finales%=60
print(hora_final," : " ,minutos_finales)

#Otra forma
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
mins = mins + dura # find a total of all minutes
hour = hour + mins // 60 # find a number of hours hidden in minutes and update the hour
mins = mins % 60 # correct minutes to fall in the (0..59) range
hour = hour % 24 # correct hours to fall in the (0..23) range
print(hour, ":", mins, sep='')