# Defensa — Asignación 1: Optimización de Horarios y Consenso Colectivo
**Autor:** Cebrián Iriarte  
**Fecha:** 2026-07-14

---

## 1. ¿Por qué la curva de ISN permanece completamente plana?

Al correr la simulación, el **Índice de Satisfacción Neta (ISN)** se mantiene constante en **30 %** durante todo el recorrido de $W_f$ (de 1.0 a 10.0). Esto ocurre por dos razones que se refuerzan mutuamente:

### a) El bloque ganador nunca cambia

La función de Bienestar General $U_{total}$ está diseñada para penalizar muy fuertemente la **exclusión** (−1.5 por estudiante que no puede asistir). Como el bloque **`Mar_12-14`** es el único que logra que la cantidad de estudiantes que *pueden* asistir sea suficientemente grande para compensar las penalizaciones, este bloque termina siendo el ganador **en cada uno de los 91 pasos** de la simulación.

Ni aumentar el peso $W_f$ cambia esta situación: los estudiantes foráneos que votaron son **Samantha Parra**, **Andrés Mendoza**, **Denice Vilchez** y **Roiner Rosario**. De esos cuatro, tanto Andrés Mendoza como Roiner Rosario tienen disponibilidad en `Mar_12-14`, lo que impide que ningún otro bloque los supere aunque se les amplifique su influencia.

### b) El ISN mide personas, no pesos políticos

El ISN se calcula como:

$$ISN = \frac{\text{Alumnos que pueden asistir Y quieren ese bloque}}{\text{Total de alumnos que pueden asistir}} \times 100\%$$

Esta fórmula es **una proporción de personas reales**, no ponderada por $W_f$. Entonces:

- En `Mar_12-14`, exactamente **3 de 10 estudiantes** que pueden asistir lo tenían en su lista de deseo (`v_d`): Rebeca Barrios, Andrés Mendoza y Franco Jaimes.  
- Esa razón es siempre 3/10 = **30 %**, sin importar cuánto valga $W_f$.

En resumen: **el bloque ganador es siempre el mismo**, y **el ISN del bloque ganador no depende de $W_f$**, por lo que la curva es una línea horizontal perfecta.

---

## 2. ¿Cuál es el bloque de consenso definitivo?

El algoritmo seleccionó como consenso definitivo el bloque:

> ### **Martes de 12:00 a 14:00 (`Mar_12-14`)**

Este bloque obtuvo el mayor $U_{total}$ en todas las iteraciones de la simulación. A continuación, algunas razones que explican su victoria:

| Razón | Detalle |
|-------|---------|
| **Alta disponibilidad** | Es el bloque con mayor número de estudiantes que declararon poder asistir (10 de 18), incluyendo estudiantes con muchas restricciones horarias como Rebeca Barrios y Rebeca Hernández. |
| **Cobertura de foráneos** | Andrés Mendoza y Roiner Rosario (ambos foráneos) tienen disponibilidad en este bloque, lo que evita que sus penalizaciones (−1.5 × $W_f$) destruyan el puntaje total. |
| **Balance penalización-recompensa** | Aunque 8 estudiantes no pueden asistir (acumulando penalizaciones), los 10 que sí pueden generan suficientes puntos positivos para mantener la delantera. |

Conforme $W_f$ aumenta, el $U_{total}$ de `Mar_12-14` **desciende linealmente** porque los foráneos que no pueden asistir (Samantha Parra y Denice Vilchez) generan penalizaciones cada vez mayores (−1.5 × $W_f$). Sin embargo, **ningún otro bloque logra superarlo** porque todos los demás bloques también sufren penalizaciones más grandes de los foráneos que excluyen.
