import streamlit as st
import requests

st.title("Hello I am KIRA")
st.subheader("I am Light Yagami")
st.text("I am Student")
st.write("I am Human")

drink = st.selectbox("You Fav drink: ", ["Tea", "Coffee", "fruit Juice", "Mocktail"])
st.write(f"You choose {drink} excellent choice")

st.success(f"Your {drink} is ready")

if st.button("Make Chai"):
    st.success("Chai is being brwed")

add_masala = st.checkbox("add masala")
if add_masala:
    st.text("Masala added to your chai")

tea_type = st.radio("Pick chai", ["Ginger", "Lemon", "Elaichi"])

st.write(f"You choose {tea_type} chai nice choice")

flavor = st.selectbox("Enter your fav flavor", ["adrak", "lemon", "elaichi", "tulsi", "kesari"])
st.write(f"You choose {flavor} flavor")

sugar = st.slider("Sugar level (table spoon)", 0, 10, 1)
st.write(f"You choose {sugar} tsp sugar")   

cups = st.number_input("How many cups", min_value= 1, max_value= 10, step= 1)
st.write(f"You order {cups} cups of chai")

name = st.text_input("Enter your name: ")
if name:
    st.write(f"Hello {name} your chai is on the way")

dob = st.date_input("Enter you DOB")
st.write(f"Your DOB is {dob}")








# Currency Converter


st.title("Currency Converter")
enter_amount_INR = st.number_input("Enter Amount in INR", min_value=1, step=1)
to_currency = st.selectbox("To Currency", ["USD", "INR", "EUR", "GBP", "AUD", "CAD", "SGD", "JPY", "CNY"])

if st.button("Convert"):
    url = f"https://v6.exchangerate-api.com/v6/32d00dc9835516c2c908e62f/latest/INR"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rate = data["conversion_rates"][to_currency]
        converted_amount = enter_amount_INR * rate
        st.success(f"{enter_amount_INR} INR = {converted_amount:.2f} {to_currency}")
    else:
        st.error("Failed to Fetch conversion rates.")