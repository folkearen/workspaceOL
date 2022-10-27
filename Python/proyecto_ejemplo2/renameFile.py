import os
import shutil
import time

def multi_copy():
    arch = 0
    for i in range(3):
        arch+= 1
        origen = 'C:/Users/alanm/Desktop/a/discurso defensa.docx'
        destino = 'C:/Users/alanm/Desktop/b/' + str(arch)
        shutil.copyfile(origen, destino)
    
time.sleep(1)
    
def rename():
    os.chdir('C:/Users/alanm/Desktop/b/')
    ruta = 'C:/Users/alanm/Desktop/b/'
    oldname = []
    for file in os.listdir():
        oldname.append(file)

    newname = []
    with open('C:/Users/alanm/Desktop/a/Nuevos nombre.txt', 'r', encoding='utf8', errors='ignore') as tf:
        lines = tf.read().split('\n')
    for line in lines:
        newname.append( line + '.docx')

    for i, h in zip(oldname, newname):
            os.rename(ruta+i,ruta+h )

def run():
    multi_copy()
    rename()


if __name__ == '__main__':
    run()

