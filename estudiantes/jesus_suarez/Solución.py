import base64
import json
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. DECODIFICACIÓN SEGURA
# ==========================================
def cargar_estudiantes(ruta_archivo):
    """
    Lee el archivo de texto con los tokens Base64 y los decodifica a diccionarios.
    """
    estudiantes_validos = []
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as file:
            lineas = file.readlines()
            
        for linea in lineas:
            token = linea.strip()
            # Ignorar líneas vacías o el texto suelto al final
            if not token or token.startswith("("):
                continue
            
            try:
                json_str = base64.b64decode(token).decode('utf-8')
                estudiante = json.loads(json_str)
                estudiantes_validos.append(estudiante)
            except Exception as e:
                print(f"⚠️ Error decodificando un token: {e}")
                
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo '{ruta_archivo}'")
        
    return estudiantes_validos

# ==========================================
# 2. EVALUACIÓN Y OPTIMIZACIÓN
# ==========================================
def evaluar_bloque(bloque, estudiantes, wf):
    """
    Calcula el Bienestar General (Utotal) y el ISN adaptado a las llaves reales:
    'f' (Foráneo), 'v_p' (Puede), 'v_d' (Desea/Quiere), 'v' (Caso atípico).
    """
    u_total = 0.0
    pueden_asistir = 0
    quieren_asistir = 0
    
    for est in estudiantes:
        # ¿Es foráneo? (True/False)
        es_foraneo = est.get("f", False)
        peso = wf if es_foraneo else 1.0
        
        # Extraer listas de disponibilidad
        lista_puede = est.get("v_p", [])
        lista_desea = est.get("v_d", [])
        lista_alternativa = est.get("v", []) # Para manejar el token mal tipeado de Alveris
        
        # Lógica de puntuación
        if bloque in lista_desea:
            u_total += (1.5 * peso)
            pueden_asistir += 1
            quieren_asistir += 1
            
        elif bloque in lista_puede or bloque in lista_alternativa:
            u_total += (1.0 * peso)
            pueden_asistir += 1
            
        else: # No Puede
            u_total -= (1.5 * peso)
            
    # Calcular Índice de Satisfacción Neta (ISN)
    if pueden_asistir > 0:
        isn = (quieren_asistir / pueden_asistir) * 100
    else:
        isn = 0.0
        
    return u_total, isn

# ==========================================
# 3. SIMULACIÓN
# ==========================================
def ejecutar_simulacion(estudiantes):
    dias = ["Lun", "Mar", "Mie", "Jue", "Vie"]
    horas = ["08-10", "10-12", "12-14", "14-16"]
    bloques_semana = [f"{dia}_{hora}" for dia in dias for hora in horas]
    
    wf_valores = np.arange(1.0, 10.1, 0.1)
    
    historial_utotal = []
    historial_isn = []
    consenso_definitivo = ""
    
    print("\n🚀 Iniciando simulación...")
    
    for wf in wf_valores:
        mejor_utotal = -float('inf')
        mejor_isn_asociado = 0.0
        mejor_bloque = ""
        
        for bloque in bloques_semana:
            utotal, isn = evaluar_bloque(bloque, estudiantes, wf)
            
            if utotal > mejor_utotal:
                mejor_utotal = utotal
                mejor_isn_asociado = isn
                mejor_bloque = bloque
                
        historial_utotal.append(mejor_utotal)
        historial_isn.append(mejor_isn_asociado)
        consenso_definitivo = mejor_bloque
        
    return wf_valores, historial_utotal, historial_isn, consenso_definitivo

# ==========================================
# 4. GRÁFICA BIFOCAL
# ==========================================
def graficar_resultados(wf_valores, historial_utotal, historial_isn):
    fig, ax1 = plt.subplots(figsize=(10, 6))

    color_u = 'tab:blue'
    ax1.set_xlabel('Peso del Estudiante Foráneo ($W_f$)', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Bienestar General ($U_{total}$)', color=color_u, fontsize=12, fontweight='bold')
    ax1.plot(wf_valores, historial_utotal, color=color_u, linewidth=2.5, label='$U_{total}$ (Puntaje)')
    ax1.tick_params(axis='y', labelcolor=color_u)
    ax1.grid(True, alpha=0.3)

    ax2 = ax1.twinx()
    color_isn = 'tab:red'
    ax2.set_ylabel('Índice de Satisfacción Neta (ISN) %', color=color_isn, fontsize=12, fontweight='bold')
    ax2.plot(wf_valores, historial_isn, color=color_isn, linestyle='--', linewidth=2.5, label='ISN (%)')
    ax2.tick_params(axis='y', labelcolor=color_isn)
    ax2.set_ylim(-5, 105)

    plt.title('Consenso Colectivo: Bienestar vs. Satisfacción Neta', fontsize=14, fontweight='bold', pad=15)
    fig.tight_layout()
    
    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left')

    plt.savefig('grafica_consenso.png', dpi=300)
    print("✅ Gráfica generada y guardada como 'grafica_consenso.png'")
    plt.show()

# --- BLOQUE PRINCIPAL ---
if __name__ == "__main__":
    archivo_tokens = "tokens.txt" 
    estudiantes = cargar_estudiantes(archivo_tokens)
    
    if estudiantes:
        print(f"✅ Se cargaron exitosamente {len(estudiantes)} estudiantes.")
        wf_vals, u_vals, isn_vals, ganador = ejecutar_simulacion(estudiantes)
        graficar_resultados(wf_vals, u_vals, isn_vals)
        print(f"🏆 El bloque de consenso definitivo al finalizar la simulación es: {ganador}")
    else:
        print("⚠️ No se pudo ejecutar la simulación por falta de datos.")
