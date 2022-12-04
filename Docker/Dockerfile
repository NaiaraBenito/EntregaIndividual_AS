# Imagen base
FROM neo4j

# Crear carpeta donde ejecutar el cliente
RUN mkdir /miCliente

# Instalar paquete de python3 y la librería neo4j de python
RUN apt -qq update && apt -qq -y install python3
RUN apt -qq -y install python3-pip
RUN python3 -m pip install neo4j

# Exponer el puerto 7474 y 7687
EXPOSE 7474
EXPOSE 7687

# Copiar main.py en la carpeta /miCliente
COPY main.py /miCliente
COPY html/index.html /miCliente

# Ubicarse dentro de la carpeta /miCliente
WORKDIR /miCliente

# Ejecutar como comando de arranque el main.py
CMD python3 main.py

# Autora: Naiara Benito Balbás
