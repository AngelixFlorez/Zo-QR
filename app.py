import random
from flask import Flask, render_template # type: ignore

# Inicializa la aplicación Flask
app = Flask(__name__)

NUM_MASCOTAS = 30

# --- Diccionario con las 40 Mascotas y sus Mensajes de Sostenibilidad ---
# DEBES COMPLETAR ESTE DICCIONARIO CON TUS 40 ENTRADAS
MASCOTAS_DATA = {
    # 1. Zó! Original (Sosteniendo el Corozo)
    'mascota_01.png': "Soy Zó!, y tengo el corozo, una fruta nativa. Al consumirla, reduces la huella de carbono del transporte internacional.",
    # 2. Zó! con una Hoja (Sosteniendo una hoja)
    'mascota_02.png': "Esta hoja me da sombra y vida. Recuerda que plantar un árbol o cuidar la vegetación local mejora la calidad del aire para todos.",
    # 3. Zó! con Gota de Mermelada (Sosteniendo una gota)
    'mascota_03.png': "El sabor natural es nuestro compromiso. Evitamos aditivos artificiales para que disfrutes de la mermelada más pura y deliciosa.",
    # 4. Zó! con Gorro de Granjero (Usando un sombrero de paja)
    'mascota_04.png': "Apoyamos a nuestros agricultores. Elegir productos de comercio justo garantiza condiciones dignas y sostenibles para quienes cultivan.",
    # 5. Zó! Recolectora (Con una canasta)
    'mascota_05.png': "Nuestra cosecha es consciente. Solo recolectamos lo necesario para mantener el equilibrio del ecosistema local.",
    # 6. Zó! con un Brote (Sosteniendo un brote)
    'mascota_06.png': "Cada acción es una semilla. Hoy siembras el cambio, mañana cosechas un futuro más verde para el planeta.",
    # 7. Zó! Cultivadora (Con una pala)
    'mascota_07.png': "Cuidar el suelo es vital. Usamos métodos de cultivo que nutren la tierra para que pueda producir alimentos de calidad por años.",
    # 8. Zó! Amiga del Sol (Con gafas de sol)
    'mascota_08.png': "Aprovecha la energía solar. Usa la luz natural en casa y ayuda a reducir la demanda de energía basada en combustibles fósiles.",
    # 9. Zó! Curiosa (Con lupa)
    'mascota_09.png': "Examinamos cada detalle. La calidad de nuestros ingredientes orgánicos es verificada para asegurar su pureza y origen natural.",
    # 10. Zó! con un Frasco (Abrazando un frasco)
    'mascota_10.png': "¡Mi hogar es reciclable! Este frasco está hecho para ser reutilizado. Lávalo y dale una segunda vida.",
    # 11. Zó! con Gotas de Rocío (Con gotas de rocío)
    'mascota_11.png': "El agua es nuestro tesoro. Promovemos el uso eficiente del agua en nuestros cultivos para preservar este recurso vital.",
    # 12. Zó! Chef (Con gorro de chef)
    'mascota_12.png': "Nuestro proceso es artesanal y lento. Valoramos la paciencia y la mano de obra local para un sabor auténtico.",
    # 13. Zó! con una Flor (Sosteniendo una flor)
    'mascota_13.png': "¡Cuidado con la biodiversidad! Evitar pesticidas dañinos permite que las flores y plantas nativas prosperen.",
    # 14. Zó! Guardiana del Agua (Con una gota de agua)
    'mascota_14.png': "¡No desperdicies! Revisa los grifos y no dejes correr el agua. Cada gota cuenta para nuestro ecosistema.",
    # 15. Zó! Raíz de Yakón (Sosteniendo la raíz de Yakón)
    'mascota_15.png': "El Yakón cuida la tierra. Es un cultivo de bajo impacto que enriquece el suelo. ¡Un héroe sostenible!",
    # 16. Zó! con un Corazón (Abrazando el corozo)
    'mascota_16.png': "Ponemos el corazón en todo. Nuestro compromiso ético significa prácticas justas y respeto total por la naturaleza.",
    # 17. Zó! en Equipo (Pulgar arriba)
    'mascota_17.png': "La unión hace la fuerza. Al igual que una colonia, trabajamos en comunidad para apoyar el desarrollo local y sostenible.",
    # 18. Zó! Protectora (Con escudo verde)
    'mascota_18.png': "Somos guardianes del ambiente. Protegemos los recursos naturales de la contaminación y la sobreexplotación.",
    # 19. Zó! con un Pequeño Mapa (Mirando un mapa)
    'mascota_19.png': "¡Kilómetro cero! Elegir productos locales reduce el transporte y, con él, la emisión de CO2.",
    # 20. Zó! Compartiendo (Ofreciendo el corozo)
    'mascota_20.png': "Comparte de forma consciente. El consumo responsable ayuda a evitar el desperdicio y la escasez de alimentos.",
    # 21. Zó! con Gafas de Laboratorio (Con gafas)
    'mascota_21.png': "Fórmula limpia, sabor real. Nos aseguramos de que solo tengas ingredientes naturales, sin químicos ni colorantes.",
    # 22. Zó! Sostenible (Con símbolo de reciclaje)
    'mascota_22.png': "Reciclar es mi superpoder. Separa tus residuos correctamente para darle una nueva vida a los materiales.",
    # 23. Zó! Alegre (Saltando de felicidad)
    'mascota_23.png': "Un planeta sano trae felicidad. Cada compra sostenible es un paso hacia un futuro con más bienestar.",
    # 24. Zó! con una Abeja Amiga (Con una abeja)
    'mascota_24.png': "¡Gracias, polinizadores! Cuidar de las abejas y otros insectos es clave para que nuestros cultivos den fruto.",
    # 25. Zó! con un Libro (Leyendo)
    'mascota_25.png': "El conocimiento es poder. Infórmate sobre el origen de tus alimentos para tomar decisiones de compra más sostenibles.",
    # 26. Zó! con Botas de Lluvia (Con botas)
    'mascota_26.png': "Afrontamos el clima. Adaptamos nuestras prácticas agrícolas para ser más resistentes a los cambios climáticos.",
    # 27. Zó! con un Regaderita (Regando)
    'mascota_27.png': "Usa tus recursos con mesura. Aplica el riego eficiente para no desperdiciar agua y energía en la agricultura.",
    # 28. Zó! con un Rayo de Sol (Bajo un rayo de sol)
    'mascota_28.png': "El sol nos da vida. Apoyamos la generación de energía renovable, como la solar, para reducir la dependencia de combustibles.",
    # 29. Zó! con un Mapa Estelar (Mirando las estrellas)
    'mascota_29.png': "Pensamos a largo plazo. Nuestra visión sostenible va más allá del hoy, buscando dejar un legado positivo para el futuro.",
    # 30. Zó! Dorada (Totalmente dorada)
    'mascota_30.png': "Eres un tesoro. Elegir Zó! significa que valoras la sostenibilidad como algo preciado y que impacta positivamente el mundo."
}
# ----------------------------------------------------------------------


