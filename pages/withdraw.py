import streamlit as st
def main():
    st.title("In order to get paid please enter your phone number on which your UPI works..")
    Paymentnumber=["Payment number"]
    choice=st.sidebar.selectbox("Payment number",Paymentnumber)
    if choice == "Payment number":
        # st.subheader("")
        # new_user = st.text_input("Username")
	email_sender=st.text_input("E-mail(Enter the E-mail id by which you sent the PDF of your Ebook")
        payment_id = st.text_input("Payment number")

        if st.button("Done"):print(payment_id)
           
import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data
if __name__=='__main__':
	main()
