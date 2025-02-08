import streamlit as st
import pandas as pd
import numpy as np
import requests

st.title("hello")

st.write("This is a steamlit app")

url_1 = "https://iran-locations-api.ir/api/v1/fa/cities"
cities = []
recponse = requests.get(url_1)
recponse = recponse.json()

for i in recponse:
    cities.append(i["name"])


x = st.selectbox("Enter source city", cities)
st.write(f"your choce is {x}")

y = st.selectbox("Enter sourcdestionalitione city", cities)
st.write(f"your choce is {y}")

def calculate_distance(x,y):
    url = "https://api.codebazan.ir/distance/index.php?"
    
    parameters = {
        "mabda" : x,
        "maghsad": y
    }
    responce = requests.get(url, params=parameters)
    return responce.content.decode()

# if __name__ == "__main__":
#     x = input("Enter source city: ")
#     y = input("enter destionalition city: ")
st.write(calculate_distance(x, y))
