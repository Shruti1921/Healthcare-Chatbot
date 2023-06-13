from flask import Flask, render_template, request
import openai
import config
import os
from dotenv import load_dotenv
app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Configure your OpenAI API credentials
openai.api_key = os.getenv('OPENAI_API_KEY')

# Define your home page
@app.route('/')
def index():
    return render_template('index.html')

# Define your chat endpoint
@app.route('/chat', methods=['POST'])
def chat():
    # Get the user inputs from the request
    condition = request.form['condition']
    severity = request.form['severity']

    # Construct the user query
    user_query = f"Health Condition: {condition}, Severity: {severity}"

    # Call the chatbot function
    response = chat_with_gpt(user_query)

    return response

# Helper function to interact with ChatGPT API
def chat_with_gpt(user_query):
    # Build the prompt with user query
    prompt = f"User: {user_query}\nAssistant:"
    
    # Set the temperature and max tokens for the API call
    temperature = 0.7
    max_tokens = 200
   
    # Generate a chatbot response
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens
        
    )

    # Extract the assistant's reply from the API response
    assistant_reply = response.choices[0].text.strip().replace("Assistant:", "").strip()

    return assistant_reply

if __name__ == '__main__':
    app.run(debug=True)
