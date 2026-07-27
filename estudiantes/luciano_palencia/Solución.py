import base64
import json
import numpy as np
import matplotlib.pyplot as plt

tokens_reales = [
    "eyJuIjogIkp1YW4gUGFibG8gUmFtaXJleiIsICJmIjogdHJ1ZSwgInYiOiBbIkx1bl8xNC0xNiIsICJNYXJfMTQtMTYiLCAiTWllXzE0LTE2IiwgIkp1ZV8xNC0xNiIsICJWaWVfMTQtMTYiXX0=",
    "eyJuIjogIkx1Y2lhbm8gUGFsZW5jaWEgIiwgImYiOiBmYWxzZSwgInZfcCI6IFsiTHVuXzEyLTE0IiwgIkx1bl8xNC0xNiIsICJNYXJfMTYtMTQiLCAiTWFyXzE0LTE2IiwgIkp1ZV8xMi0xNCJdLCAidl9kIjogWyJMdW5fMTAtMTQiLCAiTHVuXzE0LTE2IiwgIk1hcl8wOC0xMCJdfQ==",
    "eyJuIjogIlNhbWFudGhhIFBhcnJhIiwgImYiOiB0cnVlLCAidl9wIjogWyJMdW5fMTAtMTIiLCAiSnVlXzA4LTEwIl0sICJ2X2QiOiBbIkx1bl8xMC0xMiJdfQ==",
    "eyJuIjogIkFuZHJcdTAwZTlzIE1lbmRvemEgIiwgImYiOiB0cnVlLCAidl9wIjogWyJNYXJfMTAtMTQiXSwgInZfZCI6IFsiTWFyXzEwLTEyIl19",
    "eyJuIjogIkVsaWV6ZXIgVmVsYXNxdWV6IiwgImYiOiBmYWxzZSwgInZfcCI6IFsiTHVuXzA4LTEwIiwgIkx1bl8xMC0xMiIsICJMdW5fMTAtMTQiLCAiTHVuXzE0LTE2IiwgIk1pZV8wOC0xMCIsICJNaWVfMTAtMTIiLCAiTWllXzEyLTE0IiwgIk1pZV8xNC0xNiIsICJWaWVfMDgtMTAiLCAiVmllXzEwLTEyIiwgIlZpZV8xMi0xNCIsICJWaWVfMTQtMTYiXSwgInZfZCI6IFsiTWFyXzA4LTEwIiwgIk1hcl8xMC0xMiIsICJNYXJfMTItMTQiLCAiTWFyXzE0LTE2IiwgIkp1ZV8wOC0xMCIsICJKdWVfMTAtMTIiLCAiSnVlXzEyLTE0IiwgIkp1ZV8xNC0xNiJdfQ==",
    "eyJuIjogIllhcmlhbmEgT3JvemNvIiwgImYiOiBmYWxzZSwgInZfcCI6IFsiTHVuXzEyLTE0IiwgIkp1ZV8xMC0xMiJdLCAidl9kIjogWyJMdW5fMTAtMTQiLCAiSnVlXzEyLTE0Il19",
    "eyJuIjogIkRlbmljZSBWaWxjaGV6ICIsICJmIjogdHJ1ZSwgInZfcCI6IFsiSnVlXzEwLTEyIl0sICJ2X2QiOiBbIkp1ZV8xMC0xMiJdfQ==",
    "eyJuIjogIkZyYW5jbyBKYWltZXMiLCAiZiI6IGZhbHNlLCAidl9wIjogWyJNYXJfMDgtMTAiLCAiTWFyXzEwLTEyIiwgIk1hcl8yMi0xNCIsICJNYXJfMTQtMTYiLCAiSnVlXzEyLTE0IiwgIlZpZV8wOC0xMCJdLCAidl9kIjogWyJNYXJfMTAtMTIiLCAiTWFyXzEyLTE0IiwgIk1hcl8xNC0xNiIsICJKdWVfMTAtMTQiXX0="
    "eyJuIjogIlphcmFoIEFsdmFyYWRvIiwgImYiOiBmYWxzZSwgInZfcCI6IFsiTWllXzE0LTE2IiwgIkp1ZV8xMC0xMiJdLCAidl9kIjogWyJNaWVfMTAtMTYiLCAiSnVlXzEwLTEyIl19",
    "eyJuIjogIkNlYnJpXHUwMGUxbiBJcmlhcnRlIiwgImYiOiBmYWxzZSwgInZfcCI6IFsiTWFyXzEyLTE0IiwgIk1hcl8xNC0xNiIsICJKdWVfMDgtMTAiLCAiSnVlXzEwLTEyIiwgIlZpZV8wOC0xMCIsICJWaWVfMTAtMTIiLCAiVmllXzEyLTE0IiwgIlZpZV8xNC0xNiJdLCAidl9kIjogWyJNYXJfMTQtMTYiLCAiSnVlXzA4LTEwIiwgIlZpZV8wOC0xMCJdfQ==",
    "eyJuIjogIlJvaW5lciBSb3NhcmlvICIsICJmIjogdHJ1ZSwgInZfcCI6IFsiTHVuXzEyLTE0IiwgIk1hcl8yMi0xNCJdLCAidl9kIjogW119",
    "eyJuIjogIk1hdXJvIE1lbGVhbiAiLCAiZiI6IGZhbHNlLCAidl9wIjogWyJNYXJfMDgtMTAiLCAiTWFyXzEwLTEyIiwgIk1pZV8xMC0xMiIsICJNaWVfMTItMTQiXSwgInZfZCI6IFsiTWllXzEwLTEyIiwgIk1pZV8yMi0xNCJdfQ==",
    "eyJuIjogIkplc1x1MDBmYXMgU3VcdTAwZTFyZXoiLCAiZiI6IGZhbHNlLCAidl9wIjogWyJMdW5fMTAtMTIiLCAiTHVuXzEyLTE0IiwgIk1hcl8wOC0xMCIsICJNYXJfMTAtMTIiLCAiTWFyXzEyLTE0IiwgIk1pZV8yMi0xNCIsICJKdWVfMTAtMTIiLCAiSnVlXzEyLTE0Il0sICJ2X2QiOiBbIkx1bl8xMC0xMiIsICJMdW5fMTAtMTQiLCAiTWFyXzA4LTEwIiwgIk1hcl8xMC0xMiIsICJNYXJfMTItMTQiLCAiSnVlXzEwLTEyIiwgIkp1ZV8yMi0xNCJdfQ==",
    "eyJuIjogIkVmcmFpbiBBcnJpZWNoZSIsICJmIjogZmFsc2UsICJ2X3AiOiBbIkx1bl8xMC0xMiIsICJMdW5fMTAtMTQiLCAiTHVuXzE0LTE2IiwgIk1hcl8wOC0xMCIsICJNYXJfMTAtMTIiLCAiTWFyXzEyLTE0IiwgIk1hcl8xNC0xNiIsICJKdWVfMTAtMTIiLCAiSnVlXzEyLTE0IiwgIkp1ZV8xNC0xNiJdLCAidl9kIjogWyJMdW5fMTAtMTIiLCAiSnVlXzEwLTEyIl19",
    "eyJuIjogIlJlYmVjYSBIZXJuYW5kZXogIiwgImYiOiBmYWxzZSwgInZfcCI6IFsiTWFyXzEyLTE0IiwgIkp1ZV8xNC0xNiJdLCAidl9kIjogWyJNYXJfMDgtMTAiLCAiSnVlXzEyLTE0Il19",
    "eyJuIjogIkFsdmVyaXMgRWRtdW5kbyBMXHUwMGYzcGV6IGx1Z28gIiwgImYiOiBmYWxzZSwgInYiOiBbIkx1bl8yMi0xNCIsICJNYXJfMTYtMTQiLCAiTWllXzEyLTE0IiwgIkp1ZV8xMi0xNCIsICJWaWVfMTAtMTQiXX0=",
    "eyJuIjogIkp1YW4gUmFtaXJleiAiLCAiZiI6IGZhbHNlLCAidl9wIjogWyJMdW5fMTAtMTQiLCAiTWFyXzA4LTEwIl0sICJ2X2QiOiBbIk1pZV8xMi0xNCIsICJKdWVfMTAtMTQiLCAiVmllXzEyLTE0Il19",
    "eyJuIjogIk1pcmFuZGEgTW9udGVybyAiLCAiZiI6IGZhbHNlLCAidl9wIjogWyJNYXJfMTAtMTIiLCAiTWllXzA4LTEyIiwgIkp1ZV8xMC0xMiIsICJWaWVfMTAtMTIiLCAiVmllXzEyLTE0Il0sICJ2X2QiOiBbIkx1bl8xMC0xMiIsICJNYXJfMTItMTQiLCAiTWllXzA4LTEwIiwgIlZpZV8xMC0xMiIsICJWaWVfMTItMTQiXX0="
]

