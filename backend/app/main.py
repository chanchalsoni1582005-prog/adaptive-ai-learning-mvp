from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.adaptive_engine import AdaptiveEngine

app = FastAPI()
engine = AdaptiveEngine()

@app.get("/")
def home():
    return {"message": "Adaptive AI Learning API is running"}

@app.get("/question")
def get_question():
    q = engine.get_question()
    return {"id": q["id"], "question": q["question"], "options": q["options"]}

@app.post("/answer/{qid}/{option}")
def answer(qid: int, option: int):
    result = engine.submit_answer(qid, option)
    return {"correct": result, "next_level": engine.level}

@app.get("/report")
def report():
    return {"skill_report": engine.report()}
