# Peer-to-peer

El término sistema peer-to-peer (P2P) abarca un amplio conjunto de aplicaciones distribuidas que permiten compartir recursos informáticos mediante el intercambio directo entre sistemas. El objetivo de un sistema P2P es agregar recursos disponibles en el borde de Internet y compartirlos de manera cooperativa entre los usuarios.

# ¿Qué es "Register"?🚀

Este proyecto tiene como objetivo diseñar e implementar una arquitectura para obtener recursos de un modo distribuido basada en nodos.
Un nodo es un proceso que realiza básicamente dos funciones: cargar número y solicitar suma por parte de otros nodos de la red.



# Modelado 📖

A continuación, podemos evidenciar un grupo de máquinas que están dispuestas en forma de un anillo para actuar como un servidor distribuido. Este grupo de máquinas se funcionará para proporcionar un mejor equilibrio de carga y una mayor disponibilidad.


<img align="Center" src="https://github.com/jhonnyrod/suma_nodos/blob/master/Modelado%20Peer-to-peer.jpeg">

# Pre-requisitos 📋

Para la elaboración de este proyecto fue necesario utilizar una librería de Python llamada p2p networking.

Es una librería de red simplificada para construir redes punto a punto en Python. Esta librería fue diseñada para resolver el problema de encontrar nodos y evitar los NAT para que pueda concentrarse en escribir el código de su aplicación.

+ Reenvío de puertos automatizados.
+ Soporte para perforación de agujeros TCP / apertura simultánea.
+ Conexión inversa (dígale a un nodo que se conecte a usted).




Se realizó la instalación de la librería a través de CMD utilizando el siguiente comando:

pip install p2pnetwork



# Instalación 🔧


    
Luego Clonar el proyecto

	git clone https://github.com/jhonnyrod/sisdistribuidos

# Codigo ⚙️

Clase init.py
```
!/usr/bin/env python
import web
import json
from collections import Counter

urls = (
    '/index/', 'index'
)

class index:
    def POST(self):
        # How to obtain the name key and then print the value?
        web.header('Content-Type', 'application/json')
        data = web.data()
        my_json = data.decode('utf8').replace("'", '"')
        res=json.loads(my_json)
        print(Counter(res["direccion1"]))
        if (res["direccion1"].isalnum() and res["direccion2"].isalnum() and (len(res["direccion1"]) == 64) and (len(res["direccion2"]) == 64)):
            comp=True
        else:
            comp=False
        resp= json.dumps({"direccion1":res["direccion1"], "direccion2": res["direccion2"],"monto":res["monto"], "comprobador":comp})      
        return resp

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
```

# Ejecutando las pruebas ⚙️

# Vista previa ⌨️

![alt text](https://github.com/jhonnyrod/sisdistribuidos/blob/master/Ejemplo%20Peticion.png)


# Construido con 🛠️

- Eclipse - Framework de modelado
- POSTMAN - (Pruebas) Envío de peticiones HTTP REST
- Python3 - Lenguaje de Programacion


# Autores ✒️

- Diana León 
- Jonathan Rodriguez
- Jeisson Guauta