@app.route('/')         # <--- RUTA PRINCIPAL # <--- Mantenemos la ruta antigua por si acaso
def handle_qr_scan():
    """Maneja la solicitud al escanear el QR."""
    
    # 1. Lógica de Aleatoriedad: Selecciona un índice entre 1 y 40.
    indice_mascota = random.randint(1, NUM_MASCOTAS)
    
    # 2. Genera el nombre del archivo (ej: 'mascota_05.png')
    nombre_archivo = f'mascota_{indice_mascota:02d}.png' 
    
    # 3. Obtiene el mensaje de sostenibilidad
    mensaje_sostenible = MASCOTAS_DATA.get(
        nombre_archivo, 
        "¡Gracias por elegir Zó! Nuestro compromiso es el sabor sostenible." # Mensaje de respaldo
    )
    
    # 4. Datos Fijos para la página
    datos_mermelada = {
        'nombre_producto': 'Zó!: Mermelada de Corozo y Yakón',
        'link_video': 'https://www.youtube.com/embed/TU_URL_DE_TU_VIDEO' # ¡Cámbialo!
    }
    
    # 5. Envía toda la información a la plantilla HTML
    return render_template('qr_response.html', 
                           datos=datos_mermelada,
                           nombre_mascota=nombre_archivo,
                           mensaje_sostenible=mensaje_sostenible)
