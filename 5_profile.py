import streamlit as st
import datetime

st.set_page_config(page_title="Profile", layout="wide")

# --- SESSION INIT ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = True
    st.session_state.user_name = "Deepanshu"
    st.session_state.user_email = "deepanshu@gmail.com"
    st.session_state.user_address = "SVECW , Bhimavaram"
    st.session_state.user_dob = "2002-01-01"

# --- TITLE ---
st.title("👤 My Profile")
st.markdown("---")

# --- PROFILE INFO ---
col1, col2 = st.columns([1, 3])

with col1:
    st.write("### Name:")
    st.write(st.session_state.user_name)
    st.write("### Email:")
    st.write(st.session_state.user_email)
    st.write("### Address:")
    st.write(st.session_state.user_address)
    if st.button("✏️ Edit Profile"):
        st.session_state.edit_profile = True

with col2:
    st.write("### My Activity Overview")
    st.success("🥳 You're a valued customer! Keep customizing cakes 🎂")

# --- EDIT PROFILE FORM ---
if "edit_profile" in st.session_state and st.session_state.edit_profile:
    st.markdown("### ✏️ Update Profile Information")
    with st.form("edit_profile_form"):
        name = st.text_input("Full Name", value=st.session_state.user_name)
        email = st.text_input("Email", value=st.session_state.user_email)
        address = st.text_input("Address", value=st.session_state.user_address)
        dob = st.date_input("Date of Birth", value=datetime.date.fromisoformat(st.session_state.user_dob))
        submitted = st.form_submit_button("Save Changes")
        if submitted:
            st.session_state.user_name = name
            st.session_state.user_email = email
            st.session_state.user_address = address
            st.session_state.user_dob = dob.isoformat()
            st.success("Profile updated successfully!")
            st.session_state.edit_profile = False
            st.rerun()

st.markdown("---")

# --- ACTIVITY SECTION ---
st.subheader("🍰 My Cake Activity")
cols = st.columns(2)

with cols[0]:
    with st.container(border=True):
        st.write("### 📜 History")
        st.write("View all your previous orders and feedback.")
        if st.button("View History", key="history"):
            st.switch_page("pages/4_History.py")

    with st.container(border=True):
        st.write("### 🛒 Cart")
        st.write("Check items you've added to your cart.")
        if st.button("Open Cart", key="cart"):
            st.switch_page("pages/cart.py")

    with st.container(border=True):
        st.write("### 🚚 Track Delivery")
        st.write("Track your recent cake orders here.")
        if st.button("Track Delivery", key="tracking"):
            st.switch_page("pages/delivery_tracking.py")

with cols[1]:
    with st.container(border=True):
        st.write("### 🏪 Explore Stores") 
        st.write("Find cake shops near your location.")
        if st.button("Browse Stores", key="stores"):
            st.switch_page("pages/2_store_listing.py")

    with st.container(border=True):
        st.write("### 💳 Checkout & Payment")
        st.write("Securely finish your current order.")
        if st.button("Proceed to Checkout", key="checkout"):
            st.switch_page("pages/checkout.py")

    with st.container(border=True):
        st.write("### 🔒 Logout")
        st.write("End your session securely.")
        if st.button("Logout", key="logout"):
            st.session_state.clear()
            st.success("You’ve been logged out.")
            st.stop()
