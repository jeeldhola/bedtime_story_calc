import streamlit as st
import pandas as pd

# Constants for different models
models = {
    'gpt-4-turbo': {'prompt': 10, 'completion': 30},
    'gpt-4': {'prompt': 30, 'completion': 60},
    'gpt-4-32k': {'prompt': 60, 'completion': 120}
}

# Image cost settings
image_cost_per_image = 0.04  # USD per image (DALL-E 3 standard 1024x1024)
fixed_cost = 1.5  # USD fixed cost to be added to each calculation

# Function to calculate pricing
def calculate_pricing(duration, model):
    tokens_per_minute = 200  # Approx tokens per minute of storytelling
    images_per_story = 2
    tokens = tokens_per_minute * duration
    
    # Get the costs based on the selected model
    token_cost_prompt = (tokens / 1_000_000) * models[model]['prompt']
    token_cost_completion = (tokens / 1_000_000) * models[model]['completion']
    
    # Total token cost (prompt + completion)
    total_token_cost = token_cost_prompt + token_cost_completion
    total_image_cost = images_per_story * image_cost_per_image
    
    # Total cost (tokens + images) plus fixed cost
    total_cost = total_token_cost + total_image_cost + fixed_cost
    return total_cost

# Streamlit UI
st.title('Bedtime Story Pricing Calculator')

# Model selection dropdown
selected_model = st.selectbox(
    "Select a GPT model for generating the story:",
    options=list(models.keys())
)

# Duration dropdown (no range, just individual selection)
selected_duration = st.selectbox(
    'Select the story duration (in minutes):',
    options=range(1, 21)
)

# Calculate pricing for the selected options
total_cost_selected = calculate_pricing(selected_duration, selected_model)

# Maximum cost calculation (20-minute story using the most expensive model, gpt-4-32k)
max_possible_cost = calculate_pricing(20, 'gpt-4-32k')

# Display the cost for the selected duration and model
st.write(f"### Selected Story Details:")
st.write(f"**Model:** {selected_model}")
st.write(f"**Duration:** {selected_duration} minute(s)")
st.write(f"Total Cost for this story : ${total_cost_selected:.4f} USD")

# Display the maximum possible cost
st.write(f"### Maximum Possible Cost for a 20-minute story with gpt-4-32k:")
st.write(f"Maximum Cost:${max_possible_cost:.4f} USD")
