Proyecto Django con Gráficas Dinámicas.
Materia : Estructura de Datos.
Alumna : Mariana Manzo Hernández.
Matricula : 20619254.
Fecha de entrega : 5 de diciembre de 2024.
Profesor : José Luis Robles Bárcenas. 
Grupo : SC05T.


Este proyecto permite visualizar gráficas dinámicas utilizando Django y Chart.js.


REQUISITOS PREVIOS

- Python 3.8 o superior instalado en el sistema. En este caso se utilizo Windows, ya que es el sistema operativo que tengo instalado en mi computadora.
- Virtualenv configurado para usar en Python. Este es opcional pero permite que las librerías que se instalen no afectan al resto de cosas que ya se tienen instaladas. Todo permanece solo en esa ventana.
- Git instalado para clonar el repositorio. Y por supuesto estar dado de alta con un usuario en GitHub, tanto para el desarrollo como para el uso final del proyecto.


INSTALACION Y USO DEL PROYECTO

1. Clonar el Repositorio
Descargar el proyecto desde GitHub con las siguientes líneas en una ventana de comandos (cmd) :
Es necesario estar en un directorio de trabaja fácil de identificar. (Por ejemplo d:\UNITEC)

git clone https://github.com/12345678910-star/graficas-django-marianamh.git
cd graficas-django-marianamh


2. Crear y Activar un Entorno Virtual (Opcional)
Es recomendable usar un entorno virtual para instalar las dependencias del proyecto:
Para crearlo en Windows, se usan las siguientes líneas.

python -m venv venv
.\venv\Scripts\activate


3. Instalar las Dependencias
Se debe ejecutar el siguiente comando para instalar las librerías necesarias:
Este archivo contiene todas las dependencias necesarias para el proyecto y es parte de los archivos clonados.

pip install -r requirements.txt



4. Ejecutar el Servidor
Ejecutar la siguientes líneas para inicia el servidor del proyecto:

python manage.py runserver



5. Verificar el Proyecto

En el navegador instalado acceder a la pagina "http://127.0.0.1:8000/" (sin comillas). Se deben de poder ver las gráficas dinámicas generadas por el proyecto.



TECNOLOGIAS UTILIZADAS EN ESTE PROYECTO

- Python : Como lenguaje de programacion
- Django : Como Framework
- Chart.js: Para visualización de gráficas dinámicas.
- GitHub : Como repositorio final para poner los archivos del proyecto en la nube
