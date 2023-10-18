#!/usr/bin/env python
# coding: utf-8

# In[1]:
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# In[3]:

st.title("Machine Learning App")
st.sidebar.title("Data Entry Panel")
st.sidebar.slider("Income level", 10000, 1000000)

option = st.sidebar.selectbox('How would you like to be contacted?',('Email', 'Home phone', 'Mobile phone'))
if option == 'Email':
    st.write("Provide your E-mail-ID")
elif option == "Home phone":
    st.write(" Provide your Home contact number")
else:
    st.write("Provide your Mobile Number")
    
agree = st.sidebar.checkbox('I agree')

if agree:
    st.write('Great!')

if st.sidebar.button('Say hello'):
    st.write('Hello, How are you?')



genre = st.sidebar.radio("What\'s your favorite movie genre",('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
      st.write('You selected comedy.')
else:
     st.write("You didn\'t select comedy.")

df = pd.read_csv("mtcars.csv")   

cars = st.sidebar.button("cars data")
if cars:
      st.write(df)
      fig,ax = plt.subplots()
      #plt.boxplot(df["mpg"])
      plt.hist(df["mpg"])
      st.pyplot(fig)
      plt.show()
        
# In[ ]:

# In[ ]:




