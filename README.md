# SOS-AI-Based-Emergency-System
A real-time emergency alert system that detects a specific hand gesture (4 fingers up + thumb folded) using **MediaPipe** and **OpenCV**. When the gesture is recognized, the system automatically sends **Telegram and Email alerts** to registered emergency contacts. This project includes user authentication, contact management, and SOS logging using **SQLite**.

**🚨 The Reality of Emergencies**

In many dangerous situations, people cannot type, call, or speak. When someone is in immediate danger:
- Hands may be shaking
- Voice may be blocked
- Typing may be impossible
- They may not have time to explain
- They may be physically unable to reach the phone

That’s why gesture-based SOS is essential. It allows the user to silently send an emergency alert without saying a word.

**When SOS is detected, the system sends the following information: Time of SOS, Username (full name preferably), IP Address, Google Maps Link, Location (Latitude & Longitude), Default SOS Message “Check up on them as soon as possible. They could be in danger.”**


This is important because:
- The message is simple and direct
- It immediately signals urgency
- It avoids confusion and reduces response time


# **Global SOS Hand Gesture**
<img width="890" height="553" alt="image" src="https://github.com/user-attachments/assets/9182b7b8-64fb-45cc-ab41-90c0856103e4" />




---

## 🔥 Features

✅ Real-time SOS detection using webcam  
✅ Gesture-based SOS activation (4 fingers up + thumb folded)  
✅ Telegram + Email alert notifications  
✅ User authentication (Register/Login)  
✅ Add up to 3 emergency contacts  
✅ Logs time, IP address, location, and user info  
✅ Clean Streamlit UI for easy interaction  

---
## 🛠️ Tech Stack

- **Python**
- **Streamlit** (UI)
- **OpenCV** (Webcam + image processing)
- **MediaPipe** (Hand gesture detection)
- **SQLite** (Database)
- **Telegram Bot API**
- **SMTP Email Notifications**
- **ipapi.co** (Location from IP)

---

## ⚙️ Setup

1. Clone the repo  
2. Create a virtual environment  
3. Install python 3.10.x and dependencies: opencv-python, streamlite, requests, mediapipe, smtplib, pytz 
pip install -r requirements.txt
4. Add the following variables to .env file
TELEGRAM_TOKEN=YOUR_BOT_TOKEN
EMAIL_ADDRESS=YOUR_EMAIL@gmail.com
EMAIL_PASSWORD=YOUR_APP_PASSWORD
5. Run the app using command in terminal
streamlit run app.py



