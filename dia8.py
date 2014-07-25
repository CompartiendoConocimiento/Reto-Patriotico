<<<<<<< HEAD
SoundCloud es una plataforma de distribución de audio 
on-line en la que sus usuarios pueden colaborar, promocionar
y distribuir sus proyectos musicales.


Objetivo de éste reto.

1.- Adentrarnos en el consumo de API 
2.- familiarizarnos con el uso de las mismas
3.- aprender haciendo.

El reto del dia de hoy consiste en consumir la API publica que 
proporciona SoundCloud.

pasos para realizar el reto.

paso 1: crearse una cuenta en:
        soundcloud.com
paso 2: crear una aplicacion para poder usar la API, en este enlace
        http://soundcloud.com/you/apps/

paso 3: pip install soundcloud
paso 4: crear un archivo dia7.py y dentro de este archivo escribir.
        import soundcloud

        client = soundcloud.Client(client_id='YOUR_CLIENT_ID')
        tracks = client.get('/tracks', limit=10)
		for track in tracks:
    		print track.title
		app = client.get('/apps/124')
		print app.permalink_url


enviar el resultado.

para poder participar enviarnos un correo electronico a 

concurso@compartiendoconocimiento.com

en asunto: RETO PATRIOTICO

Importante: indicarnos su cuenta de faceboob para poder mantenernos en contacto.
=======
Introducir dos numeros por teclado. Imprimir los numeros que hay entre ellos 
comenzando por el mas pequeno. Contar cuantos hay y cuantos de ellos son 
pares. Calcular la suma de los pares


para poder participar del concurso enviar su archivo "*.py" al siguiente correo
concurso@compartiendoconocimiento.com

indicando en asunto RETO PATRIOTICO

Importante: indicar su nombre y su cuenta de FB para podernos comunicar












>>>>>>> origin/master
