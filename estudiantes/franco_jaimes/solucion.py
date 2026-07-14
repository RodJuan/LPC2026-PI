import base64
import json
import matplotlib.pyplot as plt
import numpy as np

# ------------------------------------------------------------
# 1. TOKENS (pegados directamente desde el enunciado)
# ------------------------------------------------------------
tokens_b64 = [
    "eyJuIjogIk1pcmFuZGEgTW9udGVybyAiLCAiZiI6IGZhbHNlLCAidl9wIjogWyJNYXJfMTAtMTIiLCAiTWllXzEwLTEyIiwgIkp1ZV8xMC0xMiIsICJWaWVfMTAtMTIiLCAiVmllXzEyLTE0Il0sICJ2X2QiOiBbIk1hcl8xMC0xMiIsICJNYXJfMTItMTQiLCAiTWllXzEwLTEyIiwgIlZpZV8xMC0xMiIsICJWaWVfMTItMTQiXX0=",
    "eyJuIjogIkp1YW4gUmFtaXJleiAiLCAiZiI6IGZhbHNlLCAidl9wIjogWyJMdW5fMTItMTQiLCAiTWFyXzA4LTEwIl0sICJ2X2QiOiBbIk1pZV8xMi0xNCIsICJKdWVfMTItMTQiLCAiVmllXzEyLTE0Il19",
    "eyJuIjogIkFsdmVyaXMgRWRtdW5kbyBMXHUwMGYzcGV6IGx1Z28gIiwgImYiOiBmYWxzZSwgInYiOiBbIkx1bl8xMi0xNCIsICJNYXJfMTItMTQiLCAiTWllXzEyLTE0IiwgIkp1ZV8xMi0xNCIsICJWaWVfMTItMTQiXX0=",
    "eyJuIjogIlJlYmVjYSBIZXJuYW5kZXogIiwgImYiOiBmYWxzZSwgInZfcCI6IFsiTWFyXzEyLTE0IiwgIkp1ZV8xMi0xNCJdLCAidl9kIjogWyJNYXJfMDgtMTAiLCAiSnVlXzEyLTE0Il19",
    "eyJuIjogIkVmcmFpbiBBcnJpZWNoZSIsICJmIjogZmFsc2UsICJ2X3AiOiBbIkx1bl8xMC0xMiIsICJMdW5fMTItMTQiLCAiTHVuXzE0LTE2IiwgIk1hcl8wOC0xMCIsICJNYXJfMTAtMTIiLCAiTWFyXzEyLTE0IiwgIk1hcl8xNC0xNiIsICJKdWVfMTAtMTIiLCAiSnVlXzEyLTE0IiwgIkp1ZV8xNC0xNiJdLCAidl9kIjogWyJMdW5fMTAtMTIiLCAiSnVlXzEwLTEyIl19",
    "eyJuIjogIkplc1x1MDBmYXMgU3VcdTAwZTFyZXoiLCAiZiI6IGZhbHNlLCAidl9wIjogWyJMdW5fMTAtMTIiLCAiTHVuXzEyLTE0IiwgIk1hcl8wOC0xMCIsICJNYXJfMTAtMTIiLCAiTWFyXzEyLTE0IiwgIk1pZV8xMi0xNCIsICJKdWVfMTAtMTIiLCAiSnVlXzEyLTE0Il0sICJ2X2QiOiBbIkx1bl8xMC0xMiIsICJMdW5fMTItMTQiLCAiTWFyXzA4LTEwIiwgIk1hcl8xMC0xMiIsICJNYXJfMTItMTQiLCAiSnVlXzEwLTEyIiwgIkp1ZV8xMi0xNCJdfQ==",
    "eyJuIjogIk1hdXJvIE1lbGVhbiAiLCAiZiI6IGZhbHNlLCAidl9wIjogWyJNYXJfMDgtMTAiLCAiTWFyXzEwLTEyIiwgIk1pZV8xMC0xMiIsICJNaWVfMTItMTQiXSwgInZfZCI6IFsiTWllXzEwLTEyIiwgIk1pZV8xMi0xNCJdfQ==",
    "eyJuIjogIlJvaW5lciBSb3NhcmlvICIsICJmIjogdHJ1ZSwgInZfcCI6IFsiTHVuXzEyLTE0IiwgIk1hcl8xMi0xNCJdLCAidl9kIjogW119",
    "eyJuIjogIkNlYnJpXHUwMGUxbiBJcmlhcnRlIiwgImYiOiBmYWxzZSwgInZfcCI6IFsiTWFyXzEyLTE0IiwgIk1hcl8xNC0xNiIsICJKdWVfMDgtMTAiLCAiSnVlXzEwLTEyIiwgIlZpZV8wOC0xMCIsICJWaWVfMTAtMTIiLCAiVmllXzEyLTE0IiwgIlZpZV8xNC0xNiJdLCAidl9kIjogWyJNYXJfMTQtMTYiLCAiSnVlXzA4LTEwIiwgIlZpZV8wOC0xMCJdfQ==",
    "eyJuIjogIlphcmFoIEFsdmFyYWRvIiwgImYiOiBmYWxzZSwgInZfcCI6IFsiTWllXzE0LTE2IiwgIkp1ZV8xMC0xMiJdLCAidl9kIjogWyJNaWVfMTQtMTYiLCAiSnVlXzEwLTEyIl19",
    "eyJuIjogIkZyYW5jbyBKYWltZXMiLCAiZiI6IGZhbHNlLCAidl9wIjogWyJNYXJfMDgtMTAiLCAiTWFyXzEwLTEyIiwgIk1hcl8xMi0xNCIsICJNYXJfMTQtMTYiLCAiSnVlXzEyLTE0IiwgIlZpZV8wOC0xMCJdLCAidl9kIjogWyJNYXJfMTAtMTIiLCAiTWFyXzEyLTE0IiwgIk1hcl8xNC0xNiIsICJKdWVfMTItMTQiXX0=",
    "eyJuIjogIkRlbmljZSBWaWxjaGV6ICIsICJmIjogdHJ1ZSwgInZfcCI6IFsiSnVlXzEwLTEyIl0sICJ2X2QiOiBbIkp1ZV8xMC0xMiJdfQ==",
    "eyJuIjogIllhcmlhbmEgT3JvemNvIiwgImYiOiBmYWxzZSwgInZfcCI6IFsiTHVuXzEyLTE0IiwgIkp1ZV8xMC0xMiJdLCAidl9kIjogWyJMdW5fMTItMTQiLCAiSnVlXzEyLTE0Il19",
    "eyJuIjogIkVsaWV6ZXIgVmVsYXNxdWV6IiwgImYiOiBmYWxzZSwgInZfcCI6IFsiTHVuXzA4LTEwIiwgIkx1bl8xMC0xMiIsICJMdW5fMTItMTQiLCAiTHVuXzE0LTE2IiwgIk1pZV8wOC0xMCIsICJNaWVfMTAtMTIiLCAiTWllXzEyLTE0IiwgIk1pZV8xNC0xNiIsICJWaWVfMDgtMTAiLCAiVmllXzEwLTEyIiwgIlZpZV8xMi0xNCIsICJWaWVfMTQtMTYiXSwgInZfZCI6IFsiTWFyXzA4LTEwIiwgIk1hcl8xMC0xMiIsICJNYXJfMTItMTQiLCAiTWFyXzE0LTE2IiwgIkp1ZV8wOC0xMCIsICJKdWVfMTAtMTIiLCAiSnVlXzEyLTE0IiwgIkp1ZV8xNC0xNiJdfQ==",
    "eyJuIjogIkFuZHJcdTAwZTlzIE1lbmRvemEgIiwgImYiOiB0cnVlLCAidl9wIjogWyJNYXJfMTItMTQiXSwgInZfZCI6IFsiTWFyXzEwLTEyIl19",
    "eyJuIjogIlNhbWFudGhhIFBhcnJhIiwgImYiOiB0cnVlLCAidl9wIjogWyJMdW5fMTAtMTIiLCAiSnVlXzA4LTEwIl0sICJ2X2QiOiBbIkx1bl8xMC0xMiJdfQ==",
    "eyJuIjogIkx1Y2lhbm8gUGFsZW5jaWEgIiwgImYiOiBmYWxzZSwgInZfcCI6IFsiTHVuXzEyLTE0IiwgIkx1bl8xNC0xNiIsICJNYXJfMTItMTQiLCAiTWFyXzE0LTE2IiwgIkp1ZV8xMi0xNCJdLCAidl9kIjogWyJMdW5fMTItMTQiLCAiTHVuXzE0LTE2IiwgIk1hcl8wOC0xMCJdfQ==",
    "eyJuIjogIlJlYmVjYSBCYXJyaW9zICIsICJmIjogZmFsc2UsICJ2X3AiOiBbIk1hcl8xMi0xNCJdLCAidl9kIjogWyJNYXJfMTItMTQiXX0="
]

# ------------------------------------------------------------
# 2. FUNCIONES DE DECODIFICACIÓN SEGURA
# ------------------------------------------------------------
def decodificar_estudiante(token_b64):
    """Decodifica un token Base64 a diccionario, manejando errores."""
    try:
        json_str = base64.b64decode(token_b64).decode('utf-8')
        datos = json.loads(json_str)
        # Normalizar: si no existe "v_p" pero sí "v", usar "v" como disponibilidad y dejar v_p vacío
        if "v_p" not in datos and "v" in datos:
            datos["v_p"] = []
            datos["v_d"] = datos.pop("v")
        # Asegurar que existan v_p y v_d (si no, listas vacías)
        datos.setdefault("v_p", [])
        datos.setdefault("v_d", [])
        return datos
    except Exception as e:
        print(f"Error decodificando token: {e}")
        return None

# ------------------------------------------------------------
# 3. CARGA DE ESTUDIANTES
# ------------------------------------------------------------
estudiantes = []
for i, token in enumerate(tokens_b64):
    est = decodificar_estudiante(token)
    if est:
        estudiantes.append(est)
    else:
        print(f"Token {i+1} ignorado por error.")

print(f"Estudiantes cargados: {len(estudiantes)}")

# ------------------------------------------------------------
# 4. DEFINICIÓN DE BLOQUES HORARIOS
# ------------------------------------------------------------
dias = ["Lun", "Mar", "Mie", "Jue", "Vie"]
horas = ["08-10", "10-12", "12-14", "14-16"]
bloques = [f"{dia}_{hora}" for dia in dias for hora in horas]  # 20 bloques

