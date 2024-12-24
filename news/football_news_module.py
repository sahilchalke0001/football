import streamlit as st
import requests

# Constants
API_KEY = '8a1a97d2a3a4431fac26c9ba27ca277c'
NEWS_API_URL = 'https://newsapi.org/v2/everything'

def get_top_football_news():

    params = {
        'q': 'Real Madrid',
        'apiKey': API_KEY,
        'language': 'en',
        'sortBy': 'publishedAt',
        'pageSize': 5,  # Limit to top 5 articles
    }
    
    try:
        response = requests.get(NEWS_API_URL, params=params)
        response.raise_for_status()  # Raise an error for bad HTTP responses
        return response.json().get('articles', [])
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching news: {e}")
        return []

def display_football_news():
    """
    Displays the top football news articles in a Streamlit app.
    """
    articles = get_top_football_news()
    
    if articles:
        st.title('Top 5 Football News')
        for idx, article in enumerate(articles, start=1):
            st.subheader(f"{idx}. {article.get('title', 'No Title')}")
            st.write(f"**Source**: {article.get('source', {}).get('name', 'Unknown')}")
            st.write(f"[Read more]({article.get('url', '#')})")

            # Display the article image if available, otherwise show a placeholder
            image_url = article.get('urlToImage', 'https://via.placeholder.com/700x400.png?text=No+Image+Available')
            st.image(image_url, width=700)  # Display image
            
            st.write('---')  # Separator between articles
    else:
        st.warning("No football news articles available.")

# Streamlit app main function
def main():
    st.title('Football News')
    display_football_news()

if __name__ == '__main__':
    main()
