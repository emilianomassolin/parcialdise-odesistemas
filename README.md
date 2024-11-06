# parcialdise-odesistemas
## Pasos para ejecutar el programa
### 1
Crear entorno virtual: python3 -m venv nombre del entorno
activar el entorno virtual:source nombre del entorno/bin/activate
### 2
Instalar las dependencias: pip install -r requirements.txt
### 3
Ejecutar el  siguiente comando: python3 inicio.py
### 4
Abrir postman y abrir el archivo que se encuentra en la carpeta collection
### 5
En Postman, selecciona el  POST para enviar una secuencia de ADN y verifica si es mutante. Ingresa una secuencia de dna en el body de la solicitud y envíala.
Para obtener estadísticas, selecciona el request GET en Postman para ver el número de mutantes y no mutantes registrados en la base de datos.
URL del postman : http://10.0.0.161:5000/
### render
## Para realizar un post:
colocar la siguiente url en postman 
https://parcialdise-odesistemas.onrender.com/mutant/
## Para realizar un get de las estadisticas 
colocar la siguiente url en postman
https://parcialdise-odesistemas.onrender.com/stats/