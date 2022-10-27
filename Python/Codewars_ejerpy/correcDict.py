"""
La función debe devolver un diccionario/Objeto/Hash "status"como clave, cuyo valor puede: "busy"o "available"dependiendo del valor de verdad del argumento is_busy.

Pero como verá después de hacer clic RUNo ATTEMPTeste código tiene varios errores, corríjalos.
"""

def get_status(is_busy):
    status = {"status":"busy"} if is_busy else {"status":"available"}
    return status

#Otra formas
# return {'status': ("busy" if is_busy else "available")}

# return {"status": ("available", "busy")[is_busy]}

# Using "not" so it will work even if busy is different from 0 and 1
# return {"status":("busy", "available")[not is_busy]}