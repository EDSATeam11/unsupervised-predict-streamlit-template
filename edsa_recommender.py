"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np
from pathlib import Path

# Custom Libraries
from app_functions import *
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

#def read_markdown_file(markdown_file):
    #return Path(markdown_file).read_text()

team = read_markdown_file("meet_the_team.html") 
slides = read_markdown_file("slides.html") 
solution = read_markdown_file("solution_overview.html")  

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Solution Overview", "Data analysis and plots",
                    "Meet the team", "Pitch"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        #movie_1 = st.selectbox('Fisrt Option',title_list[1493:1520])
        #movie_2 = st.selectbox('Second Option',title_list[2110:2120])
        #movie_3 = st.selectbox('Third Option',title_list[2110:2120])
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.markdown(solution, unsafe_allow_html=True)

    if page_selection == "Data analysis and plots":
        st.title("Data analysis") 
        if st.checkbox("Ratings insights"):
            st.subheader("These plots give insights about the ratings given for the movies")
            st.write("The most common rating is 4 with over 2.5 million ratings")
            st.image("resources/imgs/plots/number_of_ratings.png", width=500)
            st.image("resources/imgs/plots/ratings_distribution.png", width=500)
            st.write("These are the highest rated movies. We have selected the top 20")
            st.image("resources/imgs/plots/highest_rated_movies.png", width=500)
        if st.checkbox("Movie insights"):
            st.subheader("A number of factors influence movie choices and below we take a look at \
                        some of those factors such as popular themes, actors, directors and era")
            st.write("The longest movie is 246 minutes long")
            st.image("resources/imgs/plots/movie_runtime.png", width=500)
            st.write("Genres with the highest number of movies were drama, comedy, action and thriller")
            st.image("resources/imgs/plots/number_of_movies_by_genre2.png", width=500)
            st.write("The majority of movies in our database were released in the 1900s")
            st.image("resources/imgs/plots/movies_per_era.png", width=500)
            st.write("These are the most popular themes.")
            st.image("resources/imgs/plots/wordcloud2.png", width=500)
            st.image("resources/imgs/plots/top_20_directors.png", width=500)
            #st.image("resources/imgs/plots/director_movies.png", width=500)
            st.image("resources/imgs/plots/frequent_actors.png", width=500)


    if page_selection == "Pitch":
        st.title("Pitch slide deck")
        st.markdown(slides, unsafe_allow_html=True)

    if page_selection == "Meet the team":
        st.title("Meet the team")
        st.markdown(team, unsafe_allow_html=True)
        local_css('html_style.css')

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.



if __name__ == '__main__':
    main()
