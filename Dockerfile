FROM python:3.10-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de dependencias
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia los archivos de la aplicación
COPY calculator.py .
COPY app.py .
COPY test_calculator.py .

# Expone el puerto 3000
EXPOSE 3000

# Ejecuta la aplicación web
CMD ["python", "app.py"]