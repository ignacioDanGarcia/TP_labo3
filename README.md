# TP_labo3

## Objetivos
### Objetivo General
El trabajo práctico tiene por objetivo garantizar que cada alumno/a, a través de la investigación y experimentación, transite por el proceso de diseñar e implementar un sistema complejo.
### Objetivos Particulares
#### Principal
Que los alumnos/as adquieran, mediante el desarrollo del trabajo práctico, una mejor comprensión de los temas que se analizan en la materia desde una perspectiva teórica.
#### Trabajo en equipo
Que los alumnos/as comprendan la importancia del trabajo en equipo para llevar adelante un proyecto. Los alumnos/as deberán conformar equipos de 4 integrantes.
#### Técnicas y herramientas
Que los alumnos/as comiencen a utilizar, o incrementen sus conocimientos sobre, técnicas y herramientas de desarrollo de software actualmente utilizadas en la industria.

## Forma de entrega y evaluación
El trabajo práctico debe estar versionado en un repositorio de código (github o gitlab).
El trabajo práctico será evaluado tanto en forma grupal como en forma individual. Para lograr esto, cada equipo debe realizar una presentación grupal del trabajo, para lo cual deberán presentar el mencionado repositorio con el código y documentación de la solución. En lo que respecta a la evaluación individual, se evaluarán los aportes de cada integrante del equipo dentro del repositorio. En caso de que alguno de los integrantes del grupo no demuestre haberse comprometido con el trabajo grupal se le realizará un coloquio en el que deberá defender la solución propuesta.
El trabajo práctico constará de puntos de control en fechas específicas y una entrega final.
#### Punto de control 1 - 20/04/2023
- Diseño tentativo de la solución. La presentación debe hacer énfasis en los diagramas de componentes, clase, secuencia, etc.
#### Punto de control 2 - 04/05/2023
- Diseño de la solución actualizado.
- Código que acompaña el diseño planteado (repositorio)
- Test unitarios que permitan probar la funcionalidad implementada.
#### Punto de control 3 - 18/05/2023 - Etapa 1 completa
- Diseño de la solución actualizado.
- Código que acompaña el diseño planteado (repositorio)
- Test unitarios que permitan probar la funcionalidad implementada.
#### Punto de control 4 - 01/06/2023
- Diseño de la solución actualizado con cambios solicitados en la segunda etapa del trabajo práctico.
#### Entrega final - 15/06/2022 en adelante
- Diseño de la solución actualizado.
- Código que acompaña el diseño planteado (repositorio)
- Test unitarios que permitan probar la funcionalidad implementada.



# INFORMACIÓN

## Introducción
Una empresa que se dedica al transporte de containers desea desarrollar una aplicación que le permita gestionar su negocio. La empresa cuenta con una flota de barcos y camiones que le permiten transportar los mencionados containers entre distintos paises donde la empresa posee sedes.

## Requerimientos del sistema
Como se mencionó en la sección anterior, el objetivo de la empresa es obtener una aplicación que le permita gestionar el traslado de containers alrededor del mundo.
La empresa cuenta con una flota de barcos de distintas características, que le permiten transportar distintos tipos de containers. Por ejemplo, posee barcos que sólo pueden transportar containers básicos, mientras que otros barcos mas especializados permiten transportar containers de mayor tamaño, con contenido especial, etc.

### Barcos
La empresa posee dentro de su flota de barcos, 2 tipos de barcos. Por un lado posee barcos que sólo pueden transportar containers de tipo básico y barcos que pueden transportar cualquier tipo de container. Cada barco posee un identificador único, también define la cantidad maxima de containers que puede transportar y el peso máximo que soporta.
Todos los barcos poseen una estructura especializada que permite organizar, asegurar y transportar los contenedores. En el caso de los barcos de tipo básico, dicha estructura sólo está diseñada para soportar contenedores cuyas dimensiones coincidan con las de un contenedor de tipo básico; mientras que en el caso de los barcos especializados dicha estructura permite transportar cualquier tipo de contenedor cuyas medidas sean superiores a las de un contenedor básico.

