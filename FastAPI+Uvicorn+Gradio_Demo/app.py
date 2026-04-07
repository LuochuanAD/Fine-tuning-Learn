from pydantic import BaseModel
from fastapi import FastAPI
from rag import rag
import gradio as gr

app = FastAPI()

class QueryModel(BaseModel):
    query: str




@app.post("/chat")
async def post_rag_answer(req: QueryModel):
    answer = rag(query=req.query)

    return {"answer": answer}   

def gradio_chat(message):
    return rag(query=message)
gradio_app = gr.Interface(fn=gradio_chat, inputs="text", outputs="text", title="RAG Chatbot", description="Ask anything!")

app= gr.mount_gradio_app(app,gradio_app, path="/ui")


@app.get("/")
async def root():
    return {"message": "API is working!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)