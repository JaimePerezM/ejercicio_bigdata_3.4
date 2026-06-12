# 1. Usamos una imagen oficial de Python ligera
FROM python:3.10-slim

# 2. Definimos el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiamos el archivo de dependencias y las instalamos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiamos el resto de los archivos (script y csv) al contenedor
COPY . .

# 5. Comando por defecto al iniciar el contenedor
CMD ["python", "script.py"]