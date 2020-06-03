import sys
import time
import p2pnetwork


from config_nodo import nodop2p

nodo_1 = nodop2p("127.0.0.1", 8002)
time.sleep(1)
nodo_1.start()
time.sleep(1)
nodo_1.connect_with_node('127.0.0.1', 8003)
time.sleep(5)
respuesta=nodo_1.send_to_nodes("sumar")
print(respuesta)

def iniciar_nodo ():
    

    # Connect with another node, otherwise you do not create any network!
    

    # Example of sending a message to the nodes.
    nodo_1.send_to_nodes({"message": "Hi there!"})

    time.sleep(5) # Create here your main loop of the application
    i=0


    

def recibirM ():
    time.sleep(7)
    mensaje = nodo_1.node_message(self,data)
    print (mensaje)
    

if __name__ == '__main__':
    # Lanzamos un hilo
    iniciar_nodo