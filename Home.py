import streamlit as st
import requests
from streamlit_lottie import st_lottie
import pickle
from pathlib import Path
import streamlit_authenticator as stauth

st.set_page_config(page_title="GoTeen.com",page_icon="🗿",layout="wide")
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
with st.container():
    left_column,right_column=st.columns(2)
    
    with left_column:
    #  #--------- HEADER SECTION----------------
      st.title("Escape the MATRIX . Get a lifestyle . ")
    #   st.subheader('''this site is a id for you which mentions you as a person who is not under MATRIX.''')
      st.write("""
      We the teenagers want to get a good lifestyle but never taught how to do so. 
This site is specially for teenagers as we can find many sites which say that they will give 
some xyz amount of money , but they don't .
This is my own experience and i want you all to put efforts in order to achieve success.
It is my humble request that don't use this as addiction can happen .
2-3 times a week is great .

   """)
      st.title("Write Ebooks and Earn Money .")  
      st.subheader("This site is specially for teenagers (13-19).")  
      st.write("Kindly upload an Ebook Written by you (scanned), and send pdf file of your ebook on E-mail on antimatrix012@gmail.com after checking out withdrawl section and completing that process you will be paid money your skills and ebook deserves...")  
      #st.subheader("You can play this legendary song and listen . You can download by clicking on 3 dots.")

   # st.audio(note_la, sample_rate=sample_rate)
    with right_column:
       url = requests.get("https://assets7.lottiefiles.com/packages/lf20_OdVhgq.json")
       url_json = dict()
       if url.status_code == 200:url_json = url.json()
       else: print("Error in URL")
  
  
# st.title("Adding Lottie Animation in Streamlit WebApp")
  
       st_lottie(url_json,
          # change the direction of our animation
          reverse=False,
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
       st.subheader("Quotes.....")
       st.write("""Indeed, the self-made millionaire is a shining example of what can 
                be for a great many of us dreamers. So, in honor of those who started
                 from the same humble beginnings as the rest of us, but have managed to claw their way
                 to the financial status we all deep down aspire to achieve, we've pulled together this list 
                 of catalyzing quotes from a handful of well-known self-made millionaires. May they inspire you 
                to continue to strive towards your journey of becoming rich and achieving the self-made
                 millionaire status.
                """)    

    

