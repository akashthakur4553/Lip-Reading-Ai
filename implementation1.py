# import cv2
# import mediapipe as mp
import streamlit as st
from streamlit_option_menu import option_menu
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from firebase_admin import auth
import pyautogui
import subprocess
import os
import time

import re

# face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")
global Start_app
Start_app = "yes"
if not firebase_admin._apps:
    cred = credentials.Certificate("lipreadingaiauth-e45d0bba0b3e.json")
    firebase_admin.initialize_app(cred)


def su():
    # try:
    # cred = credentials.Certificate("lipreadingaiauth-e45d0bba0b3e.json")
    # firebase_admin.initialize_app(cred)
    pat = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
    if len(password_) >= 6 and re.match(pat, email_):
        try:
            user = auth.create_user(email=email_, password=password_, uid=username)
            st.success("Account created successfully!")
            st.markdown("Please Login using your email and password")
            st.balloons()
        except:
            st.warning("Sign Up Failed as email already exists")
    else:
        st.warning("Please enter a valid email and password(minimum 6 characters)")


def Lu():
    global Start_app
    pat = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
    Start_app = "yes"
    if len(password) >= 6 and re.match(pat, email):

        # streamlit.web.bootstrap.run("streamlitapp.py", "", [], [])
        try:
            user = auth.get_user_by_email(email)
            st.success(f"Logged In successfully! Welcome   {user.uid}")
            Start_app = "yes"
            st.balloons()

            process = subprocess.Popen(["streamlit", "run", "streamlitapp.py"])
            time.sleep(5)
            pyautogui.hotkey("ctrl", "w")

        # streamlit.web.bootstrap.run("streamlitapp.py", "", [], [])
        # st.text(f"starting {Start_app}")

        except:
            st.warning("Login Failed")
    else:
        st.warning("kindly enter a valid username and password")


with st.sidebar:
    detection_type = option_menu(
        menu_title="Lip Reading AI",
        options=["Home", "Account"],
        icons=["house-fill", "person-circle"],
        menu_icon=":lips:",
        default_index=1,
        styles={
            "container": {"padding": "5!important", "background-color": "black"},
            "icon": {"color": "white", "font-size": "23px"},
            "nav-link": {
                "color": "white",
                "font-size": "20px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "blue",
            },
            "nav-link-selected": {"background-color": "light blue"},
        },
    )


# st.sidebar.title("Lip Reading AI Sidebar")
# st.sidebar.subheader("DashBoard")

# detection_type = st.sidebar.selectbox(
#     "Choose the App mode", ["About APP", "Run on Video", "Open Webcam"]
# )

if detection_type == "Home":
    st.title("Lip Reading AI")
    st.markdown(
        "This Application helps reading the lip movements from  VIDEO depending on your App mode. "
    )
    st.markdown(
        """
    About the Author: \n
    Hey this is Syntax Error from SJCEM.\n

    This APP help in reading the lips in a video or in real time.


    SAMPLE OUTPUT:
    """
    )

    st.video("https://youtu.be/NGmJ5T3mXYU?si=Lx3kkghMYFAnnwq4")


elif detection_type == "Run on Video":
    pass

elif detection_type == "Open Webcam":
    pass


elif detection_type == "Account":
    st.title("Welcome to Lip Reading AI :lips:")
    choice = st.selectbox("Login/Signup", ["Login", "Sign up"])
    if choice == "Login":
        email = st.text_input("Email Address")
        password = st.text_input("Password", type="password")
        st.button("Login", on_click=Lu)
    else:
        username = st.text_input("Enter  your unique username")
        email_ = st.text_input("Email Address")
        password_ = st.text_input("Password", type="password")
        st.button("Create New Account", on_click=su)
        # if st.button("Create New Account"):
        #     user = auth.create_user(email=email_, password=password_, uid=username)
        #     st.success("Account created successfully!")
        #     st.markdown("Please Login using your email and password")
        #     st.balloons()
