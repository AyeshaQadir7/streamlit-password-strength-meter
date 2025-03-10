import streamlit as st
import re

# Streamlit UI
st.set_page_config(page_title="Password Strength Meter", page_icon="🔒")
st.title("🔒 Password Strength Checker")
st.markdown("""
Welcome to the Password Strength Checker! This tool helps you evaluate the security of your password by analyzing its length, character variety, and complexity.
#### Try it now and make your passwords stronger! 💪
""")

def check_password_strength(password):
    feedback = []
    score = 0
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain both upper and lower case characters.")
    
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one digit.")
    
    if re.search(r'[!@#$%^&*()_+={}:;"<>?/.,]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one special character (!@#$%^&* etc.).")
    
    return score, feedback


# User Input
password = st.text_input("Enter your password", type="password")

if password:
    score, feedback = check_password_strength(password)
    
    # Display strength message
    if score == 4:
        st.success("✔ Your password is strong!")
    elif score == 3:
        st.warning("🟡 Your password is medium strength. It could be stronger.")
    else:
        st.error("🔴 Your password is weak. Please make it stronger.")
    
    # Display improvement suggestions
    if feedback:
        st.markdown("## Improvement Suggestions")
        for tip in feedback:
            st.write(tip)
else:
    st.info("Please enter your password to get started.")
