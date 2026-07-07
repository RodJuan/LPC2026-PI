# ==============================================================================
# 🏛️ ASIGNACIÓN 1 - MÓDULO 1: INTERFAZ DE CAPTURA DE VOTOS (Fase de Recolección)
# ==============================================================================

import base64
import json
import ipywidgets as widgets
from IPython.display import display

# --- Variables Globales de Calendario ---
dias = ["Lun", "Mar", "Mie", "Jue", "Vie"]
horas = ["08-10", "10-12", "12-14", "14-16"]

# Configuración inicial de datos personales y socioeconómicos
nombre = widgets.Text(placeholder='Tu Nombre y Apellido', description='Nombre:')

procedencia = widgets.Dropdown(
    options=[
        ('Local (Vive en Maracaibo)', 1.0),
        ('Foráneo Cerca (San Francisco / La Cañada)', 1.2),
        ('Foráneo Medio (Cabimas / Costa Oriental)', 1.5),
        ('Foráneo Lejos (Fuera de la COL / Horas de viaje)', 2.0)
    ],
    description='Procedencia:',
    layout=widgets.Layout(width='450px')
)

residencia_maracaibo = widgets.Checkbox(
    description='¿Resides en Maracaibo de Lunes a Viernes?',
    value=False,
    layout=widgets.Layout(width='450px')
)

logistica_local = widgets.Dropdown(
    options=[
        ('Transporte propio / Sin complicaciones de traslado', 1.0),
        ('Dependo de transporte público largo o difícil', 1.3),
        ('Tengo horario laboral u obligaciones restrictivas', 1.5)
    ],
    description='Logística:',
    layout=widgets.Layout(width='450px')
)

output_voto = widgets.Output()

print("========================================================================")
print("🏛️ CONFIGURACIÓN DE HORARIO v3.0 (Fase 1: Captura Estudiantil)")
print("========================================================================")
display(nombre, procedencia, residencia_maracaibo, logistica_local)
print("-" * 72)
print("Indica los bloques donde PUEDES asistir y marca con DESEO tu horario ideal:")

# Generación dinámica de la matriz de checkboxes
checks = {}
for d in dias:
    print(f"\n--- {d} ---")
    for b in horas:
        c_puedo = widgets.Checkbox(description="Puedo", indent=False)
        c_deseo = widgets.Checkbox(description="Deseo", indent=False)

        checks[f"{d}_{b}_puedo"] = c_puedo
        checks[f"{d}_{b}_deseo"] = c_deseo

        etiqueta = widgets.Label(value=f"{b}:", layout=widgets.Layout(width='60px'))
        display(widgets.HBox([etiqueta, c_puedo, c_deseo]))

# Función para empaquetar y codificar el voto en Base64
def generar_voto(b):
    puedo = [k.replace("_puedo", "") for k, v in checks.items() if "_puedo" in k and v.value]
    deseo = [k.replace("_deseo", "") for k, v in checks.items() if "_deseo" in k and v.value]

    if not nombre.value or not puedo:
        with output_voto:
            output_voto.clear_output()
            print("❌ Error: Debes ingresar tu nombre y al menos una disponibilidad (Puedo).")
        return

    data = {
        "n": nombre.value,
        "proc_w": procedencia.value,
        "res_m": residencia_maracaibo.value,
        "socio_w": logistica_local.value,
        "v_p": puedo,
        "v_d": deseo
    }

    token = base64.b64encode(json.dumps(data).encode('utf-8')).decode()

    with output_voto:
        output_voto.clear_output()
        print("\n✅ ¡VOTO PERSONALIZADO GENERADO CON ÉXITO!")
        print("Copia y pega TODO este código en el grupo de WhatsApp:")
        print("-" * 65)
        print(token)
        print("-" * 65)

print("\n")
btn_voto = widgets.Button(description="GENERAR CÓDIGO V3.0", button_style='success', layout=widgets.Layout(width='200px'))
btn_voto.on_click(generar_voto)
display(btn_voto, output_voto)

