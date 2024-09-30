import random

# Lista de palabras posibles
palabras = ["python", "desarrollo", "programacion", "juego", "algoritmo"]

# Seleccionar una palabra al azar
palabra_secreta = random.choice(palabras)
# Inicializar el progreso de la palabra (con guiones bajos)
progreso_palabra = ["_"] * len(palabra_secreta)

# Número de intentos permitidos
intentos_restantes = 6

# Letras ya adivinadas
letras_adivinadas = []
letra = input("Adivina una letra: ").lower()

# Comprobar si la letra ya fue adivinada
if letra in letras_adivinadas:
    print("Ya has adivinado esa letra.")
else:
    letras_adivinadas.append(letra)
    if letra in palabra_secreta:
        # Actualizar el progreso si la letra está en la palabra
        for i, l in enumerate(palabra_secreta):
            if l == letra:
                progreso_palabra[i] = letra
    else:
        intentos_restantes -= 1
        print(f"Letra incorrecta. Te quedan {intentos_restantes} intentos.")

print(" ".join(progreso_palabra))

if "_" not in progreso_palabra:
    print("¡Felicidades! Adivinaste la palabra:", palabra_secreta)
elif intentos_restantes == 0:
    print("Perdiste. La palabra era:", palabra_secreta)
while intentos_restantes > 0 and "_" in progreso_palabra:
    letra = input("Adivina una letra: ").lower()
    
    if letra in letras_adivinadas:
        print("Ya has adivinado esa letra.")
    else:
        letras_adivinadas.append(letra)
        if letra in palabra_secreta:
            for i, l in enumerate(palabra_secreta):
                if l == letra:
                    progreso_palabra[i] = letra
        else:
            intentos_restantes -= 1
            print(f"Letra incorrecta. Te quedan {intentos_restantes} intentos.")

    print(" ".join(progreso_palabra))

if "_" not in progreso_palabra:
    print("¡Felicidades! Adivinaste la palabra:", palabra_secreta)
else:
    print("Perdiste. La palabra era:", palabra_secreta)
