import hashlib

def listaPalabras():
    palabras = ['Hola','1234','password','123abc','aLTaCOnTrAs@ña12.', 't3fu1st3.h4ck34d0@']
    return palabras
    
def adivinarContraseña(contraseña, listaContraseñas):
    for password in listaContraseñas:
        resultado = hashlib.md5(password.encode())
        if contraseña == resultado.hexdigest():
            return password
    return 1

def imprimir(texto_claro, hash):
    if texto_claro != 1:
        print(f"El hash md5 '{hash}' descifrado es -> {texto_claro}")
    else:
        print(f"El hash md5 '{hash}' NO se pudo descifrar :(")
        
        
# MAIN # 

md5Pass = '5896d3690544fa3af676a8f94b8bad73'

listaPa = listaPalabras()

importante = adivinarContraseña(md5Pass, listaPa)

imprimir(importante, md5Pass)

# PoV: a906449d5769fa7361d7ecc6aa3f6d28 - 5896d3690544fa3af676a8f94b8bad73 - 181461fa05c3f88bf544f07e5f9c7e3d - 5f4dcc3b5aa765d61d8327deb882cf99 #