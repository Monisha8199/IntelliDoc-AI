import streamlit as st
import sqlite3

# Connect to Database
conn = sqlite3.connect("database/intellidoc.db", check_same_thread=False)
cursor = conn.cursor()

st.title("🔐 IntelliDoc AI Login")

menu = ["Login", "Register"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Register":

    st.subheader("Create New Account")

    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):

        try:
            cursor.execute(
                "INSERT INTO users(username,email,password) VALUES(?,?,?)",
                (username, email, password)
            )

            conn.commit()

            st.success("Account Created Successfully ✅")

        except:
            st.error("Username or Email already exists!")

elif choice == "Login":

    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )

        data = cursor.fetchone()

        if data:
            st.success("Login Successful ✅")
        else:
            st.error("Invalid Username or Password")