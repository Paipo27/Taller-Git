import pandas as pd
#bilibioteca para leer archivos excel pandas

#funcion para cargar los estudiantes desde un archivo excel
def cargar_estudiantes(ruta):
    estudiantes = []
    try:
        #leemos el archivo excel con pandas y openpyxl
        df = pd.read_excel(ruta, engine='openpyxl', header=None, names=['nombre', 'nota'])
        for _, fila in df.iterrows():
            nombre = str(fila['nombre']).strip()
            try:
                # Convertimos la nota a float y verificamos que esté en el rango válido
                nota = float(fila['nota'])
                if 0.0 <= nota <= 5.0:
                    estudiantes.append((nombre, nota))
            except ValueError:
                continue
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
    return estudiantes

