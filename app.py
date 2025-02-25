# Streamlit App
import streamlit as st

# Set page configuration (should be the first command)
st.set_page_config(page_title="Growth Mindset Project", page_icon="😎")

st.title("🧠 Growth Mindset AI")
st.header("🚀 Elevate Your Potential!")
st.write("Face challenges, learn from mistakes, and reach your full potential. "
         "This AI-powered app helps you develop a **growth mindset** with reflections, challenges, and achievements!")

# Quote Section
st.header("🌱 Today's Wisdom for Growth ✨")
st.write("Success doesn’t last forever, and failure isn’t the end. What matters is having the courage to keep going.")

# User Challenge Input
st.header("🔥 **What’s Your Bold Move Today?** 💪")
user_input = st.text_input("📝 Describe a challenge you are facing:")

if user_input:
    st.success(f"🚀 You're facing: {user_input}. Keep moving ahead toward your dreams!✨")
else:
    st.warning("⚡ Share Your Challenge to Begin!")

# Reflection Section (Always visible)
st.header("🧠 Review Your Growth! 🚀")
reflection = st.text_area("Share your growth insights!")

if reflection:
    st.success(f"🌟 **Valuable Insights!** Your Reflection: 🧠 {reflection}")
else:
    st.info("🔍 Reflect on your experiences to keep growing! Share your insights.")

# Achievements Section (Always visible)
st.header("🏆 Embrace Your Success! 🚀")
achievements = st.text_input("Tell us about your recent win!")

if achievements:
    st.success(f"🎉 **Great Job!** You Accomplished: 🌟 {achievements}")
else:
    st.info("🌟 **Every Win Matters, Big or Small! Share Yours Now!** 🏆")

# Footer
st.write("---")
st.write("🌱 **Trust Yourself. Growth is a Path, Not a Finish Line!** 🚀")
st.write("© **Created by Muhammad Afham** ✨")
