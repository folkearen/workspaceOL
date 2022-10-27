def make_readable(seconds):
    horas = seconds // 3600
    minutos = (seconds%3600)//60
    segundos = minutos%60

    if horas<10 and minutos < 10 and segundos<10 :
        return(f"0{horas}:0{minutos}:0{segundos}")
    elif minutos < 10 and segundos<10 :
        return(f"{horas}:0{minutos}:0{segundos}")
    
    elif horas < 10:
        return(f"0{horas}:{minutos}:{segundos}")   

    elif minutos < 10:
        return(f"{horas}:0{minutos}:{segundos}")    
    elif segundos < 10:
        return(f"{horas}:{minutos}:0{segundos}")

   


    
    return(f"{horas}:{minutos}:{segundos}")

print(make_readable(0))