# ==============================================================================
# 🏛️ ASIGNACIÓN 1 - MÓDULO 2: PROCESADOR, SIMULACIÓN Y GRÁFICAS OFICIALES
# ==============================================================================

import base64
import json
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import ipywidgets as widgets
from IPython.display import display

# --- Variables Globales de Calendario ---
dias = ["Lun", "Mar", "Mie", "Jue", "Vie"]
horas = ["08-10", "10-12", "12-14", "14-16"]
bloques_semana = [f"{d}_{b}" for d in dias for b in horas]

print("========================================================================")
print("📊 ESCRUTINIO GENERAL v3.0 (Fase 2: Simulación y Optimización)")
print("========================================================================")
print("Pega aquí abajo todos los tokens recolectados (uno por línea):")

txt_tokens = widgets.Textarea(
    placeholder='Pega los tokens aquí...',
    layout=widgets.Layout(width='100%', height='150px')
)
output_procesamiento = widgets.Output()
display(txt_tokens)

def procesar_simulacion_oficial(b):
    # Separar la entrada por saltos de línea y limpiar espacios
    raw_input = txt_tokens.value.replace(",", "\n")
    lista_tokens = [t.strip() for t in raw_input.split("\n") if t.strip()]

    if not lista_tokens:
        with output_procesamiento:
            output_procesamiento.clear_output()
            print("❌ Error: No se han ingresado tokens para el procesamiento.")
        return

    estudiantes = []
    for idx, token in enumerate(lista_tokens):
        try:
            datos_decodificados = base64.b64decode(token).decode('utf-8')
            estudiantes.append(json.loads(datos_decodificados))
        except Exception as e:
            with output_procesamiento:
                print(f"⚠️ Alerta: Token inválido ignorado en la línea {idx+1}")

    # --- SIMULACIÓN EXIGIDA POR LA ASIGNACIÓN (Paso de W_f de 1.0 a 10.0) ---
    pesos_foraneo = np.arange(1.0, 10.1, 0.1)

    historico_wf = []
    historico_utotal = []
    historico_isn = []
    bloques_ganadores = []

    for W_f in pesos_foraneo:
        mejor_bloque = None
        max_utotal = float('-inf')
        mejor_isn = 0.0

        for bloque in bloques_semana:
            u_bloque = 0.0
            alumnos_pueden = 0
            alumnos_quiero = 0

            for est in estudiantes:
                # Criterio de clasificación oficial adaptado a la v3.0
                # Si es foráneo (proc_w > 1.0) y NO vive en Maracaibo de lunes a viernes
                es_foraneo = est["proc_w"] > 1.0 and not est["res_m"]
                peso_politico = W_f if es_foraneo else 1.0

                # Reglas de puntuación de la guía
                if bloque in est["v_p"]:
                    puntos = 1.0
                    alumnos_pueden += 1
                    if bloque in est["v_d"]:
                        puntos += 0.5
                        alumnos_quiero += 1
                else:
                    puntos = -1.5 # Penalización drástica

                u_bloque += puntos * peso_politico

            if u_bloque > max_utotal:
                max_utotal = u_bloque
                mejor_bloque = bloque
                # ISN oficial de la guía basado exclusivamente en conteo democrático físico
                if alumnos_pueden > 0:
                    mejor_isn = (alumnos_quiero / alumnos_pueden) * 100
                else:
                    mejor_isn = 0.0

        historico_wf.append(W_f)
        historico_utotal.append(max_utotal)
        historico_isn.append(mejor_isn)
        bloques_ganadores.append(mejor_bloque)

    with output_procesamiento:
        output_procesamiento.clear_output()

        print("=== RESULTADOS DE LA SIMULACIÓN OFICIAL ===")
        print(f"Consenso Inicial (W_f = 1.0): {bloques_ganadores[0].replace('_', ' ')} (ISN: {historico_isn[0]:.1f}%)")
        print(f"Consenso Foráneo (W_f = 10.0): {bloques_ganadores[-1].replace('_', ' ')} (ISN: {historico_isn[-1]:.1f}%)\n")

        # --- 1. Generación de la Gráfica Bifocal Obligatoria ---
        fig, ax1 = plt.subplots(figsize=(10, 5))
        color_utotal = 'indigo'
        ax1.set_xlabel('Peso del Estudiante Foráneo ($W_f$)', fontsize=11)
        ax1.set_ylabel('Bienestar General ($U_{total}$)', color=color_utotal, fontsize=11)
        linea1, = ax1.plot(historico_wf, historico_utotal, color=color_utotal, linewidth=2.5, label='Bienestar General ($U_{total}$)')
        ax1.tick_params(axis='y', labelcolor=color_utotal)
        ax1.grid(True, linestyle=':', alpha=0.6)

        ax2 = ax1.twinx()
        color_isn = 'darkorange'
        ax2.set_ylabel('Satisfacción Neta ($ISN$ %)', color=color_isn, fontsize=11)
        linea2, = ax2.plot(historico_wf, historico_isn, color=color_isn, linestyle='--', linewidth=2, label='Satisfacción Neta ($ISN$)')
        ax2.tick_params(axis='y', labelcolor=color_isn)
        ax2.set_ylim(-5, 105)

        # Anotaciones en los extremos
        ax1.annotate(f"Inicial: {bloques_ganadores[0].replace('_', ' ')}", xy=(historico_wf[0], historico_utotal[0]),
                     xytext=(historico_wf[0]+0.4, historico_utotal[0]-2), arrowprops=dict(arrowstyle='->'))
        ax1.annotate(f"Final: {bloques_ganadores[-1].replace('_', ' ')}", xy=(historico_wf[-1], historico_utotal[-1]),
                     xytext=(historico_wf[-1]-2.5, historico_utotal[-1]-5), arrowprops=dict(arrowstyle='->'))

        ax1.legend([linea1, linea2], [linea1.get_label(), linea2.get_label()], loc='lower right', frameon=True, shadow=True)
        plt.title('Simulación de Consenso Colectivo y Optimización de Horarios', fontsize=12, fontweight='bold', pad=15)
        fig.tight_layout()
        plt.savefig('grafica_consenso.png', dpi=300)
        plt.show()

        # --- 2. Matriz de Calor Complementaria (Tu Tabla Gráfica) ---
        # Se genera con W_f = 1.0 para visualizar la distribución cruda de votos del salón
        matriz_calor = np.zeros((len(horas), len(dias)))
        for i, hora in enumerate(horas):
            for j, dia in enumerate(dias):
                b_actual = f"{dia}_{hora}"
                u_blq = 0.0
                for est in estudiantes:
                    if b_actual in est["v_p"]:
                        u_blq += 1.5 if b_actual in est["v_d"] else 1.0
                    else:
                        u_blq -= 1.5
                matriz_calor[i, j] = u_blq

        plt.figure(figsize=(9, 4.5))
        sns.heatmap(matriz_calor, annot=True, fmt=".1f", cmap="RdYlGn", xticklabels=dias, yticklabels=horas, cbar_kws={'label': 'Preferencia del Grupo'})
        plt.title('Matriz Gráfica de Consenso General (Distribución de Votos por Celda)', fontsize=12, fontweight='bold', pad=12)
        plt.xlabel('Días')
        plt.ylabel('Horas')
        plt.tight_layout()
        plt.savefig('tabla_calor_horarios.png', dpi=300)
        plt.show()

btn_procesar = widgets.Button(description="PROCESAR OPTIMIZACIÓN OFICIAL", button_style='primary', layout=widgets.Layout(width='280px'))
btn_procesar.on_click(procesar_simulacion_oficial)
display(btn_procesar, output_procesamiento)
