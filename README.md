# Peer-to-peer

El término sistema peer-to-peer (P2P) abarca un amplio conjunto de aplicaciones distribuidas que permiten compartir recursos informáticos mediante el intercambio directo entre sistemas. El objetivo de un sistema P2P es agregar recursos disponibles en el borde de Internet y compartirlos de manera cooperativa entre los usuarios.

Este proyecto tiene como objetivo diseñar e implementar una arquitectura para obtener recursos de un modo distribuido basada en nodos.
Un nodo es un proceso que realiza básicamente dos funciones: cargar número y solicitar suma por parte de otros nodos de la red.


# Modelado 📖

A continuación, podemos evidenciar un grupo de máquinas que están dispuestas en forma de un anillo para actuar como un servidor distribuido. Este grupo de máquinas se funcionará para proporcionar un mejor equilibrio de carga y una mayor disponibilidad.



<p align="center"><img src="https://github.com/jhonnyrod/suma_nodos/blob/master/Modelado%20Peer-to-peer.jpeg" /> </p>



# Pre-requisitos 📋

Para la elaboración de este proyecto fue necesario utilizar una librería de Python llamada p2p networking.

Es una librería de red simplificada para construir redes punto a punto en Python. Esta librería fue diseñada para resolver el problema de encontrar nodos y evitar los NAT para que pueda concentrarse en escribir el código de su aplicación.

+ Reenvío de puertos automatizados.
+ Soporte para perforación de agujeros TCP / apertura simultánea.
+ Conexión inversa (dígale a un nodo que se conecte a usted).

Se realizó la instalación de la librería a través de CMD utilizando el siguiente comando:

```pip install p2pnetwork```

