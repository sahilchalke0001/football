import streamlit as st
from PIL import Image

def home_page():
    # Custom CSS for background image
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url('https://wallpapers-clan.com/wp-content/uploads/2024/01/dynamic-red-cristiano-ronaldo-desktop-wallpaper-preview.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
        .st-emotion-cache-1wmy9hl.e1f1d6gn1 {
        background-color: rgba(173,173,173, 0.6); 
        border-radius: 8px;  
        display: flex;
        text-align: center;
        }
        li,h1{
        color: black;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    container = st.container()

    with container:
        st.image("logo1.png", width=150)

        st.title("⚽Football⚽")

        st.write("* This web app predicts the outcome of football matches in the top European leagues like: Bundesliga, EPL, La Liga, Serie A")



        st.write("* Select the league from the sidebar to get started")

    
        st.write("* Bundesliga: German Football League")
        st.text("")
        st.write("* EPL: English Premier League")
        st.text("")
        st.write("* La Liga: Spanish Football League")
        st.text("")
        st.write("* Serie A: Italian Football League")
        st.text("")
        st.write("* Football News")
        st.text("")
        st.write("* Player Valuation")
        st.text("")

if __name__ == "__main__":
    home_page()

