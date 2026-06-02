# defensa.md

1. ¿Por qué la curva de Satisfacción (ISN) se queda completamente plana?
   
Al observar la gráfica, la línea punteada naranja del ISN se mantiene horizontal
en exactamente 42.9 % durante toda la simulación, desde Wf = 1.0 hasta Wf = 1.5.

Esto ocurre porque el bloque ganador es siempre el mismo: Jue_12-14 gana en
los 11 pasos de la simulación sin excepción. Como el algoritmo nunca cambia de
bloque, el grupo de estudiantes que puede asistir a ese horario es idéntico en
cada iteración, y también lo es el subgrupo que además lo tenía como preferencia.

Al dividir siempre los mismos números, el ISN produce siempre el mismo porcentaje.
En otras palabras: la línea plana es evidencia de estabilidad. Con un peso justo
de máximo 1.5, los foráneos no tienen suficiente influencia para desplazar el
consenso hacia otro bloque, y por eso la satisfacción no salta ni cae en ningún
momento de la simulación.


2. Bloque horario seleccionado como consenso definitivo

El algoritmo seleccionó Jue_12-14 — Jueves de 12:00 a 14:00 como el
consenso definitivo de la sección.

Este bloque obtuvo el Utotal más alto en toda la simulación: −8.00 con
Wf = 1.0, bajando gradualmente hasta −11.00 con Wf = 1.5. La tendencia
descendente de la curva índigo se explica porque Roiner Rosario es foráneo y
no tiene disponibilidad en ningún bloque, por lo que su penalización de −1.5
se multiplica por Wf y pesa más a medida que el peso foráneo sube — arrastrando
el Utotal hacia abajo en todos los bloques por igual, sin cambiar cuál es el
mejor.

A pesar de que el Utotal es negativo en todo el rango, Jue_12-14 es
consistentemente el menos negativo de los 20 bloques evaluados, lo que lo
convierte en la opción que minimiza la exclusión y maximiza el bienestar
colectivo de la sección.