![alt text](https://github.com/jhonnyrod/suma_nodos/blob/master/p2pnetwork.jpeg)
<p align="center">Figura 2 Instalación de la librería p2pnetwork</p>


# Codigo ⚙️

Clase nodo.py
```
import sys
import time
from p2pnetwork.node import Node

# node_callback
#  event         : event name
#  node          : the node (Node) that holds the node connections
#  connected_node: the node (NodeConnection) that is involved
#  data          : data that is send by the node (could be empty)

#variable verificadora
esfinal=False

def node_callback(event, main_node, connected_node, data):
    try:
        #aquí se verifican eventos en nuestra red
        if event != 'node_request_to_stop': # node_request_to_stop does not have any connected_node, while it is the main_node that is stopping!
            if event=="node_message":
                solicitud=str(data)
                if "sumar" in solicitud:
                    global esfinal
                    if  esfinal==True:
                        numeros=solicitud.replace("sumar:","").split("-")
                        suma=0
                        for numero in numeros:
                            try:
                                suma+= int (numero)
                            except Exception as e:
                                suma=suma
                        print(suma)
                        esfinal=False
                    else:
                        
                        node.connect_with_node('127.0.0.1', 8002)
                        time.sleep(1)
                        
                        with open("F:/Documentos/Doceavo/Sistemas distribuidos/Suma_nodos/nodo1/numeros.txt", "r") as file:
                            for line in file:
                                solicitud=solicitud+line
                        for n in node.nodes_outbound:        
                            node.send_to_node(n,solicitud)
                        
                

    except Exception as e:
        print(e)

# The main node that is able to make connections to other nodes
# and accept connections from other nodes on port 8001.
node = Node("127.0.0.1", 8001, node_callback)

# Do not forget to start it, it spins off a new thread!
node.start()
time.sleep(1)




#crear txt
txt = open("F:/Documentos/Doceavo/Sistemas distribuidos/Suma_nodos/nodo1/numeros.txt","w")
txt.close()

while True:
    try: 
        print("\nMenu\n1. insertar número \n2.hacer suma de nodos \n3. Salir")
            
        opc = int(input(" \nQué desea realizar?: "))

        if opc == 1:
            num = input("\nEscriba el numero que desea agregar  ")
            txt = open("F:/Documentos/Doceavo/Sistemas distribuidos/Suma_nodos/nodo1/numeros.txt","a")#Creando txt con la información del cliente
            txt.write("{}-".format(num))
            txt.close()
        elif opc == 2:
            numbers = []
            
            node.connect_with_node('127.0.0.1', 8002)
            time.sleep(1)
            print(node)
            with open("F:/Documentos/Doceavo/Sistemas distribuidos/Suma_nodos/nodo1/numeros.txt", "r") as file:
                enviar="sumar:"
                for line in file:
                    enviar=enviar+line
            for n in node.nodes_outbound:        
                node.send_to_node(n,enviar)
            esfinal=True
            
        elif opc == 3:
            node_2.stop()
            print('end')
            break
    except ValueError:
        print("Porfavor, ingresa solo numeros")

```
# Metodos Empleados 🔧

Los métodos presentados en este documento son implementados con el lenguaje de programación Python.
Hemos optado por llevar a cabo la implementación con Python, porque varios tipos de datos, módulos y bibliotecas ofrecidos hacen posible que la programación sea manejable.Por lo tanto, los siguientes ejemplos se presentan para ilustrar algunos de los beneficios del lenguaje.

###### Descubriendo nodos 
queremos que los nodos puedan enviarse mensajes entre sí y hablar, para esto necesitamos anunciar nuestro propio ip:port  de escucha.
 
```node = Node("127.0.0.1", 8001, node_callback)```

para iniciar el nodo utilizamos el siguiente código el cual inicia un nuevo hilo:

```node.start()```

En este punto necesitamos realizar la conexión con un nuevo nodo, lo cual se logra usando esta parte del código, es necesario especificar la Ip del nodo "vecino" y el puerto

```node.connect_with_node('127.0.0.1', 8002)```

El siguiente método es principal, el cual utilizamos para recibir el mensaje junto con otros datos como el nombre del evento y el nodo emisor, en este punto verificamos si el nodo que recibe el mensaje es el final y de ser así suma la cadena de números recibida por los otros nodos, en caso contrario realiza la conexión con un nuevo nodo empleando el código mencionado anteriormente enviando el mismo mensaje pero concatenando su número asignado en un archivo.txt local

```
 def node_callback(event, main_node, connected_node, data)
    try:
        #aquí se verifican eventos en nuestra red
        if event != 'node_request_to_stop': # node_request_to_stop does not have any connected_node, while it is the main_node that is stopping!
            if event=="node_message":
                solicitud=str(data)
                if "sumar" in solicitud:
                    global esfinal
                    if  esfinal==True:
                        numeros=solicitud.replace("sumar:","").split("-")
                        suma=0
                        for numero in numeros:
                            try:
                                suma+= int (numero)
                            except Exception as e:
                                suma=suma
                        print(suma)
                        esfinal=False
                    else:
                        
                        node.connect_with_node('127.0.0.1', 8002)
                        time.sleep(1)
                        
                        with open("F:/Documentos/Doceavo/Sistemas distribuidos/Suma_nodos/nodo1/numeros.txt", "r") as file:
                            for line in file:
                                solicitud=solicitud+line
                        for n in node.nodes_outbound:        
                            node.send_to_node(n,solicitud)}
```

El siguiente fragmento de código es el empleado para enviar el mensaje al nodo siguiente:

```node.send_to_node(n,enviar)```

# Ejecutando las pruebas ⚙️

# Vista previa ⌨️

A continuación, daremos a conocer la interfaz de programación de nuestra red peer to peer (P2P).
Específicamente, adición de registros (datos), suma de nodos y salir del programa. Esta interfaz utiliza varios parámetros del programa para administrar. 

![alt text](https://github.com/jhonnyrod/sisdistribuidos/blob/master/Ejemplo%20Peticion.png)


# Construido con 🛠️

- Visual Studio Code - Framework de modelado
- Python3 - Lenguaje de Programacion


# Autores ✒️

- Diana León 
- Jonathan Rodriguez
- Jeisson Guauta
