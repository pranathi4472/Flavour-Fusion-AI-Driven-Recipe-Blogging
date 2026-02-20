import streamlit as st
import google.generativeai as genai
import random

# --- MILESTONE 2: Configuration ---
# PASTE YOUR WORKING API KEY HERE (The one that just gave you the green success message!)
api_key = "AIzaSyAZsyCZSjgYxM32JRkNGtBWC0z_W-6HAGw" 
genai.configure(api_key=api_key)

# Define the Model
generation_config = {
    "temperature": 0.75,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
}

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    generation_config=generation_config,
)

# --- MILESTONE 3: Joke Generation ---
def get_joke():
    jokes = [
        "Why don't programmers like nature? It has too many bugs.",
        "Why did the developer go broke? Because he used up all his cache.",
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why was the JavaScript developer sad? Because he didn't know how to 'null' his feelings.",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem."
    ]
    return random.choice(jokes)

# --- MILESTONE 4: Recipe Generation ---
def recepie_generation(user_input, word_count):
    st.write("🕒 **Generating your recipe...**")
    st.write(f"While I work on creating your blog, here's a joke:\n\n**{get_joke()}**")
    
    try:
        chat_session = model.start_chat(history=[])
        prompt = f"Write a professional recipe blog post about {user_input} in approximately {word_count} words."
        
        response = chat_session.send_message(prompt)
        st.success("✨ Your recipe is ready!")
        return response.text
    except Exception as e:
        st.error(f"Error generating blog: {e}")
        return None

# --- MILESTONE 5: Streamlit Output UI ---
st.set_page_config(page_title="RecepieMaster")
st.title("RecepieMaster: AI-Powered Blog Generation")
st.write("🤖 Hello! I'm recepieMaster, your friendly robot. Let's create a fantastic recipe together!")

topic = st.text_input("Enter the Recipe Topic (e.g., Paneer Curry):")
count = st.number_input("Desired Word Count:", min_value=100, max_value=2000, step=50, value=500)

if st.button("Generate recipe"):
    if topic:
        result = recepie_generation(topic, count)
        if result:
            st.markdown("---")
            st.markdown(result)
    else:
        st.warning("Please enter a recipe topic first!")