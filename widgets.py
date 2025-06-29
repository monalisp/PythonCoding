import streamlit as st
import pandas as pd
st.title("Streamlit text input")
name=st.text_input("Enter your name:")
age=st.slider("Select your age:",0,100,25)
st.write(f"Your age is {age}.")

options=["Python","Java","C++","Javascript"]
choice=st.selectbox("Choose your favourite language:",options)
st.write(f"You selected {choice}.")
if name:
    st.write(f"Hello, {name}")

data = {
    "Name":["John","Jale","Jake","Jelly"],
    "Age" :[20,25,60,34],
    "City":["Outram Park","Tanah Mehra","Clarke Quay","Havelock"]
}
df = pd.DataFrame(data)
df.to_csv(data.csv)
st.write(df)
uploaded_file=st.file_uploader("Choose a csv file",type="csv")
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)