#  Este es el directorio de un entorno virtual


### activarlo
>> MockObjects\Scripts\activate

### desactivarlo
>> deactivate



## Un poco de data
Los tests unitarios son bastante utiles a la hora de analizar el codigo y chequear cada algunos cambios que no se nos rompa

Aunque los tests pueden ejecutarse normalmente fuera de un entorno virtual, nos brinda ciertos beneficios ejecutarlos dentro 
de los mismos.

- Aislamiento del entorno: El entorno virtual permite separar las dependencias y configuraciones específicas del proyecto, asegurando que las pruebas se ejecuten en un entorno controlado
y consistente. Esto evita posibles conflictos entre las dependencias de prueba y las del sistema.

- Reproducibilidad: Al ejecutar pruebas unitarias en un entorno virtual, se pueden recrear exactamente las mismas condiciones de prueba en diferentes máquinas o entornos de
desarrollo. Esto facilita la colaboración en nuestro equipo y la portabilidad del proyecto. Por ejemplo, al principio tuvimos problemas con los test, porque con el mismo codigo, a un
compañero los test le terminaban de forma correcta, y a otro de forma incorrecta.

- Facilidad de configuración: Configurar y mantener un entorno virtual es relativamente sencillo, y la verdad que mucho no lo tuvimos que usar. Pero las
herramientas de gestión de entornos virtuales, como virtualenv en Python, permiten instalar y gestionar las dependencias necesarias específicas para las pruebas, u alguna otra que solo
sirve para cierta version de python por ejemplo, lo cual no afecta el entorno global del sistema en si.

- Independencia de recursos externos: Se pueden simular y aislar recursos externos, como bases de datos, servicios web u otros sistemas, mediante el uso de mocks o stubs. Esto permite
ejecutar pruebas unitarias sin depender de la disponibilidad o accesibilidad de estos recursos externos. Esto tampoco lo usamos mucho, pero es bueno saberlo.

- Mayor confiabilidad: Los tests nos ayudan a identificar y solucionar errores en el código de forma temprana. Esto mejora la calidad del código y reduce la posibilidad de errores en
producción. La idea siempre es, si los tests simulan un posible codigo cliente, luego de hacer cambios, ejecutarlos para ver si responden de forma correcta, y si no es asi, analizar
si es necesario modificar esos cambios nuevos que se hicieron, o quizá hasta cambiar los tests, que quedaron viejos.

- Retroalimentación rápida: Verde bueno, rojo malo. Y la mejor parte de cuando te tira error, es el detalle sumamente especifico de en donde se encuentra el error. El arreglo es mucho
mas veloz y eficiente. Un debuggeo mas visual.