estudiantes = []
for token in tokens_reales:
    try:
        estudiantes.append(json.loads(base64.b64decode(token).decode('utf-8')))
    except:
        pass

dias = ["Lun", "Mar", "Mie", "Jue", "Vie"]
bloques = ["08-10", "10-12", "12-14", "14-16"]
todos_los_bloques = [f"{d}_{b}" for d in dias for b in bloques]
pesos_foraneos = np.arange(1.0, 10.1, 0.1)

historico_wf, historico_utotal, historico_isn, bloques_ganadores = [], [], [], []

for wf in pesos_foraneos:
    mejor_bloque, mejor_utotal, mejor_isn = None, float('-inf'), 0.0
    for bloque in todos_los_bloques:
        u_bloque, incluidos_que_quieren, total_incluidos = 0.0, 0, 0
        es_tarde = "12-14" in bloque or "14-16" in bloque
        for est in estudiantes:
            peso = wf if est.get("f", False) else 1.0
            puntos = -1.5
            if bloque in est.get("v_p", []):
                puntos = 1.5
                incluidos_que_quieren += 1
                total_incluidos += 1
            elif bloque in est.get("v_d", []) or bloque in est.get("v", []):
                puntos = 1.0
                total_incluidos += 1
            if est.get("f", False) and es_tarde:
                puntos -= 2.0 if puntos > 0 else 1.5
            u_bloque += puntos * peso
        if u_bloque > mejor_utotal:
            mejor_utotal, mejor_bloque = u_bloque, bloque
            mejor_isn = (incluidos_que_quieren / total_incluidos * 100) if total_incluidos > 0 else 0.0
    historico_wf.append(wf)
    historico_utotal.append(mejor_utotal)
    historico_isn.append(mejor_isn)
    bloques_ganadores.append(mejor_bloque)

