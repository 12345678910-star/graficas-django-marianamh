Proyecto Django con Gráficas Dinámicas
Materia : Estructura de Datos
Alumna : Mariana Manzo Hernández
Matricula : 20619254
Fecha de entrega : 5 de diciembre de 2024
Profesor : José Luis Robles Bárcenas 
Grupo : SC05T


Este proyecto permite visualizar gráficas dinámicas utilizando Django y Chart.js.


REQUISITOS PREVIOS

- Python 3.8 o superior instalado en tu sistema.

- Virtualenv configurado (opcional pero recomendado).

- Git instalado para clonar el repositorio.



INSTALACION Y USO



1. Clonar el Repositorio

Descarga el proyecto desde GitHub:



git clone https://github.com/12345678910-star/graficas-django-marianamh.git

cd graficas-django-marianamh



2. Crear y Activar un Entorno Virtual (Opcional)

Es recomendable usar un entorno virtual para instalar las dependencias:



python -m venv venv

# En Windows: 
.\venv\Scripts\activate



3. Instalar las Dependencias

Ejecuta el siguiente comando para instalar las librerías necesarias:



pip install -r requirements.txt



4. Aplicar Migraciones

Configura la base de datos aplicando las migraciones incluidas en el proyecto:



python manage.py migrate



5. Ejecutar el Servidor

Inicia el servidor de desarrollo:



python manage.py runserver



6. Verificar el Proyecto

Abre tu navegador y accede a `http://127.0.0.1:8000/`. Deberías poder ver las gráficas dinámicas generadas por el proyecto.




TECNOLOGIAS UTILIZADAS EN ESTE PROYECTO

- Django : Como Framework

- Chart.js: Para visualización de gráficas dinámicas.

