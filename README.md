# AI Supply Chain Assistant

A web app that lets logistics managers describe supply chain problems 
in plain English and get structured AI-powered recommendations instantly.

## The problem it solves
Supply chain managers waste time manually cross-referencing inventory 
spreadsheets to find what needs reordering and who to call. This tool 
answers those questions in seconds.

## How it works
- Type a question in plain English
- The app analyzes current inventory data using AI
- Returns specific product recommendations, stock levels, and supplier actions

## Example questions
- "Which products are below their reorder point right now?"
- "We have a big weekend sale coming. What should we reorder immediately?"
- "Which supplier should we contact first and why?"
- "Summarize overall inventory health and top 3 actions to take today."

## Tech stack
- Python
- OpenAI API (GPT-3.5-turbo)
- Gradio
- Pandas

## How to run
1. Clone this repo
2. Install dependencies: `pip install openai gradio pandas`
3. Add your OpenAI API key to `app.py`
4. Run: `python app.py`
5. Open `http://127.0.0.1:7860` in your browser

## Built by
Lorenzo Dillard — Technical PM transitioning into AI development.
Background in supply chain operations and data systems at PepsiCo.
