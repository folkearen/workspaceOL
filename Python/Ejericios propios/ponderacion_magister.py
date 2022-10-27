def ponderacion_ramos(notas):
    pr = 0
    print("---------- Convirtiendo notas ---------")
    for i in notas:
        x = (i * 70) / 100
        print ("""{:>8} % = {}""".format(i, x))
        pr += i
    print("----------------------------------------")
    pr /= len(notas)
    pn = (pr * 70) // 100
    pon_pr = pr * 0.6 
    print(f"EL promedio del porcentaje de los ramos es {pr}, y su ponderacio es {pon_pr}. El promedio en escal 1 a 7 es {pn}")  
    
    return pon_pr


def ponderacion_tallerTFM(nota_taller, nota_documento):
    nota_taller = nota_taller
    nota_documento = nota_documento
    pon_taller = nota_taller * 0.2
    pon_documento = nota_documento * 0.8
    pon_TFM = pon_taller + pon_documento
    print("La ponderacion del taller TFM es: ", pon_TFM)
    
    return pon_TFM

def ponderacio_finalTFM(ponderacion_finaltaller, defensa):
    pon_ftaller = ponderacion_finaltaller * 0.3
    pon_defensa = defensa * 0.1
    pon_finalTFM = pon_ftaller + pon_defensa
    print("La ponderacion final del TFM es: ", pon_finalTFM)
    
    return pon_finalTFM


def calculo_nota_fianl(ponderado_ramos, ponderado_TFM):
    nota_final = ponderado_ramos + ponderado_TFM
    conversion_NF = (nota_final * 70) / 100
    print(f"El porcentaje final obtenido es {nota_final} y su conversion a escala de 1 a 7 es {conversion_NF}")
    
    return conversion_NF



def run():
    x = ponderacion_ramos([98, 84, 97, 79, 99, 92, 84, 95, 92, 85])
    y = ponderacion_tallerTFM(83, 78)
    z = ponderacio_finalTFM(y,78)
    n = calculo_nota_fianl(x,z)

if __name__ == "__main__":
    run()

