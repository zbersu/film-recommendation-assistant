# Movie Recommendation System - README

## Overview

**Movie Recommendation System** is a Streamlit web application that provides personalized movie suggestions based on user preferences. The app utilizes OpenAI's GPT-4o-mini model to generate tailored recommendations, complete with explanations and interesting trivia about each suggested movie.

## Features

- Custom gradient background for a visually appealing interface
- Genre selection from a curated list of popular movie genres
- Input for user's top 3 favorite movies
- AI-powered movie recommendations using GPT-4o-mini
- Presentation of recommendations in a clear, markdown-formatted table
- Explanations for why each movie was recommended
- Interesting trivia facts about each recommended movie
- Additional movie facts displayed when no recommendations are shown

## Prerequisites

- Python 3.x
- pip (Python package installer)
- OpenAI API key
- Python packages listed in requirements.txt

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/zbersu/film-recommendation-assistant.git
    cd film-recommendation-assistant
    ```

2. **Create a Virtual Environment**

    On Windows:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

    On macOS and Linux:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**

    ```bash
    pip install requirements.txt
    ```

4. **Set Up Environment Variables**
   Add your OpenAI API key to the `.env` file in the root directory of the project:
    ```bash
    OPENAI_API_KEY=<your_api_key_here>
    ```
## Running the App

To run the Streamlit application, execute the following command in your terminal:

```bash
streamlit run main.py
```
The app will open in your default web browser.

To stop the app, press `Ctrl+C` in the terminal where it's running.

## How to Use

1. Select your favorite movie genres from the sidebar.
2. Enter your top 3 favorite movies in the provided input fields.
3. Click "Get Recommendations" to receive personalized movie suggestions.
4. Explore the recommended movies in the table, complete with genres, short summaries, and IMDB scores.
5. Read about why each movie was recommended and discover interesting trivia about them.

## Customization

* Adjust the custom CSS in the `st.markdown()` function to modify colors, gradient, or layout.
* Modify the genre list in the `st.sidebar.multiselect()` function to change available genres.
* Update the `movie_facts` list to add or change the displayed movie trivia.

## Troubleshooting

* If you encounter any issues with missing modules, ensure you've activated the virtual environment and installed all dependencies.
* If the OpenAI API doesn't work, check that your API key is correctly set in the `.env` file.
* For any other issues, please check the Streamlit documentation or open an issue in the project repository.

## Contributing

Contributions to the Movie Recommendation System are welcome! Please feel free to submit a Pull Request.

## Acknowledgements

* OpenAI for providing the GPT-4o-mini model
* Streamlit for the excellent web app framework

Enjoy discovering your next favorite movie with the Movie Recommendation System!