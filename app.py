import streamlit as st

st.title("Hello I am KIRA")
st.subheader("I am Light Yagami")
st.text("I am Student")
st.write("I am Human")

drink = st.selectbox("You Fav drink: ", ["Tea", "Coffee", "fruit Juice", "Mocktail"])
st.write(f"You choose {drink} excellent choice")

st.success(f"Your {drink} is ready")