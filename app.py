import random
from flask import Flask, render_template

# Inicializa la aplicación Flask
app = Flask(__name__)

NUM_MASCOTAS = 40

# --- Diccionario con las 40 Mascotas y sus Mensajes de Sostenibilidad ---
# DEBES COMPLETAR ESTE DICCIONARIO CON TUS 40 ENTRADAS
MASCOTAS_DATA = {
    'mascota_01.png': "El Corozo es nativo. Al consumirlo, apoyas la biodiversidad local y reduces la huella de carbono del transporte internacional.",
    'mascota_02.png': "El Yakón es un cultivo resiliente que mejora la calidad del suelo. Cultivar con conciencia es el primer paso para un planeta más verde.",
    'mascota_03.png': "Usamos frascos reciclables. ¿Te unes? Reutiliza este envase y reduce tu impacto en el relleno sanitario.",
    # ... continúa hasta 'mascota_40.png'
}
# ----------------------------------------------------------------------


@app.route('/qr-scan/')
def handle_qr_scan():
    """Maneja la solicitud al escanear el QR."""
    
    # 1. Lógica de Aleatoriedad: Selecciona un índice entre 1 y 40.
    indice_mascota = random.randint(1, NUM_MASCOTAS)
    
    # 2. Genera el nombre del archivo (ej: 'mascota_05.png')
    nombre_archivo = f'mascota_{indice_mascota:02d}.png' 
    
    # 3. Obtiene el mensaje de sostenibilidad
    mensaje_sostenible = MASCOTAS_DATA.get(
        nombre_archivo, 
        "¡Gracias por elegir So! Nuestro compromiso es el sabor sostenible." # Mensaje de respaldo
    )
    
    # 4. Datos Fijos para la página
    datos_mermelada = {
        'nombre_producto': 'So: Mermelada de Corozo y Yakón',
        'link_video': 'https://www.youtube.com/embed/TU_URL_DE_TU_VIDEO' # ¡Cámbialo!
    }
    
    # 5. Envía toda la información a la plantilla HTML
    return render_template('qr_response.html', 
                           datos=datos_mermelada,
                           nombre_mascota=nombre_archivo,
                           mensaje_sostenible=mensaje_sostenible)

# Solo para probar en tu computadora:
if __name__ == '__main__':
    print("Iniciando servidor local en http://127.0.0.1:5000/qr-scan/")
    app.run(debug=True)