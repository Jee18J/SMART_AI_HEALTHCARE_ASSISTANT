import streamlit as st
import google.generativeai as genai

# Configure Gemini AI (use your actual API key)
genai.configure(api_key="AIzaSyClwCo8aIpV8gieeDQ5HsjiASODhGkxt-0")

# Model configuration (identical to your Flask version)
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="pediatrician work\nFor example if i ask \"My child has cough for 3 days \" means it should reply like it cold disease \nand give some common medicin names \n\n",
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm your pediatric health assistant. How can I help?"}
    ]

# Page layout
st.set_page_config(page_title="Pediatric Health Assistant", page_icon="👶")
st.title("👶 Pediatric Health Assistant")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask about your child's symptoms..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = model.generate_content(prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"Error: {str(e)}")

# Navigation button using native Streamlit
st.markdown("---")
if st.button("Detailed Symptom Checker", type="primary", use_container_width=True):
    st.switch_page("pages/pediatric_checker.py")  # Native navigation


# import streamlit as st
# import google.generativeai as genai
# import numpy as np
# from io import BytesIO
# import speech_recognition as sr
# import tempfile
# import os

# # Configure Gemini AI
# genai.configure(api_key="AIzaSyClwCo8aIpV8gieeDQ5HsjiASODhGkxt-0")

# # Model configuration
# generation_config = {
#     "temperature": 1,
#     "top_p": 0.95,
#     "top_k": 40,
#     "max_output_tokens": 8192,
#     "response_mime_type": "text/plain",
# }

# model = genai.GenerativeModel(
#     model_name="gemini-1.5-flash",
#     generation_config=generation_config,
#     system_instruction="pediatrician work\nFor example if i ask \"My child has cough for 3 days \" means it should reply like it cold disease \nand give some common medicin names \n\n",
# )

# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = [
#         {"role": "assistant", "content": "Hello! I'm your pediatric health assistant. How can I help?"}
#     ]

# # Initialize speech recognizer
# r = sr.Recognizer()

# def transcribe_audio(audio_bytes):
#     """Convert audio bytes to text using Google Speech Recognition"""
#     try:
#         # Create a temporary WAV file
#         with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
#             tmp.write(audio_bytes.read())
#             tmp_path = tmp.name
        
#         # Use the audio file for recognition
#         with sr.AudioFile(tmp_path) as source:
#             audio_data = r.record(source)
#             text = r.recognize_google(audio_data)
        
#         # Clean up
#         os.unlink(tmp_path)
#         return text
#     except sr.UnknownValueError:
#         st.error("Could not understand audio")
#     except sr.RequestError as e:
#         st.error(f"Could not request results; {e}")
#     except Exception as e:
#         st.error(f"Error: {str(e)}")
#     return None

# # Page layout
# st.set_page_config(page_title="Pediatric Health Assistant", page_icon="👶")
# st.title("👶 Pediatric Health Assistant")

# # Microphone input section
# st.subheader("Voice Input")
# audio_bytes = st.audio_input("Click and speak (hold to record)", key="audio_recorder")

# if audio_bytes:
#     # Display audio player
#     st.audio(audio_bytes, format="audio/wav")
    
#     # Transcribe audio
#     with st.spinner("Processing your voice..."):
#         # Reset file pointer before reading
#         audio_bytes.seek(0)
#         prompt = transcribe_audio(audio_bytes)
        
#         if prompt:
#             st.session_state.messages.append({"role": "user", "content": prompt})
#             with st.chat_message("user"):
#                 st.markdown(f"🎤: {prompt}")

# # Display chat messages
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # Text input fallback
# if prompt := st.chat_input("Or type your question here..."):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(prompt)

# # Process and display responses
# if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
#     with st.chat_message("assistant"):
#         with st.spinner("Thinking..."):
#             try:
#                 response = model.generate_content(st.session_state.messages[-1]["content"])
#                 st.markdown(response.text)
#                 st.session_state.messages.append({"role": "assistant", "content": response.text})
#             except Exception as e:
#                 st.error(f"Error: {str(e)}")

# # Navigation button
# st.markdown("---")
# if st.button("Detailed Symptom Checker", type="primary", use_container_width=True):
#     st.switch_page("pages/pediatric_checker.py")