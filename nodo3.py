import sys
import time
from p2pnetwork.node import Node

# node_callback
#  event         : event name
#  node          : the node (Node) that holds the node connections
#  connected_node: the node (NodeConnection) that is involved
#  data          : data that is send by the node (could be empty)
def node_callback(event, main_node, connected_node, data):
    try:
        if event != 'node_request_to_stop': # node_request_to_stop does not have any connected_node, while it is the main_node that is stopping!
            if event=="node_message":
                print("sirve")
                time.sleep(1)
                node.send_to_nodes("hola")

    except Exception as e:
        print(e)

# The main node that is able to make connections to other nodes
# and accept connections from other nodes on port 8001.
node = Node("127.0.0.1", 8003, node_callback)

# Do not forget to start it, it spins off a new thread!
node.start()
time.sleep(1)

# Connect to another node, otherwise you do not have any network.
node.connect_with_node('127.0.0.1', 8002)
time.sleep(2)
node.send_to_nodes("hola")

while True:
    try: 
        print("\n_____________BIENVENIDO___________\n"
        +"\n Ingrese el numero de la acción que desea realizar:"
        +"\n1. Agregar numero \n2.Sumar numero \n3. Salir")
            
        op = int(input(" \n : "))

        if op == 1:
            print("hilo 1")
        elif op == 2:
            numbers = []
            with open("numeros.txt", "r") as file:
                for line in file:
                    fields = line.split(",")
                    #print(line.rstrip("n"))
                subnumbers = (int(field) for field in fields)
                numbers.extend(subnumbers)
                suma = sum(numbers)
            print("\nLa suma es: "+str(suma))
        elif op == 3:
            node_2.stop()
            print('end')
            break
    except ValueError:
        print("Porfavor, ingresa solo numeros")

def enviar_men():
    node.send_to_nodes(5)