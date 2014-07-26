# Reto Patriotico Dia 9 - PYTROPOLITANO

En la ciudad de Lima es muy comun usar el servicio de transporte metropolitano.
Jorge desea consultar de forma sencilla cuanto fue su consumo mensual
en el metropolitano sin necesidad de ir a su [pagina web](http://www.metropolitano.com.pe/index.php/consultas/tarjetas).
Para ello necesita ingresar su numero de tarjeta y un codigo de seguridad de 4
digitos generado en la misma web.

## Problema

Realizar un script en python que genere la siguiente interacción:

```bash
$ python main.py
>> Ingrese Nro. de Tarjeta:
1183026686

V A L I D A C I O N E S
===============
Service Fecha/Hora            Estación/Ruta Alim.   Monto (S/.)
TRONCAL 2014-06-30  17:09:00  Honorio Delgado       1.00
TRONCAL 2014-06-30  15:48:00  EspaÃ±a               1.00
TRONCAL 2014-06-27  21:37:00  Uni                   1.00
TRONCAL 2014-06-27  13:24:00  EspaÃ±a               1.00
TRONCAL 2014-06-25  16:39:00  Honorio Delgado       1.00
TRONCAL 2014-06-25  11:54:00  EspaÃ±a               1.00
TRONCAL 2014-06-24  20:53:00  Honorio Delgado       1.00
TRONCAL 2014-06-24  09:25:00  EspaÃ±a               1.00
TRONCAL 2014-06-23  14:11:00  EspaÃ±a               1.00
TRONCAL 2014-06-22  13:12:00  Tomas Valle           2.00
TRONCAL 2014-06-22  11:59:00  EspaÃ±a               2.00
TRONCAL 2014-06-21  17:45:00  Tomas Valle           1.00
TRONCAL 2014-06-21  16:36:00  EspaÃ±a               1.00
TRONCAL 2014-06-20  21:21:00  Uni                   1.00
TRONCAL 2014-06-20  16:13:00  EspaÃ±a               1.00

R E C A R G A S
===============
Operación Punto             Fecha/Hora            Monto (S/.)
Recarga   EspaÃ±a           2013-10-31 16:13:00   2.00
Recarga   EspaÃ±a           2013-10-29 14:20:00   2.00
Recarga   Uni               2013-10-28 19:24:00   1.00
Recarga   Estacion Central  2013-10-28 11:27:00   1.00
Recarga   EspaÃ±a           2013-10-25 16:05:00   2.00
Recarga   EspaÃ±a           2013-10-24 14:45:00   2.00
Recarga   EspaÃ±a           2013-10-23 16:24:00   2.00
Recarga   EspaÃ±a           2013-10-22 15:43:00   1.00
Recarga   2 de Mayo         2013-10-16 13:48:00   5.00
Recarga   Uni               2013-10-11 18:13:00   2.00
Recarga   Colmena           2013-10-10 17:23:00   1.00
Recarga   Espa?             2013-10-10 15:14:00   5.00
Recarga   Uni               2013-10-07 15:43:00   5.00
Recarga   Espa±a            2013-10-07 15:09:00   2.00
Recarga   Espa±a            2013-10-05 10:16:00   5.00
```

## Hints

Revise las siguientes webs:

+ Para encontrar el código de seguridad busque el siguiente string 
***id="txtcondicion">*** en la siguiente web:
www.metropolitano.com.pe/webmetro/new/prueba/consulta_prueba.php

+ Realize un post al siguiente url con los siguientes parámetros:
www.metropolitano.com.pe/webmetro/new/prueba/validaciones_recargas.php
```python
param = {
    'tarjeta': card_id,
    'txt': security_code,
}
```

+ Otras urls:
www.metropolitano.com.pe/webmetro/new/prueba/busca_itinerario.php

+ Puede usar la libreria requests, urllib, urllib2, etc.
```bash
# Para usar requests...
# http://docs.python-requests.org/en/latest/
$ pip install requests
```

+ No olvide mantener la sesión viva mientras realiza los métodos http 
necesarios.