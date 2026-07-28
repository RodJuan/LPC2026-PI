import base64
import json

# ======================================================
# CONFIGURACIÓN DEL CONSENSO
# ======================================================

HORARIO_PRINCIPAL = "Mar_12-14"
HORARIO_RESPALDO = "Jue_10-12"

PESO_LOCAL = 1.0
PESO_FORANEO = 3.5


codigos = [
    "eyJuIjogIlJlYmVjYSBCYXJyaW9zICIsICJmIjogZmFsc2UsICJ2X3AiOiBbIk1hcl8xMi0xNCJdLCAidl9kIjogWyJNYXJfMTItMTQiXX0=",
    "eyJuIjogIkx1Y2lhbm8gUGFsZW5jaWEgIiwgImYiOiBmYWxzZSwgInZfcCI6IFsiTHVuXzEyLTE0IiwgIkx1bl8xNC0xNiIsICJNYXJfMTItMTQiLCAiTWFyXzE0LTE2IiwgIkp1ZV8xMi0xNCJdLCAidl9kIjogWyJMdW5fMTItMTQiLCAiTHVuXzE0LTE2IiwgIk1hcl8wOC0xMCJdfQ==",
    "eyJuIjogIlNhbWFudGhhIFBhcnJhIiwgImYiOiB0cnVlLCAidl9wIjogWyJMdW5fMTAtMTIiLCAiSnVlXzA4LTEwIl0sICJ2X2QiOiBbIkx1bl8xMC0xMiJdfQ==",
    "eyJuIjogIkFuZHJcdTAwZTlzIE1lbmRvemEgIiwgImYiOiB0cnVlLCAidl9wIjogWyJNYXJfMTItMTQiXSwgInZfZCI6IFsiTWFyXzEwLTEyIl19",
    "eyJuIjogIkVsaWV6ZXIgVmVsYXNxdWV6IiwgImYiOiBmYWxzZSwgInZfcCI6IFsiTHVuXzA4LTEwIiwgIkx1bl8xMC0xMiIsICJMdW5fMTItMTQiLCAiTHVuXzE0LTE2IiwgIk1pZV8wOC0xMCIsICJNaWVfMTAtMTIiLCAiTWllXzEyLTE0IiwgIk1pZV8xNC0xNiIsICJWaWVfMDgtMTAiLCAiVmllXzEwLTEyIiwgIlZpZV8xMi0xNCIsICJWaWVfMTQtMTYiXSwgInZfZCI6IFsiTWFyXzA4LTEwIiwgIk1hcl8xMC0xMiIsICJNYXJfMTItMTQiLCAiTWFyXzE0LTE2IiwgIkp1ZV8wOC0xMCIsICJKdWVfMTAtMTIiLCAiSnVlXzEyLTE0IiwgIkp1ZV8xNC0xNiJdfQ==",
    "eyJuIjogIllhcmlhbmEgT3JvemNvIiwgImYiOiBmYWxzZSwgInZfcCI6IFsiTHVuXzEyLTE0IiwgIkp1ZV8xMC0xMiJdLCAidl9kIjogWyJMdW5fMTItMTQiLCAiSnVlXzEyLTE0Il19",
    "eyJuIjogIkRlbmljZSBWaWxjaGV6ICIsICJmIjogdHJ1ZSwgInZfcCI6IFsiSnVlXzEwLTEyIl0sICJ2X2QiOiBbIkp1ZV8xMC0xMiJdfQ==",
    "eyJuIjogIkZyYW5jbyBKYWltZXMiLCAiZiI6IGZhbHNlLCAidl9wIjogWyJNYXJfMDgtMTAiLCAiTWFyXzEwLTEyIiwgIk1hcl8xMi0xNCIsICJNYXJfMTQtMTYiLCAiSnVlXzEyLTE0IiwgIlZpZV8wOC0xMCJdLCAidl9kIjogWyJNYXJfMTAtMTIiLCAiTWFyXzEyLTE0IiwgIk1hcl8xNC0xNiIsICJKdWVfMTItMTQiXX0=",
    "eyJuIjogIlphcmFoIEFsdmFyYWRvIiwgImYiOiBmYWxzZSwgInZfcCI6IFsiTWllXzE0LTE2IiwgIkp1ZV8xMC0xMiJdLCAidl9kIjogWyJNaWVfMTQtMTYiLCAiSnVlXzEwLTEyIl19",
    "eyJuIjogIkNlYnJpXHUwMGUxbiBJcmlhcnRlIiwgImYiOiBmYWxzZSwgInZfcCI6IFsiTWFyXzEyLTE0IiwgIk1hcl8xNC0xNiIsICJKdWVfMDgtMTAiLCAiSnVlXzEwLTEyIiwgIlZpZV8wOC0xMCIsICJWaWVfMTAtMTIiLCAiVmllXzEyLTE0IiwgIlZpZV8xNC0xNiJdLCAidl9kIjogWyJNYXJfMTQtMTYiLCAiSnVlXzA4LTEwIiwgIlZpZV8wOC0xMCJdfQ==",
    "eyJuIjogIlJvaW5lciBSb3NhcmlvICIsICJmIjogdHJ1ZSwgInZfcCI6IFsiTHVuXzEyLTE0IiwgIk1hcl8xMi0xNCJdLCAidl9kIjogW119",
    "eyJuIjogIk1hdXJvIE1lbGVhbiAiLCAiZiI6IGZhbHNlLCAidl9wIjogWyJNYXJfMDgtMTAiLCAiTWFyXzEwLTEyIiwgIk1pZV8xMC0xMiIsICJNaWVfMTItMTQiXSwgInZfZCI6IFsiTWllXzEwLTEyIiwgIk1pZV8xMi0xNCJdfQ==",
    "eyJuIjogIkplc1x1MDBmYXMgU3VcdTAwZTFyZXoiLCAiZiI6IGZhbHNlLCAidl9wIjogWyJMdW5fMTAtMTIiLCAiTHVuXzEyLTE0IiwgIk1hcl8wOC0xMCIsICJNYXJfMTAtMTIiLCAiTWFyXzEyLTE0IiwgIk1pZV8xMi0xNCIsICJKdWVfMTAtMTIiLCAiSnVlXzEyLTE0Il0sICJ2X2QiOiBbIkx1bl8xMC0xMiIsICJMdW5fMTItMTQiLCAiTWFyXzA4LTEwIiwgIk1hcl8xMC0xMiIsICJNYXJfMTItMTQiLCAiSnVlXzEwLTEyIiwgIkp1ZV8xMi0xNCJdfQ==",
    "eyJuIjogIkVmcmFpbiBBcnJpZWNoZSIsICJmIjogZmFsc2UsICJ2X3AiOiBbIkx1bl8xMC0xMiIsICJMdW5fMTItMTQiLCAiTHVuXzE0LTE2IiwgIk1hcl8wOC0xMCIsICJNYXJfMTAtMTIiLCAiTWFyXzEyLTE0IiwgIk1hcl8xNC0xNiIsICJKdWVfMTAtMTIiLCAiSnVlXzEyLTE0IiwgIkp1ZV8xNC0xNiJdLCAidl9kIjogWyJMdW5fMTAtMTIiLCAiSnVlXzEwLTEyIl19",
    "eyJuIjogIlJlYmVjYSBIZXJuYW5kZXogIiwgImYiOiBmYWxzZSwgInZfcCI6IFsiTWFyXzEyLTE0IiwgIkp1ZV8xMi0xNCJdLCAidl9kIjogWyJNYXJfMDgtMTAiLCAiSnVlXzEyLTE0Il19",
    "eyJuIjogIkFsdmVyaXMgRWRtdW5kbyBMXHUwMGYzcGV6IGx1Z28gIiwgImYiOiBmYWxzZSwgInYiOiBbIkx1bl8xMi0xNCIsICJNYXJfMTItMTQiLCAiTWllXzEyLTE0IiwgIkp1ZV8xMi0xNCIsICJWaWVfMTItMTQiXX0=",
    "eyJuIjogIkp1YW4gUmFtaXJleiAiLCAiZiI6IGZhbHNlLCAidl9wIjogWyJMdW5fMTItMTQiLCAiTWFyXzA4LTEwIl0sICJ2X2QiOiBbIk1pZV8xMi0xNCIsICJKdWVfMTItMTQiLCAiVmllXzEyLTE0Il19",
    "eyJuIjogIk1pcmFuZGEgTW9udGVybyAiLCAiZiI6IGZhbHNlLCAidl9wIjogWyJNYXJfMTAtMTIiLCAiTWllXzEwLTEyIiwgIkp1ZV8xMC0xMiIsICJWaWVfMTAtMTIiLCAiVmllXzEyLTE0Il0sICJ2X2QiOiBbIk1hcl8xMC0xMiIsICJNYXJfMTItMTQiLCAiTWllXzEwLTEyIiwgIlZpZV8xMC0xMiIsICJWaWVfMTItMTQiXX0="
]