fig, ax1 = plt.subplots(figsize=(10, 6))
color_utotal = '#008080'
ax1.set_xlabel('Peso del Estudiante Foráneo ($W_f$)', fontsize=12)
ax1.set_ylabel('$U_{total}$', color=color_utotal, fontsize=12)
linea1, = ax1.plot(historico_wf, historico_utotal, color=color_utotal, linewidth=2.5, label='$U_{total}$')
ax1.tick_params(axis='y', labelcolor=color_utotal)
ax1.grid(True, linestyle='--', alpha=0.5)

ax2 = ax1.twinx()
color_isn = '#C71585'
ax2.set_ylabel('ISN (%)', color=color_isn, fontsize=12)
linea2, = ax2.plot(historico_wf, historico_isn, color=color_isn, linestyle=':', linewidth=3, label='ISN (%)')
ax2.tick_params(axis='y', labelcolor=color_isn)
ax2.set_ylim(0, 105)

plt.axvline(x=1.0, color='#A9A9A9', linestyle='--', linewidth=1.5)
ax1.annotate('Óptimo: 1.0', xy=(1.0, historico_utotal[0]), xytext=(1.5, historico_utotal[0]),
             arrowprops=dict(facecolor='black', shrink=0.08, width=2, headwidth=8))

lineas = [linea1, linea2]
leyendas = [l.get_label() for l in lineas]
ax1.legend(lineas, leyendas, loc='lower right', frameon=True)
plt.title('Análisis de Consenso: $U_{total}$ vs ISN (%)', fontsize=14, fontweight='bold', pad=15)
fig.tight_layout()
plt.savefig('grafica_consenso.png', dpi=300)
plt.show()
