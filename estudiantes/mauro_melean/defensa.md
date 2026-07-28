Mauro Melean
C.I 33913326
Facultad experimental de ciencias
Lenguaje de programación científica

Defensa del problema de consenso

1. Planteamiento del problema:
El objetivo de este proyecto fue encontrar un horario de clases que beneficiara al mayor número posible de estudiantes. Sin embargo, no todos cuentan con la misma disponibilidad, por lo que resulta imposible elegir un horario que satisfaga al 100 % del grupo.
Ante esta situación, el problema se abordó como un problema de optimización del consenso, buscando una solución que maximizara la satisfacción estudiantil y, al mismo tiempo, minimizara el sacrificio que implica asistir a clases.

2. Recolección y procesamiento de datos:
Para obtener información objetiva, se desarrolló un script que permitió a cada estudiante registrar sus horarios de mayor disponibilidad y preferencia.
Cada respuesta fue almacenada mediante un código codificado, el cual posteriormente fue procesado por un programa desarrollado en Python. Este programa decodificó automáticamente la información para analizar la disponibilidad de todos los estudiantes de forma uniforme y sin realizar cálculos manuales.

3. Clasificación de los estudiantes:
Con el fin de representar de manera más justa la realidad del grupo, los estudiantes fueron clasificados en dos categorías:
Estudiantes foráneos.
Estudiantes locales.
Esta clasificación no busca dividir al grupo, sino reconocer que el estudiante foráneo suele realizar un mayor esfuerzo para asistir a clases, ya sea por tiempo de traslado, costos de transporte u otras dificultades asociadas.
4. Sistema de ponderación de votos:
En lugar de considerar que todos los votos tienen el mismo impacto, se implementó un sistema de ponderación:
Peso del voto local: 1
Peso del voto foráneo: 3.5
Este valor fue seleccionado como un punto de equilibrio que reconoce el esfuerzo adicional de los estudiantes foráneos sin dejar de considerar la opinión de los estudiantes locales.
De esta manera, el modelo busca encontrar horarios que reduzcan el sacrificio estudiantil y aumenten el bienestar colectivo.

5. Desarrollo del algoritmo:
Se desarrolló un script en Python capaz de realizar automáticamente las siguientes tareas:
Decodificar los votos de todos los estudiantes.
Identificar la disponibilidad registrada por cada uno.
Evaluar si un estudiante puede asistir al horario principal o al horario de respaldo.
Calcular automáticamente la satisfacción ponderada obtenida con la solución propuesta.
Este procedimiento garantiza que todos los estudiantes sean evaluados bajo el mismo criterio, haciendo que el proceso sea transparente, reproducible y libre de errores derivados de cálculos manuales.

6. Solución obtenida:
Después de analizar las diferentes alternativas, el algoritmo determinó que la combinación que ofrece el mejor nivel de consenso es la siguiente:
Horario principal: Martes de 12:00 a 14:00.
Horario de respaldo: Jueves de 10:00 a 12:00.
Esta combinación representa la mejor alternativa encontrada dentro de las restricciones existentes, ya que permite aumentar la cantidad de estudiantes que pueden asistir y reduce el sacrificio requerido para participar en las clases.

7. Resultados:
Con esta propuesta, el modelo alcanzó una satisfacción ponderada aproximada entre el 80 % y el 83 %.
Aunque este resultado no representa un consenso absoluto, demuestra que es posible maximizar el bienestar colectivo utilizando un criterio objetivo basado en la disponibilidad expresada por los propios estudiantes.
8. Conclusión
La solución propuesta consiste en establecer un horario principal los martes de 12:00 a 14:00 y un horario de respaldo los jueves de 10:00 a 12:00.
El horario de respaldo no sustituye la clase principal, sino que funciona como una alternativa para aquellos estudiantes que, por motivos de disponibilidad, no puedan asistir al horario principal. Su propósito es servir como un espacio de apoyo o repaso que permita disminuir el impacto de los conflictos de horario.

En conclusión, este proyecto demuestra que un problema cotidiano puede resolverse mediante el uso de programación, análisis de datos y un sistema de votación ponderada, permitiendo tomar decisiones fundamentadas que buscan maximizar el bienestar colectivo y ofrecer una solución más equitativa para el grupo estudiantil.