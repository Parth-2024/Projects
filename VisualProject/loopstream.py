import streamlit as st
import time

# Initialize session state variables if not already set
if 'counter' not in st.session_state:
    st.session_state.counter = 0
    st.session_state.running = False

def start_loop():
    st.session_state.running = True

def stop_loop():
    st.session_state.running = False

st.title("Loop in Streamlit Example")

# Buttons to start and stop the loop
start_button = st.button("Start Loop", on_click=start_loop)
stop_button = st.button("Stop Loop", on_click=stop_loop)

# Display the counter
counter_display = st.empty()

# Main loop
while st.session_state.running:
    st.session_state.counter += 1
    counter_display.write(f"Counter: {st.session_state.counter}")
    time.sleep(1)
    
    # Check for button clicks to stop the loop
    if st.button("Stop Loop", key=f"stop_loop_button{st.session_state.counter}"):
        stop_loop()

# Display the final value of the counter
counter_display.write(f"Final Counter: {st.session_state.counter}")