### Camiones
La mayoría de los clientes de la empresa, retiran la mercadería por el puerto, una vez que el container es descargado del barco que lo transporta. Para aquellos clientes que no poseen transporte propio, la empresa ofrece el servicio de entrega en puerta, por lo que la empresa cuenta con una flota de 5 camiones. Este servicio tiene un costo fijo de $20000 por viaje realizado.
> Un camión sólo puede transportar 1 container a la vez. 

### Contenedores
En general un contenedor tiene un identificador único, mediante el cual la empresa consigue mantener la trazabilidad del mismo. A su vez, la empresa destina ciertos containers para el transporte de materiales especiales como puede ser explosivos, desechos químicos o radioactivos.
Cada contenedor define un precio base que se debe pagar para transportar una determinada carga en el mismo, a esto debe sumarse el precio que se debe pagar por la carga en sí misma. Ver el apartado de precios más adelante.

#### Básico
El contenedor Básico estándar también conocido como contenedor de 20 pies, es el contenedor más usados a nivel mundial en el transporte marítimo de mercancías. El contenedor estándar se diferencia de otros modelos de contenedor principalmente en que está cerrado herméticamente y no cuenta con sistemas de refrigeración o ventilación, como es el caso de los contenedores refrigerados o ventilados. 


Dimensiones del contenedor        | Ancho[m] | Alto[m]  | Largo[m] |
------------- | -------------
Exterior   | 2.45 | 2.6 | 6.1
Interior  | 2.35 | 2.3 | 6.0

Peso y Volumen soportado        | Peso max[Kg] | Volumen[m3]
------------- | -------------
   | 24000 | 32.6

#### Básico HC (High Cube)
El contenedor Básico HC, también conocido como contenedor de 40 pies, es idéntico al contenedor básico pero con mayores dimensiones, volumen y kilos soportados.

Dimensiones del contenedor        | Ancho[m] | Alto[m]  | Largo[m] |
------------- | -------------
Exterior   | 2.45 | 2.6 | 12.1
Interior  | 2.35 | 2.3 | 12.0

Peso y Volumen soportado        | Peso max[Kg] | Volumen[m3]
------------- | -------------
   | 32500 | 67.7


#### Flat Rack
Los contenedores flat rack están diseñados para dar cabida a todas aquellas cargas cuyas medidas, distribución de los bultos o peso no permiten su transporte en contenedores estándar Los flat rack están hechos de planchas de metal que se ajustan a una estructura estándar de 20 o 40 pies. Los laterales son abatibles y no disponen de techo o parte superior. Esto los hace adecuados para el transporte de: 
>Mercancías muy pesadas que deben ser cargadas en el contenedor con grúas o equipamientos especializados. Un ejemplo típico de mercancías transportadas en flat rack son las de la industria de la maquinaria.

>Mercancías con una altura superior a la de un contenedor de 20 o 40 pies High Cube o con volúmenes muy irregulares, como vehículos industriales o tuberías.

Dimensiones del contenedor        | Ancho[m] | Alto[m]  | Largo[m] |
------------- | -------------
Exterior   | N/A | 2.3 | 6.1
Interior  | N/A | 2.3 | 6.0

Peso y Volumen soportado        | Peso max[Kg] | Volumen[m3]
------------- | -------------
   | 45000 | 33

                
----
### Reglas de Negocio

1. Un barco no puede cargar más containers del máximo definido 
2. Un barco no puede cargar más peso del máximo definido 
3. Un barco no puede cargar un container para el cual no fue diseñado. 
4. Un container con material especial (explosivos, desechos químicos o radioactivos) sólo puede ser transportado por un barco diseñado para tal fin. 
5. Cualquier carga cuyas dimensiones, volumen o peso supere lo definido en el container no podrá ser trasladada en el mismo. 
6. Un contenedor sin características especiales no puede transportar material 





## Cosas que nos faltan
- [x] Punto control 1
    - [x] Diagrama
- [ ] Punto control 2
    - [ ] Codigo base
    - [ ] MockObjects base
- [ ] Punto control 3
    - [ ] Codigo
    - [ ] MockObjects
- [ ] Punto control 4 (2da Etapa)
    - [ ] Codigo nuevo
    - [ ] MockObjects nuevos
- [ ] Punto control 5
    - [ ] Codigo final
    - [ ] MockObjects finales
- [ ] Entregado
