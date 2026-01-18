import streamlit as st
import sqlite3
from datetime import datetime
import pytz

from database import init_db
from auth import register, login
from sos_detector import detect_sos
from alert import send_alert
from utils.location import get_ip_and_location

init_db()

st.set_page_config(page_title="Emergency SOS", layout="wide")

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}
.stButton>button {
    background: #22c55e;
    color: white;
    border-radius: 10px;
    padding: 10px;
}
.stButton>button:hover {
    background: #16a34a;
}
.stTextInput>div>div>input {
    border-radius: 10px;
    padding: 10px;
    border: 1px solid #334155;
    background: #0b1220;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.title("🚨 Emergency SOS System")

# Session
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "refresh" not in st.session_state:
    st.session_state.refresh = False

# Login/Register
if not st.session_state.logged_in:
    tab1, tab2 = st.tabs(["🔐 Login", "🧾 Register"])

    with tab1:
        st.subheader("Login")
        username = st.text_input("Username", key="login_user")
        password = st.text_input("Password", type="password", key="login_pass")

        if st.button("Login"):
            user = login(username, password)
            if user:
                st.session_state.logged_in = True
                st.session_state.user_id = user[0]
                st.session_state.username = username
                st.success("Logged in!")
                st.session_state.refresh = not st.session_state.refresh
                st.stop()
            else:
                st.error("Wrong credentials")

    with tab2:
        st.subheader("Register")
        r_username = st.text_input("New Username", key="reg_user")
        r_password = st.text_input("New Password", type="password", key="reg_pass")

        if st.button("Register"):
            register(r_username, r_password)
            st.success("Registered! Please login.")
            st.session_state.refresh = not st.session_state.refresh
            st.stop()

else:
    st.success(f"Logged in as {st.session_state.username}")

    col1, col2 = st.columns([2, 3])

    with col1:
        st.subheader("Emergency Contacts (1–3)")

        conn = sqlite3.connect("sos.db")
        c = conn.cursor()
        c.execute(
            "SELECT id, name, phone, telegram_id, email FROM contacts WHERE user_id=?",
            (st.session_state.user_id,)
        )
        contacts = c.fetchall()
        conn.close()

        if len(contacts) == 0:
            st.warning("You must add at least 1 contact to use SOS.")

        for contact in contacts:
            st.write(f"**{contact[1]}** | 📞 {contact[2]} | ✉️ {contact[4]} | 🟦 {contact[3]}")
            if st.button(f"Delete {contact[1]}", key=f"del_{contact[0]}"):
                conn = sqlite3.connect("sos.db")
                c = conn.cursor()
                c.execute("DELETE FROM contacts WHERE id=?", (contact[0],))
                conn.commit()
                conn.close()
                st.session_state.refresh = not st.session_state.refresh
                st.stop()

        if len(contacts) < 3:
            st.write("---")
            st.write("Add new contact")

            name = st.text_input("Contact Name", key="c_name")
            phone = st.text_input("Phone (optional)", key="c_phone")
            telegram_id = st.text_input("Telegram Chat ID (optional)", key="c_telegram")
            email = st.text_input("Email", key="c_email")

            if st.button("Add Contact"):
                if name.strip() == "":
                    st.error("Name required")
                else:
                    conn = sqlite3.connect("sos.db")
                    c = conn.cursor()
                    c.execute(
                        "INSERT INTO contacts (user_id, name, phone, telegram_id, email) VALUES (?, ?, ?, ?, ?)",
                        (st.session_state.user_id, name, phone, telegram_id, email)
                    )
                    conn.commit()
                    conn.close()
                    st.session_state.refresh = not st.session_state.refresh
                    st.stop()

    with col2:
        st.subheader("SOS Detection")

        if st.button("Start Camera") and len(contacts) >= 1:
            st.write("Detecting SOS...")

            if detect_sos():
                st.success("SOS detected!")

                ip, lat, lon, location = get_ip_and_location()

                time_now = datetime.now(
                    pytz.timezone("Asia/Kolkata")
                ).strftime("%d %b %Y, %I:%M %p IST")

                if lat and lon:
                    map_link = f"https://www.google.com/maps?q={lat},{lon}"
                else:
                    map_link = "Unavailable"

                sos_message = f"""
🚨 SOS ALERT 🚨

Name: {st.session_state.username}
Time: {time_now}
IP Address: {ip}
Location: {location}
Map: {map_link}

⚠️ Please check up on them as soon as possible.
They could be in danger.
"""

                send_alert(contacts, sos_message)

            else:
                st.info("No SOS detected.")
