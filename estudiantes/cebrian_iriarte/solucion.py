"""
Asignación 1: Optimización de Horarios y Consenso Colectivo
Autor: Cebrián Iriarte
Fecha: 2026-07-14

Script que procesa tokens de disponibilidad en Base64 y simula cómo varía
la selección del bloque horario óptimo al aumentar el peso de los estudiantes
foráneos (W_f) de 1.0 a 10.0 con pasos de 0.1.

Métricas calculadas:
  - U_total: Bienestar General del bloque horario seleccionado.
  - ISN: Índice de Satisfacción Neta (% de asistentes que obtuvieron su "quiero").
"""

import base64
import json
import matplotlib
matplotlib.use('Agg')  # Backend sin pantalla para guardar sin mostrar
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import os

# =============================================================================
# 1. DATOS DE ENTRADA: Tokens Base64 de los estudiantes de la sección
# =============================================================================

votes = [
    "eyJuIjogIlJlYmVjYSBCYXJyaW9zICIsICJmIjogZmFsc2UsICJ2X3AiOiBbIk1hcl8xMi0xNCJdLCAidl9kIjogWyJNYXJfMTItMTQiXX0",
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

# =============================================================================
# 2. DECODIFICACIÓN SEGURA: Base64 → JSON, con manejo de errores
# =============================================================================

estudiantes = []
print(">>> Decodificando tokens de los estudiantes...")
for i, token in enumerate(votes):
    try:
        # Agregar padding '=' si hace falta (Base64 sin padding estándar)
        padding = len(token) % 4
        if padding:
            token += '=' * (4 - padding)
        decoded_bytes = base64.b64decode(token)
        data = json.loads(decoded_bytes.decode('utf-8'))
        estudiantes.append(data)
        print(f"  [{i:02d}] OK {data.get('n', 'Desconocido').strip()} "
              f"({'Foraneo' if data.get('f', False) else 'Local'})")
    except Exception as e:
        print(f"  [{i:02d}] ERROR al decodificar token: {e}")

print(f"\n  Total decodificados: {len(estudiantes)} de {len(votes)}\n")

# =============================================================================
# 3. DEFINICIÓN DE BLOQUES HORARIOS (Lunes a Viernes, 08-10 hasta 14-16)
# =============================================================================

dias   = ['Lun', 'Mar', 'Mie', 'Jue', 'Vie']
franjas = ['08-10', '10-12', '12-14', '14-16']
bloques = [f"{d}_{f}" for d in dias for f in franjas]  # 20 bloques en total

# =============================================================================
# 4. FUNCIÓN: Puntaje individual de un estudiante para un bloque dado
# =============================================================================

def puntaje_estudiante(estudiante, bloque):
    """
    Calcula el puntaje bruto de un estudiante para un bloque horario.

    Reglas (antes de aplicar el peso político):
      - Puede asistir Y quiere el bloque (está en v_d): +1.5
      - Puede asistir pero NO quiere (no está en v_d): +1.0
      - NO puede asistir (no está en v_p ni en v): -1.5

    Nota: algunos tokens usan la clave 'v' en lugar de 'v_p'.
    Se usa 'v_p' con fallback a 'v'. Si ninguno existe, lista vacía.
    """
    puede  = estudiante.get('v_p', estudiante.get('v', []))
    quiere = estudiante.get('v_d', [])

    if bloque in puede:
        if bloque in quiere:
            return 1.5   # Puede Y quiere: bono de preferencia incluido
        else:
            return 1.0   # Puede, pero no es su preferencia declarada
    else:
        return -1.5      # No puede asistir: penalización por exclusión

# =============================================================================
# 5. SIMULACIÓN: W_f de 1.0 a 10.0 con pasos de 0.1
# =============================================================================

print(">>> Iniciando simulacion de pesos del foraneo (W_f = 1.0 a 10.0)...")

pesos_wf          = [round(1.0 + i * 0.1, 1) for i in range(91)]  # [1.0, 1.1, ..., 10.0]
lista_u           = []   # U_total del bloque ganador en cada paso
lista_isn         = []   # ISN (%) del bloque ganador en cada paso
bloques_ganadores = []   # Bloque seleccionado en cada paso

for w_f in pesos_wf:
    mejor_bloque = None
    mejor_u      = -float('inf')
    mejor_isn    = 0.0

    for bloque in bloques:
        u_total          = 0.0
        pueden_asistir   = 0   # Estudiantes que SI pueden ir
        quieren_y_pueden = 0   # Estudiantes que pueden ir Y quieren ese bloque

        for est in estudiantes:
            bruto = puntaje_estudiante(est, bloque)
            peso  = w_f if est.get('f', False) else 1.0
            u_total += bruto * peso

            # Conteo para ISN (sin ponderar, es una proporción de personas)
            puede  = est.get('v_p', est.get('v', []))
            quiere = est.get('v_d', [])
            if bloque in puede:
                pueden_asistir += 1
                if bloque in quiere:
                    quieren_y_pueden += 1

        # ISN: porcentaje de asistentes que obtuvieron su bloque deseado
        isn = (quieren_y_pueden / pueden_asistir * 100.0) if pueden_asistir > 0 else 0.0

        # Elegimos el bloque que maximice U_total en esta iteracion
        if u_total > mejor_u:
            mejor_u      = u_total
            mejor_bloque = bloque
            mejor_isn    = isn

    lista_u.append(mejor_u)
    lista_isn.append(mejor_isn)
    bloques_ganadores.append(mejor_bloque)

# Bloque de consenso definitivo: el que ganó en todas las iteraciones
bloque_consenso = max(set(bloques_ganadores), key=bloques_ganadores.count)
print(f"  Bloque de consenso definitivo: {bloque_consenso}\n")

# =============================================================================
# 6. GRAFICA BIFOCAL con doble eje Y
# =============================================================================

print(">>> Generando grafica bifocal...")

plt.rcParams['font.family'] = 'DejaVu Sans'

COLOR_U   = '#4f46e5'  # Indigo para Bienestar General
COLOR_ISN = '#f97316'  # Naranja para ISN

fig, ax1 = plt.subplots(figsize=(11, 6))
fig.patch.set_facecolor('#0f0f23')
ax1.set_facecolor('#0f0f23')

# --- Eje izquierdo: U_total (curva continua) ---
line1, = ax1.plot(
    pesos_wf, lista_u,
    color=COLOR_U, linewidth=2.5, linestyle='-',
    label='Bienestar General (U_total)',
    zorder=3
)
ax1.set_xlabel('Peso del Foraneo (W_f)', color='#e2e8f0', fontsize=13, labelpad=10)
ax1.set_ylabel('U_total (Bienestar General)', color=COLOR_U, fontsize=12, labelpad=10)
ax1.tick_params(axis='x', colors='#94a3b8', labelsize=10)
ax1.tick_params(axis='y', colors=COLOR_U,   labelsize=10)
ax1.set_xlim(1.0, 10.0)
ax1.xaxis.set_major_locator(mticker.MultipleLocator(1))
ax1.xaxis.set_minor_locator(mticker.MultipleLocator(0.5))
ax1.grid(which='major', color='#1e293b', linewidth=0.8, zorder=1)
ax1.grid(which='minor', color='#1e293b', linewidth=0.3, linestyle=':', zorder=1)

# Sombra suave bajo la curva de bienestar
ax1.fill_between(pesos_wf, lista_u, alpha=0.12, color=COLOR_U, zorder=2)

# Estilo de spines del eje izquierdo
ax1.spines['left'].set_color(COLOR_U)
ax1.spines['bottom'].set_color('#334155')
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# --- Eje derecho: ISN (linea punteada) ---
ax2 = ax1.twinx()
ax2.set_facecolor('#0f0f23')
line2, = ax2.plot(
    pesos_wf, lista_isn,
    color=COLOR_ISN, linewidth=2.0, linestyle='--',
    label='Satisfaccion Neta (ISN %)',
    zorder=3
)
ax2.set_ylabel('Indice de Satisfaccion Neta (%)', color=COLOR_ISN, fontsize=12, labelpad=10)
ax2.tick_params(axis='y', colors=COLOR_ISN, labelsize=10)
ax2.set_ylim(0, 110)
ax2.yaxis.set_major_locator(mticker.MultipleLocator(10))
ax2.spines['right'].set_color(COLOR_ISN)
ax2.spines['left'].set_color(COLOR_U)
ax2.spines['bottom'].set_color('#334155')
ax2.spines['top'].set_visible(False)

# Anotacion del bloque de consenso
ax1.text(
    9.85, lista_u[-1],
    f' {bloque_consenso}',
    color='#cbd5e1', fontsize=9, va='center',
    bbox=dict(boxstyle='round,pad=0.3', facecolor='#1e293b', edgecolor='#475569', alpha=0.9)
)

# --- Titulo y leyenda unificada (abajo a la derecha) ---
fig.suptitle(
    'Simulacion de Consenso Colectivo — Optimizacion de Horarios · LPC 2026-PI',
    color='#f1f5f9', fontsize=13, fontweight='bold', y=0.99
)

handles = [line1, line2]
labels  = [h.get_label() for h in handles]
ax1.legend(
    handles, labels,
    loc='lower right', fontsize=10,
    facecolor='#1e293b', edgecolor='#475569',
    labelcolor='#e2e8f0', framealpha=0.92
)

plt.tight_layout(rect=[0, 0, 1, 0.96])

# =============================================================================
# 7. EXPORTACION: guardar grafica en la misma carpeta que este script
# =============================================================================

script_dir  = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, 'grafica_consenso.png')
fig.savefig(output_path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"  Grafica guardada en: {output_path}")
print("\nSimulacion completada exitosamente.")
