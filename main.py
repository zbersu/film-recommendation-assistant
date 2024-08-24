import streamlit as st
import openai
import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set page config
st.set_page_config(page_title="Movie Recommendation System", page_icon="🎬", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .stApp {
        background-image: linear-gradient(to right, #141E30, #243B55);
        color: #FFFFFF;
    }
    .stButton>button {
        color: #FFFFFF;
        background-color: #4CAF50;
        border-radius: 20px;
    }
    .stTextInput>div>div>input {
        color: #FFFFFF;
        background-color: rgba(255, 255, 255, 0.1);
    }
    .stMultiSelect>div>div>div {
        background-color: rgba(255, 255, 255, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# Title and introduction
st.title("🎬 Movie Recommendation System")
st.markdown("Discover your next favorite movie based on your preferences!")

# Sidebar for user inputs
st.sidebar.header("Your Movie Preferences")

# Genre selection
genres = st.sidebar.multiselect(
    "Select your favorite genre(s):",
    ["Action", "Comedy", "Drama", "Sci-Fi", "Horror", "Romance", "Thriller", "Fantasy", "Musical", "Animation"],
    help="You can select multiple genres"
)

# Favorite movies input
st.sidebar.subheader("Your Top 3 Favorite Movies")
favorite_movies = []
for i in range(3):
    movie = st.sidebar.text_input(f"Favorite Movie #{i + 1}", key=f"movie_{i}")
    if movie:
        favorite_movies.append(movie)


def get_movie_recommendations(genres, favorite_movies):
    prompt = f"""
    Based on the following user preferences, recommend 4 movies:
    Favorite genres: {', '.join(genres)}
    Favorite movies: {', '.join(favorite_movies)}

    Please provide the recommendations in a markdown table format with the following columns:
    | Movie | Genre | Short Summary | IMDB Score |

    Each short summary should be concise, not exceeding 30 words. The IMDB Score should be a number between 1 and 10.
    Include the year of the movie in parentheses next to the movie title.

    After the table, provide for each recommendation:
    1. A brief explanation (1-2 sentences) for why it was recommended.
    2. An interesting trivia fact about the movie, prefixed with "Did you know:"

    Example format:
    | Movie | Genre | Short Summary | IMDB Score |
    |-------|-------|---------------|------------|
    | Inception (2010) | Sci-Fi | A thief enters dreams to plant ideas. | 8.8 |

    1. Inception (2010): Recommended for its mind-bending plot and stunning visuals, which align with your interest in sci-fi.
       \n🎬 Did you know: The spinning top at the end of Inception was not actually Leonardo DiCaprio's totem - it was his wedding ring.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a movie recommendation expert with vast knowledge of cinema."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000
    )

    return response.choices[0].message['content']


def parse_response(gpt_response):
    # Split the response into table and explanations
    parts = gpt_response.split('\n\n', 1)
    table_md = parts[0]
    explanations = parts[1] if len(parts) > 1 else ""

    # Convert markdown table to DataFrame
    lines = table_md.split('\n')
    headers = [h.strip() for h in lines[0].split('|')[1:-1]]
    data = []
    for line in lines[2:]:
        row = [cell.strip() for cell in line.split('|')[1:-1]]
        if len(row) == len(headers):
            data.append(row)

    df = pd.DataFrame(data, columns=headers)
    return df, explanations


if st.sidebar.button("Get Recommendations"):
    if not genres or len(favorite_movies) < 3:
        st.warning("Please select at least one genre and enter three favorite movies.")
    else:
        with st.spinner("Generating your personalized movie recommendations..."):
            try:
                gpt_response = get_movie_recommendations(genres, favorite_movies)
                recommendations_df, explanations = parse_response(gpt_response)

                if not recommendations_df.empty:
                    st.subheader("Your Personalized Movie Recommendations")
                    st.markdown(gpt_response)

                else:
                    st.warning("No valid recommendations could be parsed from the response. Please try again.")
                    st.text("Raw GPT Response:")
                    st.text(gpt_response)
            except Exception as e:
                st.error(f"An error occurred while processing the recommendations: {str(e)}")
                st.text("Raw GPT Response:")
                st.text(gpt_response)

# Footer
st.sidebar.markdown("---")
st.sidebar.info(
    "This Movie Recommendation System uses GPT-4o-mini model to provide personalized suggestions based on your preferences.")

# Main page additional content
if 'recommendations_df' not in locals():
    st.markdown("""
    ## How It Works
    1. Select your favorite movie genres from the sidebar.
    2. Enter your top 3 favorite movies.
    3. Click "Get Recommendations" to receive personalized movie suggestions.
    4. Explore the recommended movies in the table, complete with genres, short summaries, and IMDB scores!
    5. Learn about why each movie was recommended and discover interesting trivia about them.

    Get ready to discover your next cinematic adventure!
    """)

    # Display some movie trivia or fun facts
    st.subheader("Did You Know?")
    movie_facts = [
        "The longest film ever made is 'Logistics' (2012), with a runtime of 857 hours.",
        "The Wilhelm Scream has been used in over 400 films and TV series.",
        "The first feature-length animated movie was 'Snow White and the Seven Dwarfs' (1937).",
        "The highest-grossing film of all time is 'Avatar' (2009), earning over $2.8 billion worldwide."
    ]
    for fact in movie_facts:
        st.markdown(f"- {fact}")