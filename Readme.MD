# Comandos para crear un proyecto de django

* Creación de un virtual environment:
  * python -m venv venv
  * Iniciamos el entorno: venv\Scripts\activate
  * Instalamos django: pip install django
  * actualizamos pip: python.exe -m pip install --upgrade pip

* Creación de un proyecto de django:
  * django-admin startproject nombre-proyecto

* Librerías:
  * python-dotenv: Librería que usamos para cargar las variables del .env file en nuestro sistema de Django

* Comandos para llevar un proyecto de un PC a otro:
  * pip freeze > requirements.txt
  * pip install -r requirements.txt
  
* Comandos en Django:
  * python manage.py startapp nombre-de-la-app

  * Migraciones:
    * python manage.py makemigrations
    * python manage.py migrate
    * python .\manage.py runserver -> correr django
    * python .\manage.py createsuperuser -> Crear un usuario admin




Acceso a servidor:
  * Conexión: ssh dam2@212.227.250.87
  * Contraseña: x85FMQ3r8c

  * ssh -L 5432:127.0.0.1:5432 dam2@212.227.250.87

  * comando: psql -U primernombre_primerapellido_dam -d primernombre_primerapellido_dam_db -W
  * contraseña: primernombre_primerapellido_dam1234



