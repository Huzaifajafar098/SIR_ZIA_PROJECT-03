# PASSWORD STRENGHT METER
# PROJECT_03

import re
import streamlit as st

# page styling 
st.set_page_config(page_title="Password Strenght Checker By Huzaifa Jafaf", page_icon="🌘",layout="centered")

# cusom css
st.markdown("""
<style>
       .main {text-aling: center;}
       .stTextInput {widht: 60% ! important; margine: auto; }
       .stButton button {widht: 50%; background-color #4CAF50; color: white; font-size: 18px; }
       .stButton button : hover {background-color: #45a049;}
</style>
""", unsafe_allow_html=True)

# Page title and description
st.title("Password Strenght Generator")
st.write("Enter Your Password Below To Check Its Security Level.🔍")

# function to check password strenght
def check_password_strenght(password):
    score = 0
    feedback = []

    if len(password) >= 8:
         score += 1   #increased
    else:
         feedback.append("❌ Password Should Be **atleast 8 Character Long**.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]",password):
         score += 1 
    else:
         feedback.append("❌ Password Should Include **Both Uppercase(A-Z) and lowercase (a-z) letters**.")
    if re.search(r"\d", password):
         score += 1
    else:
         feedback.append("❌ Password Should  Include **at least one number (0-9) **. ")


            #special character
    if re.search(r"[!@#$%^&*]",password):
        score += 1
    else:
         feedback.append("❌ Include **at least one special character (!@#$%^&*)**.")

# display password stenght result
    if score == 4:
     st.success("✔️ **Strong Password** Your Password is Secure.")
    elif score == 3:
        st.info(" ⚠️ **Moderate Password** - Consider Improvng Security By adding more feature")
    else:
        st.error("❌**Week Password** - Follow the suggestion below to strenght it.")


    # feedback        
    if feedback:
        with st.expander("🔍**Improving Your Password** "):
            for item in feedback:
                st.write(item) 
password = st.text_input("Enter Your Password:", type="password", help="Ensure Your Password Is Strong🔐")


# Button Working
if st.button("Check strenght"):
    if password:
        check_password_strenght(password)
    else:
        st.warning(" ⚠️ Please Enter a Password First")   #show warning if password
