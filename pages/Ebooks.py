import streamlit as st
import os
import pandas
import smtplib
from os.path import basename
from socket import gethostname
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
from streamlit_lottie import st_lottie
import requests

with st.container():
    left_column,right_column=st.columns(2)
   
    with left_column:
        st.title("Write Ebooks and Earn Money .")
        st.subheader("This site is specially for teenagers (13-19).")
        st.write ("""
Kindly upload an Ebook Written by you (scanned),
and send pdf file of your ebook on E-mail on antimatrix012@gmail.com
after checking out withdrawl section and completing that process you will be paid
money your skills and ebook deserves...
        """)
    with right_column:
        url = requests.get(
        "https://assets4.lottiefiles.com/packages/lf20_yg29hewu.json")
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

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    # st.write(bytes_data)

st.write ("Please send pdf file of your ebook on E-mail on antimatrix012@gmail.com ")
import sqlite3 
import hashlib

# st.write("you can write e book here and then copy this and paste it wherever you want/n and make a pdf and upload or send email")   
# def main():
#     # new_ebook = st.text_input("Write Your Ebook Here")
#     label="Write Your Ebook Here.(This page can be extended from the right-bottom part of this page)"

    # st.text_area(label, value='', height=1000, max_chars=None, key=None)
  
   

					
from fpdf import FPDF
import base64
label="""Write Your Ebook Here.(This page can be extended from the right-bottom part of this page),
donot Copy paste , if you do you will not be paid . 
"""

report_text = st.text_area(label, value='', height=600, max_chars=None, key=None)


export_as_pdf = st.button("Download this Ebook and then do the drag file ")

def create_download_link(val, filename):
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'

if export_as_pdf:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, report_text)
    
    html = create_download_link(pdf.output(dest="S").encode("latin-1"), "test")

    st.markdown(html, unsafe_allow_html=True)            
    
            

# if __name__=='__main__':
#     main()
