print("Step 1: starting...")

import openai
print("Step 2: openai imported")

import gradio as gr
print("Step 3: gradio imported")

import pandas as pd
print("Step 4: pandas imported")

openai.api_key = "your-api-key-here"

df = pd.read_csv("inventory.csv")
print("Step 5: CSV loaded")

inventory_summary = df.to_string(index=False)
print("Step 6: inventory ready")

def analyze_problem(user_question):
    system_prompt = f"""You are an AI supply chain analyst for Apex Foods, 
a regional food distributor. You help logistics managers make fast, 
data-driven decisions.

Here is the current inventory snapshot:
{inventory_summary}

When answering, always:
- Reference specific products and numbers from the data
- Flag any items below their reorder point
- Give a clear recommendation, not just observations
- Keep your response concise and structured with headers
"""
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_question}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content

examples = [
    ["Which products are at risk of stocking out this week?"],
    ["We have a big weekend sale coming. What should we reorder immediately?"],
    ["Which supplier should we contact first and why?"],
    ["Summarize the overall inventory health and top 3 actions to take today."]
]

app = gr.Interface(
    fn=analyze_problem,
    inputs=gr.Textbox(
        lines=3,
        placeholder="Describe your supply chain problem or question...",
        label="Your Question"
    ),
    outputs=gr.Textbox(
        lines=15,
        label="AI Analysis"
    ),
    title="Apex Foods — AI Supply Chain Assistant",
    description="Ask any supply chain or inventory question in plain English.",
    examples=examples,
    
)

print("Step 7: launching app...")
app.launch(theme=gr.themes.Soft())