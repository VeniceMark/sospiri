
import streamlit as st
import datetime
from PIL import Image

# -------------------- CONFIGURAZIONE GRAFICA -------------------- #
st.set_page_config(page_title="Wishable", page_icon="🎁", layout="centered")

# Stile personalizzato per look moderno/social
st.markdown("""
    <style>
    html, body, [class*="css"]  {
        font-family: 'Segoe UI', sans-serif;
        background-color: #f8f9fb;
    }
    .main h1, .main h2, .main h3 {
        color: #ff4d6d;
    }
    .wish-box {
        background-color: #ffffff;
        border-radius: 16px;
        padding: 1rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    }
    .wish-img {
        border-radius: 12px;
        width: 100%;
        height: auto;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------- MOCK DATA -------------------- #
users = [
    {
        "id": "1",
        "username": "mario_rossi",
        "full_name": "Mario Rossi",
        "bio": "Appassionato di tecnologia e design.",
        "avatar": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=100&h=100&fit=crop&crop=face"
    },
    {
        "id": "2",
        "username": "giulia_tech",
        "full_name": "Giulia Bianchi",
        "bio": "UX Designer e tech enthusiast.",
        "avatar": "https://images.unsplash.com/photo-1494790108755-2616b612b5bc?w=100&h=100&fit=crop&crop=face"
    }
]

public_wishes = [
    {
        "name": "iPad Pro 12.9"",
        "description": "Perfetto per arte digitale e produttività",
        "price": "$1,099",
        "image": "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=500&h=300&fit=crop",
        "user_id": "2",
        "priority": "Alta"
    },
    {
        "name": "RTX 4090 Graphics Card",
        "description": "Per gaming e streaming in 4K",
        "price": "$1,599",
        "image": "https://images.unsplash.com/photo-1591462618497-9e87ad43a7b6?w=500&h=300&fit=crop",
        "user_id": "1",
        "priority": "Alta"
    }
]

# -------------------- FUNZIONI DI SUPPORTO -------------------- #
def get_user_by_id(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None

# -------------------- UI PRINCIPALE -------------------- #
st.title("🎁 Wishable")
st.caption("Crea e condividi le tue liste dei desideri con un tocco di stile")

st.subheader("🔍 Scopri i desideri pubblici")
for wish in public_wishes:
    user = get_user_by_id(wish["user_id"])

    with st.container():
        st.markdown("<div class='wish-box'>", unsafe_allow_html=True)

        st.image(wish["image"], caption=wish["name"], use_column_width=True)
        st.write(f"**Descrizione:** {wish['description']}")
        st.write(f"**Prezzo:** {wish['price']}")
        st.write(f"**Priorità:** {wish['priority']}")

        if user:
            st.markdown(f"<div style='display:flex; align-items:center; gap:0.5rem; margin-top:1rem;'>"
                        f"<img src='{user['avatar']}' style='width:40px;height:40px;border-radius:50%;'/>"
                        f"<span>@{user['username']} - {user['full_name']}</span>"
                        f"</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

# -------------------- BARRA LATERALE -------------------- #
st.sidebar.header("Navigazione")
st.sidebar.page_link("https://github.com/shadcn-ui/ui", label="shadcn/ui", icon="🔗")
st.sidebar.page_link("https://unsplash.com", label="Unsplash", icon="🌍")
st.sidebar.markdown("---")
st.sidebar.write("Design moderno ispirato ai social network")

# -------------------- FOOTER -------------------- #
st.markdown("""
    <hr>
    <center><small>Powered by Streamlit ✨ | Made with ❤️ by Wishable Team</small></center>
""", unsafe_allow_html=True)
