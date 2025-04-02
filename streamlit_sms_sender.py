import streamlit as st
import requests
import random

# API Setup
API_KEY = "8hDLLw2xZAT8CNpFEDdj"
BASE_URL = "http://bulksmsbd.net/api"
SENDER_ID = "8809617625214"

# SMS Templates
SMS_TEMPLATES = {
    "Greetings SMS": "Thanks for calling BAYAS! We're here to assist you with your computer needs. Stay tuned for more updates.",
    "Confirm SMS": "Thank you! A BAYAS technician will be assigned shortly to resolve your PC issue. We appreciate your patience.",
    "Thanks SMS": "Thanks for choosing BAYAS! Share your feedback: https://g.page/r/CQ8V96C6Lf8nEBM/review | Your Invoice: #INV-{random8}"
}

# SMS Sender Function
def send_sms(number, message):
    url = f"{BASE_URL}/smsapi"
    payload = {
        "api_key": API_KEY,
        "type": "text",
        "number": number,
        "senderid": SENDER_ID,
        "message": message
    }
    response = requests.get(url, params=payload)
    return response

# UI
st.set_page_config(page_title="BAYAS SMS Sender", page_icon="📲")
st.title("📲 BAYAS SMS Sender")

st.markdown("Enter a Bangladeshi phone number and choose a message template to send an SMS.")

with st.form("sms_form"):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.text_input("Country Code", value="88", disabled=True)
    with col2:
        user_number = st.text_input("Phone Number (11 digits, starts with 01)", max_chars=11, placeholder="01XXXXXXXXX")

    template_name = st.selectbox("Select a Template", list(SMS_TEMPLATES.keys()))
    submitted = st.form_submit_button("Send SMS")

if submitted:
    if len(user_number) == 11 and user_number.startswith("01"):
        full_number = "88" + user_number
        message = SMS_TEMPLATES[template_name]

        if "{random8}" in message:
            rand_num = random.randint(10000000, 99999999)
            message = message.replace("{random8}", str(rand_num))

        response = send_sms(full_number, message)

        if response.status_code == 200:
            st.success("✅ SMS sent successfully!")
            st.code(response.text)
        else:
            st.error("❌ Failed to send SMS.")
            st.code(response.text)
    else:
        st.warning("⚠️ Please enter a valid 11-digit Bangladeshi number starting with 01.")

ip = requests.get('https://api.ipify.org').text
print("Your public IP is:", ip)