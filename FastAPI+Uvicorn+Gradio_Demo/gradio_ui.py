import gradio as gr
import requests

API_URL = "http://localhost:8000/chat"

def chat_with_api(query):
    response = requests.post(API_URL, json={"query": query})
    if response.status_code == 200:
        return response.json().get("answer", "No answer found.")
    else:
        return f"Error: {response.status_code}"

with gr.Blocks() as demo:
    gr.Markdown("## RAG Chatbot")
    query_input = gr.Textbox(label="Enter your query:")
    submit_button = gr.Button("Submit")
    answer_output = gr.Textbox(label="Answer:", interactive=False)

    submit_button.click(fn=chat_with_api, inputs=query_input, outputs=answer_output)    


if __name__ == "__main__":
    demo.launch()