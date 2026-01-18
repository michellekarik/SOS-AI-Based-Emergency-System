# SOS-AI-Based-Emergency-System
A real-time emergency alert system that detects a specific hand gesture (4 fingers up + thumb folded) using **MediaPipe** and **OpenCV**. When the gesture is recognized, the system automatically sends **Telegram and Email alerts** to registered emergency contacts. 

# **Global SOS Hand Gesture**
<img width="593" height="439" alt="image" src="https://github.com/user-attachments/assets/a5b9b1d1-b1bc-4ae1-a82d-1a9d2602bce5" />

This project includes user authentication, contact management, and SOS logging using **SQLite**.

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
3. Install dependencies  

```bash
pip install -r requirements.txt
