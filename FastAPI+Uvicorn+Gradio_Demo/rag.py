from typing import List, Optional

documents = [
    "this is a document",
    "this is another document",
    "this is a third document"
]

def retrieve(query: str, top_k: int = 2) -> List[str]:
    # For simplicity, we will just return the top_k documents that contain the query
    results = []
    for doc in documents:
        if query in doc:
            results.append(doc)
    return results[:top_k]

def generate_answer(query: str, retrieved_docs: List[str]) -> str:
    # For simplicity, we will just concatenate the retrieved documents to form an answer
    answer = f"Answer to '{query}':\n"
    for doc in retrieved_docs:
        answer += f"- {doc}\n"
    return answer
def rag(query: str, top_k: int = 2) -> str:
    retrieved_docs = retrieve(query, top_k)
    answer = generate_answer(query, retrieved_docs)
    return answer
# Example usage
if __name__ == "__main__":
    query = "document"
    answer = rag(query)
    print(answer)

