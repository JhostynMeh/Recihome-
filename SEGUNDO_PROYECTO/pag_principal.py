import pandas as pd
import streamlit as st

# Función para la página principal
def pagina_principal():
    # Inyectar los estilos CSS personalizados
    gif_url = "https://github.com/Sawamurarebatta/Recihome-/blob/main/SEGUNDO_PROYECTO/Uonl.gif?raw=true"  # URL del GIF

    # Título de la aplicación
    st.title("Recihome")
    
    # Descripción de la aplicación
    st.write("Una app centrada en la visualización, recolección y reciclaje de residuos en el hogar, "
             "permitiendo monitorear en tiempo real los residuos generados por los hogares en todo el Perú mediante gráficos y promedios de cada vivienda.")
    
    st.write("Usa el menú de la izquierda para navegar entre páginas.")

    # Incluir el GIF como fondo
    st.markdown(f"""
        <style>
            .stApp {{
                background-image: url("{gif_url}");
                background-repeat: no-repeat;
                background-size: cover;
                background-position: center;
                height: 100%;
            }}
        </style>
    """, unsafe_allow_html=True)

    # Imagen en la esquina inferior derecha
    st.markdown("""
        <div style="position: fixed; bottom: 10px; right: 10px; z-index: 999;">
            <img src="https://raw.githubusercontent.com/Sawamurarebatta/Recihome-/main/SEGUNDO_PROYECTO/planeta.png" width="150">
        </div>
    """, unsafe_allow_html=True)
