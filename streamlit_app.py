import streamlit
streamlit.title('Indian Oreo  Healthy Diner')
streamlit.header('Breakfast Menu') 
streamlit.text('Idli')
streamlit.text('Dosa')
streamlit.text('Upma')
streamlit.text('Pongal')
streamlit.text('Poori')
streamlit.text('Tea')
streamlit.text('Cofee')

streamlit.header('Make Your Orio') 
streamlit.text('🍌 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.text('🥝🍇 kale Spinach & Rocket Smoothie 🍌🥭')
streamlit.text('🍌🥭Avacado Upma smoothie 🥝🍇')

streamlit.header('Specials')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)


