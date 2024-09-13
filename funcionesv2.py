print("Funciones version 2")
print("Samuel Grijalva")
# zona de tuplas, set y diccionario
celulares=["Samsung S24 Ultra","Iphone 15 Pro Max","Chafa"]
TUPLA=["Manzana","sadia","tomate"]
SET={"Flores","Mota","Roger"}
DICCIONARIO={
    "DODGE":"Challenger",
    "FORD":"F150",
    "CHEVY":"Camaro"
}

# zona de funciones
def verlista(telefonos):
    for uncelular in telefonos:
        print(uncelular)

def verBanca(pressbanca):
    for banca in pressbanca:
        print(banca)

def integrantesSi14(si14):
    for INTE in si14:
        print("--",INTE,"--")
        
# Llamadas a funciones
print("IMPRIME CELULARES ")
verlista(celulares) 
print("IMPRIME LAS FRUTAS")
verBanca(TUPLA) 
print("IMPRIME EL DICCIONARIO DE CARROS")
for x in DICCIONARIO:
    print(DICCIONARIO[x])
print("IMPRIME INTEGRANTE DE 'Si 14'")
integrantesSi14(SET)