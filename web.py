import streamlit as st
import requests
from streamlit_lottie import st_lottie
import json 
st.set_page_config(page_title="Happy Birthday Div",page_icon=":sparkling_heart:",layout="wide")
page_bg_img="""
<style>
[data-testid="stAppViewContainer"]{
background-color: #1f1f75;
opacity: 0.8;
background-image:  linear-gradient(135deg, #8bf745 25%, transparent 25%), linear-gradient(225deg, #8bf745 25%, transparent 25%), linear-gradient(45deg, #8bf745 25%, transparent 25%), linear-gradient(315deg, #8bf745 25%, #1f1f75 25%);
background-position:  10px 0, 10px 0, 0 0, 0 0;
background-size: 20px 20px;
background-repeat: repeat;

}
</style>
"""

 #--------- HEADER SECTION----------------
def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json
def load_lottiefile(filepath:str):
    with open(filepath,"r")as f:
        return json.load(f)
lottie_coding=load_lottiefile("lottiefiles/bday.json")
lottie_birthday=load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_nguy2ppj.json")
# st.subheader("CONGRATULATIONS ")
st.title("-----Happy Birthday Divyanshi 🎉-----")
st.write('''Congratulations for your 14th Birthday , May god bless you......''')
st_lottie(lottie_coding,
    speed=1,
    reverse=False,
    loop=True,
    quality='low',
    height=None,
    width=None,
    key=None)
# with st.container():
#     left_column,right_column=st.columns(2)
#     with right_column:
#         st.write(st_lottie(lottie_birthday, height=300))