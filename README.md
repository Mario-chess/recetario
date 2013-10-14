ACTIVIDADES DE FINDE SEMANA - 13/10/2013

* Se realizo un programa de Recetario,siguiendo la guia de Maestros del Web.

* Se investigó y descargo un video de Mejorandola, para aprender la manera en que se debe trabajar con Github.

	- Hay dos cosas importantes. Primero es necesario tener na llave ssh, la cual se encarga de conectar un equipo determinado con Github, y segundo, antes de realizar el push, por lo general se debe realizar un pull.

* Una vez que se aprendió a usar correctamente Github, se procedió a buscar un servidor para cargar una Aplicacion realizada en Django, se comenzo intentando con AllwaysData, que realmente no vale la pena, al menos en la version gratuita (perdida de tiempo). Luego se encontro un server realmente muy interesante y flexible...Pythonanywhere, se aprendió a crear una nueva app, me di cuenta que es mucho mejor crearla de manera manual, ya que se tiene más control, sobretodo si se comienza a crear la carpeta de virtualenv, en la cual podemos instalar todo lo que se requiera. 

https://www.pythonanywhere.com/wiki/DjangoTutorial

https://www.pythonanywhere.com/wiki/VirtualEnvForNewerDjango


Una vez configurado el proyecto se procedio con la clonacion del Proyecto desde el repositorio de Github, lo cual agilizo las cosas, pero aun faltaban hacer algunos cambios importantes antes de iniciar.

* Primero, surgieron problemas con el ckeditor, por lo cual se lo quito.

* Luego el manejo de rutas fue un dolor de cabeza, ya que se deben a manejar rutas absolutas, lo cual significo un cambio en varias partes del settings.py.

* Una vez solucionada eso, el sistema corria con normalidad, pero los estilos y demás, es decir el STATIC_URL no se reconociá, es ahi donde me demore y finalmente me di cuenta que habia que agregar esta ruta desde la interfaz del Server.

* Finalmente el proyecto corre al igual que en mi PC de desarrollo.

Nota: 
* Es necesario limitar el tamaño de las imagenes, ya que se tarda demasiado en cargar...

* Nota: Es necesario optimizar para hacer todo mas veloz.
