INFORME DE ANALISIS - RENDIMIENTO.

-- Descripción del experimento realizado

El experimento consistió en evaluar y comparar el rendimiento temporal de dos estructuras de datos distintas en Python: una lista nativa y un array de la librería NumPy. Para ello, se estableció un volumen significativo de información consistente en $1.000.000 de elementos numéricos. A ambas estructuras se les aplicó la misma operación matemática básica (sumar el valor 5 a cada elemento), midiendo el tiempo exacto en segundos mediante la librería time


-- Resultados obtenidos en la medición del rendimiento

A partir de la ejecución del código, se midió el tiempo que tardó cada estructura en completar la operación sobre el millón de elementos:

* Tiempo con lista:Se ejecutó mediante una comprensión de lista iterando elemento por elemento.

* Tiempo con array de NumPy: Se ejecutó mediante una operación vectorizada directa.

* Resultado comparativo: El array de NumPy demostró una velocidad de procesamiento drásticamente superior en comparación con la lista nativa de Python.



-- Análisis comparativo entre listas y arrays

* Listas nativas: Almacenan referencias a objetos dispersos en la memoria y dependen de un bucle interpretado por Python para realizar operaciones, lo que incrementa la sobrecarga de procesamiento a medida que el volumen de datos aumenta.

* Arrays de NumPy: Almacenan datos homogéneos en bloques de memoria contiguos y ejecutan operaciones vectorizadas a bajo nivel (en lenguaje C), optimizando de forma radical el rendimiento y el uso de recursos del sistema.



-- Respuestas: 


* *¿Qué diferencias observas en el tiempo de ejecución al realizar la misma operación con una lista y con un array, y a qué crees que se deben esas diferencias?

Se observa que el array completa la operación en una fracción mínima del tiempo que le toma a la lista. Esto ocurre porque la lista procesa los datos mediante un bucle iterativo interpretado, mientras que el array aplica la operación de forma masiva y directa mediante vectorización nativa.


* ¿Cómo influye la forma en que cada estructura almacena los datos en memoria en el rendimiento obtenido durante la ejecución?

Las listas guardan punteros a objetos en ubicaciones de memoria separadas, lo que obliga al procesador a realizar saltos constantes. En contraste, los arrays de NumPy guardan los datos en bloques de memoria contiguos, facilitando un acceso sumamente eficiente y rápido.


* Si tuvieras que elegir una de estas estructuras para procesar grandes volúmenes de datos numéricos, ¿cuál seleccionarías y por qué?

Seleccionaría el array, ya que está diseñado específicamente para optimizar el rendimiento y el uso de recursos al gestionar conjuntos grandes de valores numéricos.