import os

def generar_plan_alimentacion_ejercicios(objetivo, nivel_actividad, imc):
    print("\n----------- PLAN DE ALIMENTACIÓN Y EJERCICIOS -----------")
    print(f"Objetivo: {objetivo}")
    print(f"Nivel de actividad física: {nivel_actividad}")
    print(f"Tu Índice de Masa Corporal (IMC): {imc:.2f}")

    # Generar plan de alimentación
    if objetivo.lower() == 'perdida de peso':
        print("\n--- Plan de Alimentación ---")
        print("Para la pérdida de peso, es importante crear un déficit calórico y enfocarse en alimentos saludables.")
        print("Sugerencias de alimentos: Verduras, frutas, proteínas magras, granos enteros y grasas saludables.")
    elif objetivo.lower() == 'reacondicionamiento fisico':
        print("\n--- Plan de Alimentación ---")
        print("Para el reacondicionamiento físico, es esencial mantener una dieta equilibrada y adecuada para tus necesidades.")
        print("Sugerencias de alimentos: Proteínas magras, carbohidratos complejos, grasas saludables y una variedad de verduras y frutas.")
    elif objetivo.lower() == 'ganancia de músculo':
        print("\n--- Plan de Alimentación ---")
        print("Para la ganancia de músculo, es necesario asegurar un excedente calórico y consumir suficientes proteínas.")
        print("Sugerencias de alimentos: Proteínas magras, carbohidratos complejos, grasas saludables y alimentos ricos en nutrientes.")
    else:
        print("Objetivo no reconocido. Por favor, verifica tu respuesta.")

    # Generar plan de ejercicios
    print("\n--- Plan de Ejercicios ---")
    if nivel_actividad.lower() == 'sedentario':
        print("Para mejorar tu nivel de actividad, considera incorporar al menos 30 minutos de actividad física moderada, como caminar, al día.")
    elif nivel_actividad.lower() == 'ligero':
        print("Para mejorar tu condición física, considera aumentar la intensidad y duración de tus actividades físicas, como correr o nadar.")
    elif nivel_actividad.lower() == 'moderado':
        print("Sigue manteniendo tu rutina actual y considera agregar ejercicios de resistencia y fuerza para mejorar tus capacidades físicas.")
    elif nivel_actividad.lower() == 'activo':
        print("Tu nivel de actividad física es alto, asegúrate de mantener un equilibrio entre el ejercicio intenso y el descanso para evitar lesiones.")
    else:
        print("Nivel de actividad física no reconocido. Por favor, verifica tu respuesta.")

def main():
    print(
        """+-----------------------------+
       |     BIENVENIDO/A A LA       |
       |        CALCULADORA          |       
       |     DEL CAMBIO FÍSICO       |    
       +-----------------------------+    
        """)
    print("Aquí podrás planificar tu cambio físico")
    print("y ver los puntos débiles a mejorar")
    print()
    print("Por favor, responde al siguiente cuestionario")
    print("rellenando los datos necesarios para su evaluación")
    print()

    edad = int(input("Ingrese su edad: "))
    genero = input("Ingrese su género (hombre/mujer):")
    peso = float(input("Ingrese su peso en Kilogramos: (ej. 70.3): "))
    estatura = int(input("Ingrese su estatura en centímetros: (ej. 168) "))
    nivel_actividad = input("Ingrese su nivel de actividad física: (Sedentario/ligero/moderado/activo): ")
    objetivo = input("Ingrese su objetivo con el cambio físico: (perdida de peso, reacondicionamiento fisico, ganancia de músculo): ")

    # Cálculo del Índice de Masa Corporal (IMC)
    estatura_metros = estatura / 100
    imc = peso / (estatura_metros ** 2)

    # Cálculo del Metabolismo Basal (MB) según la fórmula de Harris-Benedict
    if genero.lower() == 'hombre':
        mb = 88.362 + (13.397 * peso) + (4.799 * estatura) - (5.677 * edad)
    else:
        mb = 447.593 + (9.247 * peso) + (3.098 * estatura) - (4.330 * edad)
        
    # Ajuste del Metabolismo Basal (MB) según el objetivo
    if objetivo.lower() == 'perdida de peso':
        mb -= 500
    elif objetivo.lower() == 'ganancia de músculo':
        mb += 50027

    print()
    print("----------- RESULTADOS -----------")
    print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")
    print(f"Tu Metabolismo Basal (MB) es: {mb:.2f}")
    print()

    # Llamar a la función para generar el plan de alimentación y ejercicios
    generar_plan_alimentacion_ejercicios(objetivo, nivel_actividad, imc)

if __name__ == "__main__":
    main()

print()

# Recursos adicionales
print("----------- RECURSOS ADICIONALES -----------")
print("Aquí tienes algunos enlaces a recursos adicionales que pueden ser útiles para ti:")

# Lista de enlaces a recursos adicionales
enlaces_recursos = {
    "Recetas saludables y equilibradas": "https://www.youtube.com/watch?v=2kCOXLkbsKw&t=633s&pp=ugMICgJlcxABGAHKBRFjaHJpcyBoZXJpYSBkaWV0YQ%3D%3D",
    "Rutinas de ejercicios en casa": "https://www.youtube.com/watch?v=NPK0DLP4_r8",
    "Artículos de nutrición y salud": "https://www.youtube.com/watch?v=1D9oyFJkafA&t=12s",
    # Agrega aquí más enlaces a recursos adicionales
}

# Mostrar los enlaces a recursos adicionales
for nombre, enlace in enlaces_recursos.items():
    print(f"- {nombre}: {enlace}")
print(
    
    """+-------------------------------------------+
       |     RECUERDE QUE SEGÚN LOS ESTUDIOS       |
       |     EL IMC SE CLASIFICA DE LA             |       
       |     SIGUIENTE MANERA:                     | 
       |-------------------------------------------|   
       |     MENOS DE 18.5 -->  BAJO PESO          |   
       |     18.5 - 24.9   -->  NORMAL             | 
       |     25.0 - 29.9   -->  SOBREPESO          |
       |     MAYOR DE 30.0 -->  OBESIDAD           |     
       +-------------------------------------------+    
    """)

input("Presiona Enter para salir...")