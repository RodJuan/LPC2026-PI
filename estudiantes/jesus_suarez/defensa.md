Informe Breve

el programa tenia como problemática la selección del mejor horario de clases de la materia LPC, siendo en sí un problema del tipo problema de 
consenso, teniendo como corazón de objetivo la alineación de un sistema efectivo y moral, por tanto asumimos que por disponibilidad y costos de
transporte entre otros, los fóraneos tienen igual o mayor peso de voto que los demás, y para observar que genera mejores resultados iteramos el
valor de voto de los fóraneos y tomamos el bloque horario con los dos mayores índices de las métricas que creamos para representar la efectividad
del sistema.

Por tanto respondiendo a las preguntas.
¿Cuál es el bloque horario que el algoritmo seleccionó como el consenso definitivo para la sección?
el horario ganador indiscutible es el Martes de 12:00 a 14:00.

Al correr la simulación, la curva de Satisfacción (ISN) se queda completamente plana en el tiempo.
¿Por qué crees que ocurre esto al analizar los datos reales de tus compañeros?

Esto sucede porque la estructura del código introduce los tokens de todos los estudiantes y obtiene númericamente el bloque horario 
más efectivo mediante la métrica U total, a su vez, se itera el valor Wf para determinar Si U Total puede mejorarse o al menos 
observar su comportamiento en función de Wf. En cada uno de todos los bloques e iteraciones de los distintos valores de wf, el ganador
siempre es el bloque Martes de 12:00 a 14:00.
Por tanto, el Isn se mantiene plano en el tiempo porque siempre se itera bajo el mismo bloque, es decir, Isn no está en función de wf,
sino del bloque, y al bloque nunca cambiar se mantiene constante en la gráfica.

Jesús Suárez
33435025
Física



