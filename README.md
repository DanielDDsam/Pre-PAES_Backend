# Backend Pre-PAES
#Daniel Duran-Cristian Aguilera
## Creado a partir de la versión inicial a cargo de Daniel Duran - José Olivar - Luis Romero - Bryan Ramírez en Taller de ingeniería de software

Para que el proyecto funcione debe realizar ciertos pasos antes de clonar el repositorio.

Primeramente, tener instalado Python en su versión 3.11.3.

En segunda instancia, debe instalar MySQL Workbench y MySQL Server en su versión 8.0.30 o superior, para poder crear el esquema de la base de datos, tambien en su defecto puede instalar postgresql junto a pg admin en su versión 16.1.

Seguidamente debe clonar el repositorio, luego debe dirigirse a la carpeta en la que fue descargado y abrirlo con su IDE, y debe escribir los siguientes comandos en la terminal

```py -m venv venv``` o ```python -m venv venv```

Si usa VSC (Visual Studio code) apretar f1 y escribir "interpreter, escoger la opción Python 3.11.3 ('venv':venv), luego cerrar la consola y volver a abrir la terminal en command prompt (CMD), en caso de que no lo detecte automáticamente debe seleccionarlo manualmente en la carpeta venv/scripts

Si ocupa PyCharm debe ver que su interprete sea seleccionado en su versión de Python3 y también utilizar command prompt (cmd).

Siguiendo este paso escribir el siguiente comando para instalar las dependencias desde el archivo requirements.txt

```pip install -r requirements.txt```

En settings.py que está dentro de la carpeta backend se debe encontrar esta parte

```python
   DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'proyecto_web',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '3306'
        }
    }
```

Aquí debe incluir la contraseña de su base de datos en la key, su usuario y su puerto según el administrador de base de datos que tenga instalado 

``` 'PASSWORD': 'Aquí poner su contraseña'
    'PORT': 'Aquí ingresar el puerto a utilizar'
``` 

Cuando ya se tenga la contraseña, en MySQL Workbench o pgAdmin debe crear un schema con este nombre "proyecto_web", al tener creado el esquema, debe ir a su IDE y escribir el siguiente comando

```py manage.py migrate```

Este comando creara la base de datos con sus tablas a través del ORM de Django.

Para poblar las tablas de la base de datos es necesario ocupar el siguiente comando.

```py manage.py shell < Scripts/main.py```

Nota: Si utiliza la terminal de PowerShell deberá habilitar la ejecución de scripts.

Luego de esto escribir el siguiente comando para inicializar el servidor.

```py manage.py runserver```




