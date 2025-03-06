import streamlit as st
from Bundesliga.bundesliga import bundesliga
from EPL.epl import epl
from LaLiga.laliga import laliga
from SerieA.seriea import seriea
from home import home_page
from news.football_news_module import display_football_news
from Player_valuation.player import player


def main():
    st.set_page_config(
        page_title='Football Match Outcome Predictor',
        page_icon='⚽',
        layout='centered',
        initial_sidebar_state='auto'
    )

    st.markdown(
        """
        <style>
        
        </style>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.header("Select the League")
    selected_page = st.sidebar.radio(
        "Choose", 
        ["Home", "Bundesliga", "EPL", "La Liga", "Serie A", "Football News", "Player valuation"]
    )

    if selected_page == "Home":
        home_page()
    elif selected_page == "Bundesliga":
        bundesliga()
    elif selected_page == "EPL":
        epl()
    elif selected_page == "La Liga":
        laliga()
    elif selected_page == "Serie A":
        seriea()
    elif selected_page == "Football News":
        display_football_news()
    elif selected_page == "Player valuation":
        player()
 # Call the football news function

if __name__ == "__main__":
    main()



