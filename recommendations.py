import os
from groq import Groq

analitic_data = {"Search Visibility":'24.1%', '#2 among competitors'
                 "Total Searches":'3.1M', 'Searches last month'
                 "Web Mentions": '3.4M','Mentions across search'
                 "AI Mentions": '443','Mentions in AI results'
                 "Majestic": [85900, 20200, 48000, 4200],
                 "Ahrefs": [36700, 9000, 24200, 893],
                 "Moz": [16800, 3300, 11500, 568],
                 "SE Ranking": [10100, 3000, 6500, 119],
                 "SpyFu": [3000, 922, 1900, 38]}

# Initialize the client with your key from: https://console.groq.com/keys
client = Groq(api_key="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")

# Conversation history to allow follow-up questions
history = [
    {"role": "system", "content": "You are an expert in marketing analytics and competitive intelligence."
    "Provide insights based on the data provided, and give reccomendations to improve search visibility and brand presence online."
    "Once I give you the data, do your best to interprete what its for and your only response to me should be recommnedations based on the data."
    "Try to give unique and creative recommendations that are not obvious, and that are actionable for a small business. "
    "Explain it to me as if I was an investor. Compare the data to competitors, let me know where I stand compared to them. "
    "Give me examples of how to implement the recommendations you give."}
]

def quiry_recommendations(data) -> str:
    # Add the data to the conversation history
    history.append({"role": "user", "content": f"Here is the data: {data}"})
    # Request completion from a Groq-supported model (e.g., Llama 3)
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile", 
        messages=history,
        temperature=0.7,
        max_tokens=1024,
    )
    
    # Get and return the AI response
    ai_response = completion.choices[0].message.content
    return ai_response

"""
while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    # Add user message to history
    history.append({"role": "user", "content": user_input})

    # Request completion from a Groq-supported model (e.g., Llama 3)
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile", 
        messages=history,
        temperature=0.7,
        max_tokens=1024,
    )

    # Get and print response
    ai_response = completion.choices[0].message.content
    print(f"\nAI: {ai_response}")

    # Add AI response to history for context in the next turn
    history.append({"role": "assistant", "content": ai_response})
"""

print(quiry_recommendations(analitic_data))