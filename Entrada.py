import streamlit as st
from PIL import Image
import base64
import io
import webbrowser

# Configuração da página
st.set_page_config(
    page_title="Afro Garimpo - Links",
    page_icon="🌍",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Cor de fundo da página
background_color = "#586D34"

# CSS personalizado
st.markdown(f"""
    <style>
    .main {{
        background-color: {background_color};
    }}
    .stApp {{
        background-color: {background_color};
        color: #F5F5DC;
    }}
    .stButton>button {{
        background-color: #8B4513;
        color: #F5DEB3;
        border: 2px solid #F5DEB3;
        border-radius: 20px;
        padding: 10px 24px;
        font-weight: bold;
        transition: all 0.3s;
        width: 200px;
        display: block;
        margin: 0 auto !important;
    }}
    .stButton>button:hover {{
        background-color: #A0522D;
        color: white;
        border: 2px solid white;
    }}
    .subheader {{
        color: #F5DEB3;
        text-align: center;
        font-style: italic;
        font-size: 1.2rem;
        margin-top: -10px;
    }}
    .divider {{
        border-top: 2px solid #F5DEB3;
        margin: 1.5rem 0;
        opacity: 0.5;
    }}
    .footer {{
        color: #F5DEB3;
        text-align: center;
        font-size: 0.8rem;
        margin-top: 2rem;
    }}
    .button-container {{
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 15px;
        margin: 10px 0 25px 0;
    }}
    </style>
""", unsafe_allow_html=True)

# Função para converter imagem em base64
def get_image_base64(image):
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Carregar e exibir logo centralizada
logo = Image.open("logo.jpg")  # Substitua se necessário
logo_base64 = get_image_base64(logo)

st.markdown(
    f"""
    <div style='display: flex; justify-content: center; margin-top: 10px;'>
        <img src='data:image/png;base64,{logo_base64}' width='220'/>
    </div>
    """,
    unsafe_allow_html=True
)

# Subtítulo
st.markdown("<p class='subheader'>Cultura, estilo e tradição em cada peça</p>", unsafe_allow_html=True)
st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

# Título
st.markdown("<h2 style='color:#F5DEB3; text-align:center;'>Nossos Contatos</h2>", unsafe_allow_html=True)

# Botões
st.markdown('<div class="button-container">', unsafe_allow_html=True)

if st.button("📷 Instagram"):
    webbrowser.open_new_tab("https://www.instagram.com")

if st.button("💬 WhatsApp"):
    webbrowser.open_new_tab("https://wa.me/27988120708")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

# Informações adicionais
st.markdown("""
    <div style='text-align:center; color:#F5DEB3;'>
        <p>Visite nossas redes sociais e fique por dentro das novidades!</p>
        <p>Promoções exclusivas para seguidores.</p>
    </div>
""", unsafe_allow_html=True)

# Rodapé
st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
st.markdown("<p class='footer'>© 2023 Afro Garimpo - Todos os direitos reservados</p>", unsafe_allow_html=True)