# ======================================================
# PROCESAMIENTO
# ======================================================

estudiantes = []

for codigo in codigos:
    datos = json.loads(base64.b64decode(codigo).decode("utf-8"))

    horarios_data = []
    if "v" in datos:
        horarios_data = datos["v"]
    elif "v_p" in datos and "v_d" in datos:
        # Combine 'v_p' and 'v_d' if 'v' is not present
        horarios_data = list(set(datos["v_p"] + datos["v_d"])) # Use set to remove duplicates if any
    # If neither 'v' nor 'v_p'/'v_d' are present, horarios_data will remain empty,
    # which is consistent with no schedules being available for that student.

    estudiantes.append({
        "nombre": datos["n"],
        "foraneo": datos["f"],
        "horarios": horarios_data
    })

# ======================================================
# EVALUACIÓN
# ======================================================

peso_total = 0
peso_satisfecho = 0

satisfechos = []
insatisfechos = []

for alumno in estudiantes:

    peso = PESO_FORANEO if alumno["foraneo"] else PESO_LOCAL
    peso_total += peso

    disponible = (
        HORARIO_PRINCIPAL in alumno["horarios"] or
        HORARIO_RESPALDO in alumno["horarios"]
    )

    if disponible:
        peso_satisfecho += peso
        satisfechos.append(alumno["nombre"])
    else:
        insatisfechos.append(alumno["nombre"])

