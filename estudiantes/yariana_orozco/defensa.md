# 🏛️ Informe de Defensa: Optimización de Horarios y Consenso Colectivo v3.0

**Estudiante:** [Yariana Orozco]  
**Asignación:** Nro. 1 - Matriz de Vulnerabilidad Socio-Geográfica  

---

## 📊 1. Análisis de la Curva de Satisfacción ($ISN$)

### Pregunta de la Guía:
*Al correr la simulación, la curva de Satisfacción ($ISN$) se queda completamente plana en el tiempo. ¿Por qué crees que ocurre esto al analizar los datos reales de tus compañeros?*

### Respuesta Analítica:
Este fenómeno ocurre debido a la naturaleza matemática diferenciada de ambas métricas y a la distribución de las restricciones reales del grupo:

1. **Unidades de Medida Distintas:** El Bienestar General ($U_{total}$) es un indicador macro-ponderado que se ve directamente afectado por el factor de peso político ($W_f$). Cada vez que $W_f$ aumenta, la utilidad de los bloques donde asisten estudiantes foráneos se multiplica de manera exponencial.
2. **Estabilización del Bloque Óptimo:** En la recolección de datos reales de la sección, el algoritmo identificó rápidamente los puntos de conflicto. Al inicio, la mayoría local impone el bloque **"Mie 10-12"**, pero al incrementar el peso de la minoría foránea para evitar penalizaciones críticas de exclusión (de $-1.5 \times W_f$), el sistema realiza una transición definitiva hacia el bloque **"Jue 12-14"**.
3. **Naturaleza del $ISN$:** El Índice de Satisfacción Neta ($ISN$) es una métrica puramente democrática y demográfica basada en **unidades físicas de personas** ($\text{Alumnos}$). Una vez que el algoritmo se estabiliza en el bloque de protección foránea (**Jue 12-14**), el conjunto de alumnos que asiste y que desea ese horario ya no varía, sin importar que el peso simbólico de los foráneos siga subiendo de $4.0$ a $10.0$. Como las cabezas físicas conformes siguen siendo las mismas, la proporción matemática se congela, generando una línea recta horizontal y plana en el $100\%$.

---

## 🏛️ 2. Determinación del Consenso Definitivo

### Pregunta de la Guía:
*¿Cuál es el bloque horario que el algoritmo seleccionó como el consenso definitivo para la sección?*

### Respuesta Analítica:
El algoritmo de optimización determinó los siguientes escenarios para nuestra sección:

* **Consenso Inicial (Democracia Pura, $W_f = 1.0$):** El bloque seleccionado fue **Miércoles de 10:00 a 12:00 (`Mie 10-12`)**. En este escenario, la densidad de la mayoría local domina la función de utilidad social, ignorando los costos de traslado de las zonas foráneas.
* **Consenso Definitivo (Protección de Minorías, $W_f = 10.0$):** El bloque óptimo final seleccionado por el sistema fue **Jueves de 12:00 a 14:00 (`Jue 12-14`)**. 

**Conclusión del Modelo:** El bloque **Jueves 12-14** se consolida como el consenso definitivo de equidad para la sección. Al aplicar la *Matriz de Vulnerabilidad Socio-Geográfica v3.0*, este horario es el único capaz de neutralizar las penalizaciones drásticas por exclusión geográfica y logística de los estudiantes con mayores dificultades de transporte y compromisos laborales, alcanzando un equilibrio justo y un Índice de Satisfacción Neta óptimo.

---

## 🖼️ 3. Evidencia Gráfica del Sistema

El comportamiento matemático descrito en este informe se encuentra respaldado de manera visual en el archivo independiente `grafica_consenso.png` adjunto en este directorio, cumpliendo con las especificaciones técnicas requeridas de doble eje coordenado.
