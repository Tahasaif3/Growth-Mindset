import streamlit as st # type: ignore
import datetime
import json
import os
from streamlit_extras.colored_header import colored_header # type: ignore
from streamlit_card import card # type: ignore
import plotly.express as px # type: ignore

# File to store user data
DATA_FILE = "user_journal.json"

st.set_page_config(
    page_title="Growth Mindset Journal",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    /* Main container styling */
    .main {
        padding: 2rem;
    }
    
    /* Custom card styling */
    .stCard {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    
    /* Input fields styling */
    .stTextInput input, .stTextArea textarea {
        background-color: #f8f9fa;
        border-radius: 12px;
        border: 1px solid #e9ecef;
        padding: 15px;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #4CAF50;
        box-shadow: 0 0 0 2px rgba(76, 175, 80, 0.2);
    }
    
    /* Button styling */
    .stButton>button {
        border-radius: 12px;
        padding: 10px 25px;
        background: linear-gradient(45deg, #4CAF50, #45a049);
        color: white;
        font-weight: 600;
        border: none;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(76, 175, 80, 0.2);
    }
    
    /* Progress bar styling */
    .stProgress > div > div {
        background-color: #4CAF50;
        border-radius: 10px;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 10px 15px;
    }
    
    /* Header styling */
    h1, h2, h3 {
        color: #2E7D32;
        font-family: 'Segoe UI', sans-serif;
    }
    
    /* Emoji size */
    .emoji-large {
        font-size: 24px;
    }
    
    /* Custom container */
    .custom-container {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

user_data = load_data()

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("<h1 style='text-align: center;'>🚀 Growth Mindset Journal</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.2em;'>Your Daily Self-Growth Companion</p>", unsafe_allow_html=True)
    
    with st.container():
        username = st.text_input("", placeholder="Enter your name...", key="username")
        if username:
            st.markdown(f"<h3 style='text-align: center;'>👋 Welcome, {username}!</h3>", unsafe_allow_html=True)

    today = datetime.date.today().strftime("%Y-%m-%d")
    st.markdown(f"<p style='text-align: center; color: #666;'>{today}</p>", unsafe_allow_html=True)

    st.markdown("### How are you feeling today? 🌟")
    mood_cols = st.columns(3)
    with mood_cols[0]:
        happy = st.button("😊 Happy")
    with mood_cols[1]:
        neutral = st.button("😐 Neutral")
    with mood_cols[2]:
        sad = st.button("😞 Sad")
    
    mood = "😊 Happy" if happy else "😐 Neutral" if neutral else "😞 Sad" if sad else None

    with st.container():
        st.markdown("### Daily Reflection ✍️")
        reflection = st.text_area(
            "What did you learn today?",
            height=150,
            placeholder="Share your thoughts and learnings..."
        )

    st.markdown("### Tomorrow's Goal 🎯")
    goal = st.text_input("", placeholder="Set one goal for self-improvement...")

    # Progress Tracking
    st.markdown("### Progress Tracker 📊")
    progress = st.slider("How much have you achieved today?", 0, 100, 0)
    st.progress(progress / 100)

    if progress == 100:
        st.balloons()
        st.success("🎉 Amazing progress! Keep up the great work!")

    if st.button("Save Today's Entry 📌", key="save"):
        if username:
            if username not in user_data:
                user_data[username] = {}
            user_data[username][today] = {
                "mood": mood,
                "reflection": reflection,
                "goal": goal,
                "progress": progress
            }
            save_data(user_data)
            st.success("✨ Entry saved successfully!")
        else:
            st.warning("⚠️ Please enter your name first")

    if username and username in user_data:
        st.markdown("---")
        st.markdown("### Your Journey So Far 📅")
        
        tab1, tab2 = st.tabs(["📝 Entries", "📊 Analytics"])
        
        with tab1:
            for date, entry in sorted(user_data[username].items(), reverse=True):
                with st.expander(f"📅 {date} | {entry['mood']}"):
                    st.markdown(f"**Reflection:**\n{entry['reflection']}")
                    st.markdown(f"**Goal:**\n{entry['goal']}")
                    st.progress(entry['progress'] / 100)
        
        with tab2:
            moods = [entry['mood'] for entry in user_data[username].values()]
            mood_counts = {mood: moods.count(mood) for mood in set(moods)}
            
            fig = px.pie(
                values=list(mood_counts.values()),
                names=list(mood_counts.keys()),
                title="Mood Distribution",
                color_discrete_sequence=px.colors.qualitative.Set3
            )
            st.plotly_chart(fig)

st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-style: italic; color: #666;'>"
    "💭 \"Progress is not about being better than someone else, "
    "it's about being better than you used to be.\""
    "</p>", 
    unsafe_allow_html=True
)