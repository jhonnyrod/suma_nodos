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
                        
                        node.connect_with_node('127.0.0.1', 8003)
                        time.sleep(1)
                        
                        with open("F:/Documentos/Doceavo/Sistemas distribuidos/Suma_nodos/nodo2/numeros.txt", "r") as file:
                            for line in file:
                                solicitud=solicitud+line
                        for n in node.nodes_outbound:        
                            node.send_to_node(n,solicitud)
                        
                        
                

    except Exception as e:
        print(e)

# The main node that is able to make connections to other nodes
# and accept connections from other nodes on port 8001.
node = Node("127.0.0.1", 8002, node_callback)

# Do not forget to start it, it spins off a new thread!
node.start()
time.sleep(1)




#crear txt
txt = open("F:/Documentos/Doceavo/Sistemas distribuidos/Suma_nodos/nodo2/numeros.txt","w")
txt.close()

while True:
    try: 
        print("\nMenu\n1. insertar número \n2.hacer suma de nodos \n3. Salir")
            
        opc = int(input(" \nQué desea realizar?: "))

        if opc == 1:
            num = input("\nEscriba el numero que desea agregar  ")
            txt = open("F:/Documentos/Doceavo/Sistemas distribuidos/Suma_nodos/nodo2/numeros.txt","a")#Creando txt con la información del cliente
            txt.write("{}-".format(num))
            txt.close()
        elif opc == 2:
            numbers = []
            
            node.connect_with_node('127.0.0.1', 8003)
            time.sleep(1)
            print(node)
            with open("F:/Documentos/Doceavo/Sistemas distribuidos/Suma_nodos/nodo2/numeros.txt", "r") as file:
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

def enviar_men():
    node.send_to_nodes(5)
