import sys
import time
import p2pnetwork

from p2pnetwork import Node


node = Node("127.0.0.1", 8001, node_callback)
time.sleep(1)

# Do not forget to start your node!
node.start()
time.sleep(1)

# Connect with another node, otherwise you do not create any network!
node.connect_with_node('127.0.0.1', 8002)
time.sleep(2)

# Example of sending a message to the nodes.
node.send_to_nodes({"message": "Hi there!"})

time.sleep(5) # Create here your main loop of the application

node.stop()