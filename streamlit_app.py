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
my_fruit_list = my_fruit_list.set_index('Fruit')
# lets put pick list
fruits_selected = streamlit.multiselect("Pick some Frutis:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on the page 

streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvice Fruit Advice!') 
fruit_choice=streamlit.text_input('what gruit would yuo like information about?','apple')
streamlit.write('The user entered',fruit_choice)

import requests
fruitvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
 
fruityvice_normalized = pandas.json_normalize(fruitvice_response.json())
streamlit.dataframe(fruityvice_normalized)

streamlit.header('Snowflake Connection!') 

import snowflake.connector

