# Colores personalizados para la aplicación
colores = {
    'fondo_principal': '#16423C',  # Verde oscuro
    'fondo_sidebar': '#C4DAD2',    # Verde claro
    'encabezado': '#FFFFFF',       # Blanco
    'boton': '#6A9C89',            # Verde medio
    'texto_general': '#FFFFFF',    # Blanco
    'grafico': ['#16423C', '#6A9C89', '#C4DAD2', '#E9EFEC']  # Colores para gráficos
}

# Función para inyectar los estilos CSS personalizados
def inyectar_estilos():
    return f"""
    <style>
    /* Cargar la fuente TTF */
    @font-face {{
        font-family: 'CustomFont';
        src: url('custom_font.ttf') format('truetype');
    }}
    
    /* Fondo principal */
    .stApp {{
        background-color: {colores['fondo_principal']};
    }}
    
    /* Fondo del sidebar */
    [data-testid="stSidebar"] {{
        background-color: {colores['fondo_sidebar']};
    }}
    
    /* Encabezados (titulo principal y subtítulos) */
    h1, h2, h3, h4 {{
        color: {colores['encabezado']};
        font-family: 'CustomFont', sans-serif;  /* Usar la fuente personalizada */
    }}
    
    /* Botones y enlaces */
    .css-1q8dd3e, .css-1aumxhk, .st-cv {{
        background-color: {colores['boton']} !important;
        color: {colores['fondo_principal']} !important;
        border: 1px solid {colores['encabezado']} !important;
    }}
    
    /* Texto general */
    .css-16huue1 {{
        color: {colores['texto_general']} !important;
        font-family: 'CustomFont', sans-serif;  /* Usar la fuente personalizada */
    }}
    </style> agrgale al fondo circulos blancos 

# Función para inyectar los estilos CSS personalizados con círculos blancos en el fondo
def inyectar_estilos():
    return f"""
    <style>
    /* Cargar la fuente TTF */
    @font-face {{
        font-family: 'CustomFont';
        src: url('custom_font.ttf') format('truetype');
    }}
    
    /* Fondo principal con círculos blancos */
    .stApp {{
        background-color: {colores['fondo_principal']};
        background-image: radial-gradient(circle, #ffffff 20%, transparent 20%);
        background-size: 100px 100px;  /* Tamaño de los círculos */
        background-position: 0 0, 50px 50px;  /* Posicionar los círculos */
        background-repeat: repeat;
    }}
    
    /* Fondo del sidebar */
    [data-testid="stSidebar"] {{
        background-color: {colores['fondo_sidebar']};
    }}
    
    /* Encabezados (titulo principal y subtítulos) */
    h1, h2, h3, h4 {{
        color: {colores['encabezado']};
        font-family: 'CustomFont', sans-serif;  /* Usar la fuente personalizada */
    }}
    
    /* Botones y enlaces */
    .css-1q8dd3e, .css-1aumxhk, .st-cv {{
        background-color: {colores['boton']} !important;
        color: {colores['fondo_principal']} !important;
        border: 1px solid {colores['encabezado']} !important;
    }}
    
    /* Texto general */
    .css-16huue1 {{
        color: {colores['texto_general']} !important;
        font-family: 'CustomFont', sans-serif;  /* Usar la fuente personalizada */
    }}
    </style>
    """


