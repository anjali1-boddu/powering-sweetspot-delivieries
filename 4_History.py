"""#fff0f5"""
import streamlit as st
from datetime import datetime

# Set page configuration
st.set_page_config(page_title="Cake Order History", page_icon="🎂", layout="wide")

# Inject custom CSS for background color and layout
st.markdown("""
    <style>
    /* Set entire page background color */
    .stApp {
        background-color: #FFC0CB;
    }

    /* Style the order cards */
    .order-card {
        background-color: white;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        margin-bottom: 25px;
    }

    /* Style buttons */
    .stButton > button {
        background-color: #ff4d6d;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 8px 20px;
        border: none;
    }

    /* Style headers */
    h1, h3 {
        color: #cc0066;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Sample order history data
orders = [
    {
        "Order ID": "ORD12345",
        "Cake": "Chocolate Truffle",
        "Customization": "Heart Shape, Happy Birthday text",
        "Image": "images/chocolate_cake.jpg",
        "Delivery Address": "123, MG Road, Hyderabad",
        "Order Date": "2025-07-18",
        "Status": "Delivered"
    },
    {
        "Order ID": "ORD12346",
        "Cake": "Vanilla Rainbow",
        "Customization": "Photo Printed, Eggless",
        "Image": "images/black_current.webp",
        "Delivery Address": "56, Beach Road, Vizag",
        "Order Date": "2025-07-22",
        "Status": "Out for Delivery"
    },
    {
        "Order ID": "ORD12347",
        "Cake": "Red Velvet",
        "Customization": "Heart Shape, Anniversary Text",
        "Image": "images/redvelvet.jpg",
        "Delivery Address": "88, Main Street, Vijayawada",
        "Order Date": "2025-07-24",
        "Status": "Preparing"
    }
]

# Header section
st.markdown("<h1>🎂 Cake Order History</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>See your past cake orders with customizations and delivery status.</p>", unsafe_allow_html=True)
st.markdown("---")

# Display each order in a styled card
for order in orders:
    with st.container():
        st.markdown("<div class='order-card'>", unsafe_allow_html=True)
        cols = st.columns([1, 2, 2, 1])
        with cols[0]:
            st.image(order["Image"], width=130)
        with cols[1]:
            st.subheader(order["Cake"])
            st.write(f'**Order ID**: {order["Order ID"]}')
            st.write(f'**Customizations**: {order["Customization"]}')
            st.write(f'**Order Date**: {order["Order Date"]}')
        with cols[2]:
            st.write(f'**Delivery Address**: {order["Delivery Address"]}')
            st.write(f'**Status**: {order["Status"]}')
            if order["Status"] == "Delivered":
                st.success("🎉 Delivered")
            elif order["Status"] == "Out for Delivery":
                st.warning("🚚 Out for Delivery")
            else:
                st.info("🧁 Preparing")
        with cols[3]:
            st.button("Reorder", key=order["Order ID"])
        st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Thank you for using our Cake Customization & Delivery Service 💖</p>", unsafe_allow_html=True)