r# vehicle-data-analysis
# Análisis de Datos de Vehículos
En el proyecto anterior se crearoon varios archivos en forma local y despues se subieron al github para despues cargar los
datos en el render para ver el archivo app.py como una pagina web, antes de subir los archivos se probaron de forma local para
corroborar que la pagina cargaba correctamente.

## Descripción del Proyecto
Esta aplicación web interactiva permite hacer un grafico de dispersion o un histograma con los datos de vehicles_us.csv que contiene
datos de mas de 51000 automoviles, con loas siguientes columnas: price(precio), model_year(año del automovil), condition(el estado del automovil, buena, como nueva, ...etc), cyliders(cilindrada), fuel(combustible con el que funciona), odometer( cantidad de km/mill que tiene el automovil, transmission (tipo de transmision), type(tipo de auto, pick up, sedan,etc),paint_color(color de pintura), is_4wd( si es 4wd: traccion en las 4 ruedas, dated_posted( dia publicado), day_listed( dias listados o dias
en la lista o pagina web).
Lo que se pretendia con este proyecto es hacer una pagina web basica de forma local, despues subir los archivo a github y al final cargar 
el archivo app.py para ver la pagina wen en linea, suena muy facil pero lleva muchos pasos y aplicaciones que se deben de usar, a persar de
eso se pudo terminar el proyecto con lo requerimentos que se nos pedian.

## Funcionalidades

- Visualización de histogramas: se crea un boton que toma todos los datos del archivo vehicles_us.csv y los grafica en un histograma,
  para poder visualizar los de forma mas facil y ver patrones.
  
- Creación de gráficos de dispersión: se crea un boton que toma los datos del archivo vehicles_us.csv y los grafico de dispersion,
  para poder visualizar los de forma mas facil y ver patrones.
  
- Análisis interactivo de datos
  
  Los datos son mas 51000 automoviles los cuales hay muchas marcas, tipos y precios, lo mas importante para este proyecto es
  el odometro( cantidad de km/millas de cada automovil, por lo que podemos graficar los datos para ver la cantidad de automoviles
  con mas o menos km/millas que han recorrido, ya que al comprar un automovil es importante los datos de cada columna, es tambien
  un dato valioso saber cuantos km/millas tiene un automovil antes de comprarlo, ya que un automovil con muchos km/millas va estar mas desgastado
  que uno con menos, pero esto es solo un punto que se debe analizar antes de adquirir un automovil.

EL grafico de histograma asi como el de dispersion tienen varias opciones como: bajar la imagen, zoom, pan, full screen entre otros por lo que se puiede interactuar
con el grafico, para ver los datos mas facil y hacer un analisis, tambien al pasar la flecha del mouse encima de cada linea se pueden ver los datos.
  

## Cómo usar la aplicación

La app se abre desde la pagina y sale un mensaje con la cantidad de filas y columnas del archivo csv de los automoviles, tambien se pueden ver dos botones los cuales solo uno sirve a la
vez, o sea si le doy al click boton de Construir histograma o al de construir grafico dispersion, se va a desplegar un grafico abajo de ese boton, si toco el otro boton que no habia
tocado se despliega el otro grafico abajo del boton, puede durar unos milisegundos.


Links: 

https://vehicle-data-analysis-1.onrender.com/
https://github.com/IsmaelArtavia/vehicle-data-analysis
