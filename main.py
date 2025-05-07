from estudiantes.registro import *

def main():
    ruta = "Estudiantes.xlsx"
    estudiantes = cargar_estudiantes(ruta)
    if estudiantes:
        mostrar_estudiantes(estudiantes)
        promedio = calcular_promedio(estudiantes)
        print(f"\nPromedio general: {promedio:.2f}")
    else:
        print("No se encontraron estudiantes válidos.")

if __name__ == "__main__":
    main()