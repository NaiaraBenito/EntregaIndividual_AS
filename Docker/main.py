# Importar la librería neo4j
from neo4j import GraphDatabase
import time
############################################################
#   Cliente que realiza los siguientes comportamientos:    #
#       - Crear tres nodos  n                              #
#       - Crear relaciónes entre esos nodos                #
#	- Obtener los nombres de todos los nodos (Persona) #
############################################################

# Conectarse a la base de datos con un driver
# Se establece la dirección IP del contenedor neo4j
uri = "neo4j://neo4j:7687"

# En el apartado auth se mandan el usuario y la contraseña para conectarse a la BBDD
driver = GraphDatabase.driver(uri, auth=("neo4j", "1234"))

#--------- Método para crear un nodo ---------#
def crear_persona(comando, nombre):

    # Mensaje informativo
    print("Creando Persona: " + nombre)

    # Crear un nodo (Persona) con el nombre recibido como parámetro
    comando.run("CREATE (persona:Persona {nombre: $nombre})", nombre=nombre)


#--------- Método para crear una relación entre nodos ---------#
def crear_amistad_con(comando, nombre, amigo):

    # Mensaje informativo
    print("Creando amistad entre: " + nombre + " y " + amigo)

    # Primero, buscamos el nodo al que queremos agregarle la relación (MATCH () WHERE...)
    # Luego, creamos la relación con el otro nodo  (CREATE ()-[]->())
    # Simultáneamente, se crea el nodo de nombre recibido en el parámetro amigo
    comando.run("MATCH (persona:Persona) WHERE persona.nombre = $nombre "
           "CREATE (persona)-[:AMIGOS]->(:Persona {nombre: $amigo})", nombre=nombre, amigo=amigo)

#--------- Método para obtener la lista de nombres de los nodos ---------#
def lista_de_personas(comando):

    # Esta variable almacenará los nombres de todos los nodos
    return_list = []

    # Hacer una petición a Neo4j. Obtener los nombres de todos los nodos tipo Persona, y evitar las repeticiones (Distinct)
    transaction_result = comando.run("MATCH (p:Persona) RETURN distinct p.nombre")

    # Recorrer cada nodo tipo persona y guardar el nombre
    return_list= [j[0] for j in transaction_result]

    # Imprimir lista de nombres
    print(return_list)

    # Abrir index.html de la carpera /html
    f = open('/html/index.html','w')

    # Crear el mensaje que se va ha escribir en index.html
    mensaje = "<html><head></head><body><p>"

    for i in return_list:
        mensaje = mensaje + "\n" + i

    mensaje = mensaje + "</p></body></html>"

    # Sacar el mensaje por pantalla
    print(mensaje)

    # Escribir el mensaje en index.html
    f.write(mensaje)

    # Cerrar el archivo
    f.close()

#--------- Llamada a los métodos ---------#

# Abrir una sesión conectándose a Neo4j con el driver
with driver.session() as session:

    # Esperar 5s para darle tiempo a la BBDD a iniciarse
    time.sleep(5)

    # Escribir en la BBDD el comando para crear un nodo de tipo Persona con el nombre de Naiara
    session.execute_write(crear_persona, "Naiara")

    # Escribir en la BBDD el comando para crear una relación (AMIGOS) entre el nodo Naiara y otro nodo
    # (El otro nodo se crea en este método)
    session.execute_write(crear_amistad_con, "Naiara", "Ane")
    session.execute_write(crear_amistad_con, "Naiara", "Maite")
    session.execute_write(lista_de_personas)

# Cerrar el driver
driver.close()


# Autora: Naiara Benito Balbás
