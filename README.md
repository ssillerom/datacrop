# datacrop
Team Datacrop Development

- Requisitos previos:

Tener instalado Kit de desarrollo de Java mayor o igual a la versión 8 para que pueda arrancar h2o y usar AutoML

Como ejecutar la plataforma en local con Anaconda:

1. Abrir Anaconda Prompt e ir a la raiz del directorio donde se encuentra el environment.ynl

Crear tu propio entorno con todas las dependencias instaladas a través de Anaconda:

conda env create -n datacrop21 -f environment.yml

2. Activar el nuevo entorno:

conda activate datacrop21

3. Ejecutar la plataforma en local, una vez instalada las librerías se deberá ejecutar:

streamlit run app.py

Esperar unos segundos a que se ejecute el nodo de h2o...

una vez iniciado todo podrá acceder a la platforma a través de:

localhost:8501 o 127.0.0.1:8501

Usuario: Cajamar Contraseña: Datacrop21