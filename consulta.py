from pyswip import Prolog

# Consulta el archivo de reglas de Prolog
prolog = Prolog()
prolog.consult("familia.pl")

# Función para procesar la pregunta y obtener la respuesta
def procesar_pregunta(frase):
    sep = frase.lower().split()
    frase_nueva = []
    
    for i in sep:
        if "papa" in i or "padre" in i or "papito" in i:
            i = "papa"
            frase_nueva.append(i)
        elif "mama" in i or "madre" in i or "mamita" in i:
            i = "mama"
            frase_nueva.append(i)
        elif "jose" in i or "pedro" in i or "mario" in i or "karla" in i or "carolina" in i:
            frase_nueva.append(i)
        elif "quien" in i:
            i = "X"
            frase_nueva.append(i)
        elif "hermano" in i or "hermana" in i:
            i = "hermano"
            frase_nueva.append(i)

    if frase_nueva[0] == "X":
        for valor in prolog.query(frase_nueva[1]+"(X, "+frase_nueva[2]+")"):
            print(f"Es {valor['X']}")
    elif frase_nueva[1] == "papa" or frase_nueva[1] == "mama":
        for valor in prolog.query(frase_nueva[1]+"("+frase_nueva[0]+", "+frase_nueva[2]+")"):
            print(f"Asi es, el {frase_nueva[1]} de {frase_nueva[2]} es {frase_nueva[0]}")
    elif frase_nueva[0] == "papa" or frase_nueva[0] == "mama":
        for valor in prolog.query(frase_nueva[0]+"("+frase_nueva[2]+", "+frase_nueva[1]+")"):
            print(f"Asi es, el {frase_nueva[0]} de {frase_nueva[1]} es {frase_nueva[2]}")
    elif frase_nueva[0] == "hermano":
        for valor in prolog.query(frase_nueva[0]+"("+frase_nueva[1]+", "+frase_nueva[2]+")"):
            print(f"{frase_nueva[1]} y {frase_nueva[2]} son hermanos")
    else:
        print("Eso es incorrecto")

# Inicio del ciclo de conversación
while True:
    frase = str(input("Hola, ¿en qué puedo ayudarte? "))
    
    if frase.lower() == "adios":
        print("¡Hasta pronto! :)")
        break
    else:
        procesar_pregunta(frase)

    continuar = input("¿Puedo ayudarte en algo más? (si/no) ")
    if continuar.lower() != "si":
        print("¡Hasta pronto! :)")
        break
