import streamlit as st
import requests
from streamlit_lottie import st_lottie
import pickle
from pathlib import Path
import streamlit_authenticator as stauth

st.set_page_config(page_title="ANTI-MATRIX.com",page_icon="🗿",layout="wide")
page_bg_img="""
<style>
[data-testid="stAppViewContainer"]{
background-color: #FFFFFF;
opacity: 0.8;
background-image:  linear-gradient(135deg, #8bf745 25%, transparent 25%), linear-gradient(225deg, #8bf745 25%, transparent 25%), linear-gradient(45deg, #8bf745 25%, transparent 25%), linear-gradient(315deg, #8bf745 25%, #1f1f75 25%);
background-position:  10px 0, 10px 0, 0 0, 0 0;
background-size: 20px 20px;
background-repeat: repeat;

}
</style>
"""




#  #--------- HEADER SECTION----------------
st.title("Escape the MATRIX . Get a lifestyle . ")
st.subheader('''this site is a id for you which mentions you as a person who is not under MATRIX.''')
st.write("""
We the teenagers want to get a good lifestyle but never taught how to do so. 
This site is specially for teenagers as we can find many sites which say that they will give 
some xyz amount of money , but they don't .
This is my own experience and i want you all to put efforts in order to achieve success.
It is my humble request that don't use this as addiction can happen .
2-3 times a week is great .

""")
st.subheader("You can play this legendary song and listen . You can download by clicking on 3 dots.")
import numpy as np

audio_file = open('audio/Theme.mp3', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes)

sample_rate = 44100  
seconds = 2  
frequency_la = 440  
t = np.linspace(0, seconds, seconds * sample_rate, False)
note_la = np.sin(frequency_la * t * 2 * np.pi)

# st.audio(note_la, sample_rate=sample_rate)

url = requests.get(
    "https://assets7.lottiefiles.com/packages/lf20_OdVhgq.json")
url_json = dict()
if url.status_code == 200:
    url_json = url.json()
else:
    print("Error in URL")
  
  
# st.title("Adding Lottie Animation in Streamlit WebApp")
  
st_lottie(url_json,
          # change the direction of our animation
          reverse=True,
          # height and width of animation
          height=400,  
          width=400,
          # speed of animation
          speed=1,  
          # means the animation will run forever like a gif, and not as a still image
          loop=True,  
          # quality of elements used in the animation, other values are "low" and "medium"
          quality='high',
           # THis is just to uniquely identify the animation
          key='Car' 
          )
with st.container():
    left_column,right_column=st.columns(2)
    
primaryColor="#F63366"
backgroundColor="#BC986A"
secondaryBackgroundColor="#FBEEC1"
textColor="#262730"
font="serif"