# ======================================================
# RESULTADOS
# ======================================================

porcentaje = 100 * peso_satisfecho / peso_total

print("="*60)
print("        RESULTADO DEL CONSENSO")
print("="*60)

print(f"Horario principal : {HORARIO_PRINCIPAL}")
print(f"Horario respaldo  : {HORARIO_RESPALDO}")
print(f"Peso local        : {PESO_LOCAL}")
print(f"Peso foráneo      : {PESO_FORANEO}")

print()

print(f"Estudiantes satisfechos : {len(satisfechos)}")
print(f"Estudiantes no cubiertos: {len(insatisfechos)}")

print()

print(f"Satisfacción ponderada: {porcentaje:.2f}%")

print("\n===== SATISFECHOS =====")
for nombre in satisfechos:
    print("✓", nombre)

print("\n===== NO CUBIERTOS =====")
for nombre in insatisfechos:
    print("✗", nombre)
import numpy as np
import matplotlib.pyplot as plt

# ======================================================
# DATOS DEL ESCENARIO SOLUCIONADO (Consenso Dual)
# ======================================================
# 15 cubiertos de 18 (12 locales y 3 foráneos)
# 3 no cubiertos (2 locales y 1 foráneo)
locales_totales = 14
foraneos_totales = 4
locales_cubiertos = 12
foraneos_cubiertos = 3

locales_fallidos = locales_totales - locales_cubiertos
foraneos_fallidos = foraneos_totales - foraneos_cubiertos

# Rango del Peso del Estudiante Foráneo (W_f)
w_f = np.linspace(1.0, 10.0, 200)

# Funciones evaluadas
u_total = -(locales_fallidos * 1.0 + foraneos_fallidos * w_f)
isn = ((locales_cubiertos * 1.0 + foraneos_cubiertos * w_f) /
       (locales_totales * 1.0 + foraneos_totales * w_f)) * 100

# ======================================================
# CONSTRUCCIÓN DE LA GRÁFICA (Estilo Requerido)
# ======================================================
fig, ax1 = plt.subplots(figsize=(10, 6), dpi=120)

# Eje Izquierdo: U_total (Teal / Verde Azulado)
color_u = '#128277' # Teal oscuro inspirado en tu referencia
ax1.set_xlabel('Peso del Estudiante Foráneo ($W_f$)', fontsize=12)
ax1.set_ylabel('$U_{total}$', color=color_u, fontsize=12, fontweight='bold')
line1 = ax1.plot(w_f, u_total, color=color_u, linewidth=2.5, label='$U_{total}$')
ax1.tick_params(axis='y', labelcolor=color_u)

# Cuadrícula base
ax1.grid(True, linestyle='--', alpha=0.5, color='lightgray')

# Eje Derecho: ISN (%) (Magenta / Fucsia)
ax2 = ax1.twinx()
color_isn = '#A01A7D' # Magenta punteado
ax2.set_ylabel('ISN (%)', color=color_isn, fontsize=12, fontweight='bold')
line2 = ax2.plot(w_f, isn, color=color_isn, linewidth=2.5, linestyle=':', label='ISN (%)')
ax2.tick_params(axis='y', labelcolor=color_isn)

# Límites del eje Y para mostrar el éxito (ISN alto)
ax2.set_ylim(0, 105)

# Línea vertical punteada en W_f = 1.0 (El punto óptimo)
ax1.axvline(x=1.0, color='gray', linestyle='--', alpha=0.7)

# Anotación con flecha negra
y_optimo = u_total[0] # El valor en W_f = 1.0
ax1.annotate('Óptimo: 1.0',
             xy=(1.0, y_optimo),
             xytext=(1.8, y_optimo),
             arrowprops=dict(facecolor='black', shrink=0.05, width=2, headwidth=8),
             fontsize=11,
             verticalalignment='center')

# Leyenda unificada en la esquina inferior derecha
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='lower right', framealpha=0.95, shadow=True, edgecolor='gray')

# Título de la gráfica
plt.title('Análisis de Consenso: $U_{total}$ vs ISN (%)', fontsize=14, fontweight='bold', pad=15)

plt.tight_layout()
plt.show()