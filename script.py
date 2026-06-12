import pandas as pd
import os

archivo_entrada = "datalake/dataset_transporte_iei095.xlsx"
carpeta_salida = "datawarehouse"
archivo_salida = os.path.join(carpeta_salida, "prueba_volumen.txt")

print("--- Iniciando prueba de infraestructura Docker ---")

# Prueba 1: ¿Docker puede leer el datalake?
try:
    df = pd.read_excel(archivo_entrada)
    print(f"✅ ¡Éxito! Docker pudo leer el Excel. Tiene {len(df)} filas.")
except Exception as e:
    print(f"❌ Error al leer el Excel: {e}")

# Prueba 2: ¿Docker puede escribir en el datawarehouse?
try:
    os.makedirs(carpeta_salida, exist_ok=True)
    with open(archivo_salida, "w") as f:
        f.write("Si puedes abrir este archivo, ¡los volúmenes de Docker funcionan perfectamente!")
    print(f"✅ ¡Éxito! Archivo de prueba creado en {archivo_salida}.")
except Exception as e:
    print(f"❌ Error al escribir: {e}")

print("--- Prueba finalizada ---")
