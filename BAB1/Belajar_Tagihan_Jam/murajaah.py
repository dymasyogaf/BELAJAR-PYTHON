import streamlit as st
import pandas as pd
import numpy as np

# Tittle of the dashboard
st.title("My Dashboard")

# Sidebar for user input
st.sidebar.header("User Input")

# Example of a text input widget
user_input = st.sidebar.text_input("Enter some text", "Hello, streamlit!")

# Example of a slider widget
slider_value = st.sidebar.slider("Select a value", 0, 100, 50)

# Example of a checkbox widget
if st.sidebar.checkbox("Show DataFrame"):
    # Example DataFrame
    df = pd.DataFrame({
        'Column 1': np.random.randn(10),
        'Column 2': np.random.randn(10)
    })
    st.write(df)

# Main content
st.header("Main Content")

# Display user input from sidebar
st.write("You entered: ", user_input)
st.write("Slide value: ", slider_value)

# Example of an interactive map
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(map_data)

# Example of a button
if st.button("Click Me"):
    st.write("Button clicked!")

# Example of a file uploader
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)

# Example of a selectbox
option = st.selectbox(
    'which option do you prefer?',
    ['Option 1', 'Option 2', 'Option 3']
)
st.write('You selected:', option)