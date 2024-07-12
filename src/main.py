from fastapi import FastAPI
from langserve import add_routes

from chain import qa_chain

app = FastAPI(title="LLM App")

# Add QA chain to our app
add_routes(app, qa_chain)