# ------------------------------------------------------------
# 5. FUNCIONES DE EVALUACIÓN
# ------------------------------------------------------------
def puntaje_estudiante(estudiante, bloque, peso_foraneo_actual):
    """Calcula el puntaje ponderado de un estudiante para un bloque."""
    # Determinar peso
    peso = peso_foraneo_actual if estudiante["f"] else 1.0
    # ¿Puede asistir?
    if bloque in estudiante["v_d"]:
        puntos = 1.0
        if bloque in estudiante["v_p"]:   # además lo quiere
            puntos += 0.5
    else:
        puntos = -1.5
    return puntos * peso

def calcular_U_y_ISN(bloque, peso_foraneo):
    """Devuelve (U_total, ISN) para un bloque con el peso dado."""
    U = 0.0
    pueden = 0
    quieren = 0
    for est in estudiantes:
        puntos = puntaje_estudiante(est, bloque, peso_foraneo)
        U += puntos
        # Para el ISN necesitamos los datos sin ponderar
        if bloque in est["v_d"]:
            pueden += 1
            if bloque in est["v_p"]:
                quieren += 1
    ISN = (quieren / pueden * 100) if pueden > 0 else 0.0
    return U, ISN

# ------------------------------------------------------------
# 6. SIMULACIÓN PRINCIPAL
# ------------------------------------------------------------
pesos = np.arange(1.0, 10.05, 0.1)   # 1.0 a 10.0 paso 0.1
mejores_bloques = []
U_ganadores = []
ISN_ganadores = []

for w in pesos:
    mejor_bloque = None
    mejor_U = -float('inf')
    mejor_ISN = 0.0
    for bloque in bloques:
        U, isn = calcular_U_y_ISN(bloque, w)
        if U > mejor_U:
            mejor_U = U
            mejor_bloque = bloque
            mejor_ISN = isn
        # Si hay empate, nos quedamos con el primero (no se especifica desempate)
    mejores_bloques.append(mejor_bloque)
    U_ganadores.append(mejor_U)
    ISN_ganadores.append(mejor_ISN)

# Mostrar el bloque que más veces fue seleccionado (consenso definitivo)
from collections import Counter
frecuencia = Counter(mejores_bloques)
bloque_final = frecuencia.most_common(1)[0][0]
print(f"\nBloque horario que más veces resultó ganador: {bloque_final}")

# ------------------------------------------------------------
# 7. GRÁFICA BIFOCAL
# ------------------------------------------------------------
fig, ax1 = plt.subplots(figsize=(10, 6))

color_U = 'indigo'
ax1.set_xlabel('Peso del foráneo ($W_f$)')
ax1.set_ylabel('Bienestar General ($U_{total}$)', color=color_U)
ax1.plot(pesos, U_ganadores, color=color_U, linewidth=2, label='$U_{total}$ (Utilidad)')
ax1.tick_params(axis='y', labelcolor=color_U)
ax1.grid(True, alpha=0.3)

# Eje Y derecho para ISN
ax2 = ax1.twinx()
color_ISN = 'orange'
ax2.set_ylabel('Índice de Satisfacción Neta ($ISN$ %)', color=color_ISN)
ax2.plot(pesos, ISN_ganadores, color=color_ISN, linestyle='dashed', linewidth=2, label='$ISN$ (Satisfacción)')
ax2.tick_params(axis='y', labelcolor=color_ISN)
ax2.set_ylim(0, 100)

# Leyenda unificada abajo a la derecha
lineas1, etiquetas1 = ax1.get_legend_handles_labels()
lineas2, etiquetas2 = ax2.get_legend_handles_labels()
ax1.legend(lineas1 + lineas2, etiquetas1 + etiquetas2, loc='lower right')

plt.title('Simulación de consenso horario: $U_{total}$ e $ISN$ vs $W_f$')
plt.tight_layout()
plt.savefig('grafica_consenso.png', dpi=150)
plt.show()
print("Gráfica guardada como grafica_consenso.png")